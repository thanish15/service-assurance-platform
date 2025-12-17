from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_recent_metrics(limit=10):
    conn = sqlite3.connect("metrics.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT timestamp, device_ip, metric_name, oid, value FROM snmp_metrics "
        "ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route("/")
def index():
    metrics = get_recent_metrics()
    return render_template("index.html", metrics=metrics)

@app.route("/metrics_data")
def metrics_data():
    conn = sqlite3.connect("metrics.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT timestamp, value FROM snmp_metrics "
        "WHERE metric_name = ? ORDER BY id DESC LIMIT ?",
        ("sysUpTime", 20)
    )
    rows = cursor.fetchall()
    conn.close()
    rows = rows[::-1]  # reverse so oldest first
    timestamps = [r[0] for r in rows]
    values     = [int(r[1]) for r in rows]
    return jsonify({"labels": timestamps, "data": values})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

