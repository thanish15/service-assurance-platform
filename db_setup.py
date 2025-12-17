import sqlite3

def init_db():
    conn = sqlite3.connect("metrics.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS snmp_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            device_ip TEXT,
            metric_name TEXT,
            oid TEXT,
            value TEXT
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database & table ready")
