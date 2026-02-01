import sqlite3
import pandas as pd
from pathlib import Path

# Resolve project root dynamically
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DB_PATH = PROJECT_ROOT / "battery_model" / "data" / "battery_schedule.db"

def load_schedule():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(
        "SELECT * FROM battery_schedule ORDER BY time", conn
    )
    conn.close()
    return df
