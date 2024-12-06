from flask import Flask, jsonify, request
import os
from database.initialize import create_damage_reports_table
from api.routes import damage_management_routes
from swagger.config import init_swagger
from flasgger import swag_from
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Initialize Swagger
swagger = init_swagger(app)

# Register the damage_management_routes 
app.register_blueprint(damage_management_routes, url_prefix='/api/v1/damage-management')

# Home route with API documentation for Damage Management
@app.route('/api/v1/', methods=['GET'])
def home():
        return jsonify({
            "message": "Welcome to Damage Management API",
            "endpoints": [
                {
                "method": "GET",
                "endpoint": "/api/v1/",
                "description": "Provides an overview of the API and its endpoints"
                },
                {
                "method": "GET",
                "endpoint": "/api/v1/damage-management/all",
                "description": "Retrieve all damage reports"
                },
                {
                "method": "GET",
                "endpoint": "/api/v1/damage-management/report/<int:report_id>",
                "description": "Retrieve a damage report by ID"
                },
                {
                "method": "POST",
                "endpoint": "/api/v1/damage-management/report",
                "description": "Add a new damage report"
                },
                {
                "method": "PUT",
                "endpoint": "/api/v1/damage-management/report/<int:report_id>",
                "description": "Update a damage report"
                },
                {
                "method": "DELETE",
                "endpoint": "/api/v1/damage-management/report/<int:report_id>",
                "description": "Remove a damage report by ID"
                },
                {
                "method": "GET",
                "endpoint": "/api/v1/damage-management/report/car/<int:car_id>",
                "description": "Retrieve all damage reports by car ID"
                }
            ]
            }


)



# Error handler for 404 not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

# Error handler for 500 internal server error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Init database and run the app
if __name__ == '__main__':
    try:
        # Create a connection to the database
        connection = sqlite3.connect('/home/damage_report.db')
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

    #create_damage_reports_table()
    app.run(host='0.0.0.0', port=80)