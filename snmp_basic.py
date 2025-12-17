import time
import sqlite3
from pysnmp.hlapi import (
    SnmpEngine,
    CommunityData,
    UdpTransportTarget,
    ContextData,
    ObjectType,
    ObjectIdentity,
    getCmd
)

def snmp_get(ip, community, oid):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community, mpModel=1),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:
        print(f"Error: {errorIndication}")
        return None
    elif errorStatus:
        print(f"ErrorStatus {errorStatus.prettyPrint()} at {errorIndex}")
        return None
    else:
        for varBind in varBinds:
            oid_str, value = varBind
            return (str(oid_str), value.prettyPrint())

def save_metric(db_path, device_ip, metric_name, oid, value):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    cursor.execute("""
        INSERT INTO snmp_metrics (timestamp, device_ip, metric_name, oid, value)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, device_ip, metric_name, oid, value))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    device_ip = "127.0.0.1"
    community = "public"
    oid = "1.3.6.1.2.1.1.3.0"
    metric_name = "sysUpTime"
    while True:
        result = snmp_get(device_ip, community, oid)
        if result:
            oid_str, value = result
            print(f"{oid_str} = {value}")
            save_metric("metrics.db", device_ip, metric_name, oid_str, value)
            print("Saved to database.")
        time.sleep(60)

