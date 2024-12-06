import sqlite3
import pandas as pd

def create_damage_reports_table():
    try:
        # Create a connection to the database
        connection = sqlite3.connect('damage_report.db')
        connection.row_factory = sqlite3.Row 
        cursor = connection.cursor()
        # Create the damage_reports table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS damage_reports (
            report_id INTEGER PRIMARY KEY,
            car_id INTEGER NOT NULL,
            report_date DATE NOT NULL,
            total_cost FLOAT NOT NULL,
            damage_description TEXT NOT NULL,
            status TEXT NOT NULL
        )
        """)
    except sqlite3.Error as e:
        print(f"Error creating damage_reports table: {e}")
    finally:
        connection.commit()
        connection.close()
