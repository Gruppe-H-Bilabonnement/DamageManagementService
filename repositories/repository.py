import sqlite3

# Retrieve all damage reports
def db_retrieve_all_damage_reports():
    try:
        connection = sqlite3.connect('damage_report.db')
        connection.row_factory = sqlite3.Row 
        cursor = connection.cursor()

        # Retrieve all damage reports
        cursor.execute(
            """
            SELECT * FROM damage_reports
            """
        )
        reports = cursor.fetchall()
        return [dict(row) for row in reports]
    except sqlite3.Error as error:
        print(f"Database error: {error}")
    finally:
        connection.close()


# Retrieve a damage report by id
def db_retrieve_damage_report_by_id(report_id):
    try:
        connection = sqlite3.connect('damage_report.db')
        connection.row_factory = sqlite3.Row 
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM damage_reports WHERE report_id = ?
            """, (report_id,)
        )
        report = cursor.fetchone()
        if report:
            return dict(report)
        else:
            return None
    except sqlite3.Error as error:
        print(f"Database error: {error}")
    finally:
        connection.close()


# Add a new damage report
def db_add_new_damage_report(data):
    try:
        connection = sqlite3.connect('damage_report.db')
        connection.row_factory = sqlite3.Row 
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO damage_reports (car_id, report_date, total_cost, damage_description, status)
            VALUES (?, ?, ?, ?, ?)
            """, (
                data['car_id'], 
                data['report_date'], 
                data['total_cost'], 
                data['damage_description'], 
                data['status']
            )
        )
        connection.commit()
        return "Damage report added successfully"
    except sqlite3.Error as error:
        print(f"Database error: {error}")
    finally:
        connection.close()


# Update a damage report by id
def db_update_damage_report(report_id, data):
    try:
        connection = sqlite3.connect('damage_report.db')
        connection.row_factory = sqlite3.Row 
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE damage_reports
            SET car_id = ?, report_date = ?, total_cost = ?, damage_description = ?, status = ?
            WHERE report_id = ?
            """, (
                data['car_id'], 
                data['report_date'], 
                data['total_cost'], 
                data['damage_description'], 
                data['status'], 
                report_id
            )
        )
        connection.commit()
        return "Damage report updated successfully"
    except sqlite3.Error as error:
        print(f"Database error: {error}")
    finally:
        connection.close()


# Remove a damage report by id
def db_remove_damage_report_by_id(report_id):
    try:
        connection = sqlite3.connect('damage_report.db')
        connection.row_factory = sqlite3.Row 
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM damage_reports WHERE report_id = ?
            """, (report_id,)
        )
        connection.commit()
        return "Damage report removed successfully"
    except sqlite3.Error as error:
        print(f"Database error: {error}")
    finally:
        connection.close()

# Retrieve all damage reports by car_id
def db_retrieve_all_damage_reports_by_car_id(car_id):
    try:
        connection = sqlite3.connect('damage_report.db')
        connection.row_factory = sqlite3.Row 
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM damage_reports WHERE car_id = ?
            """, (car_id,)
        )
        reports = cursor.fetchall()
        return [dict(row) for row in reports]
    except sqlite3.Error as error:
        print(f"Database error: {error}")
    finally:
        connection.close()
