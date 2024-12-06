from flask import Blueprint, jsonify, request
from flasgger import swag_from
from repositories.repository import (
    db_retrieve_all_damage_reports,
    db_retrieve_damage_report_by_id,
    db_add_new_damage_report,
    db_update_damage_report,
    db_remove_damage_report_by_id,
    db_retrieve_all_damage_reports_by_car_id
)

damage_management_routes = Blueprint('damage_management_routes', __name__)

# Get all damage reports
@damage_management_routes.route('/all', methods=['GET'])
@swag_from('../swagger/docs/get_all_damage_reports.yml')
def get_all_damage_reports():
    try:
        reports = db_retrieve_all_damage_reports()
        return jsonify(reports), 200
    except Exception as error:
        return jsonify({'error': str(error)}), 500


# Retrieve a damage report by ID
@damage_management_routes.route('/report/<int:report_id>', methods=['GET'])
@swag_from('../swagger/docs/get_damage_report_by_id.yml')
def get_damage_report_by_id(report_id):
    try:
        report = db_retrieve_damage_report_by_id(report_id)
        if report:
            return jsonify(report), 200
        else:
            return jsonify({'error': 'Damage report not found'}), 404
    except Exception as error:
        return jsonify({'error': str(error)}), 500


# Add a new damage report
@damage_management_routes.route('/report', methods=['POST'])
@swag_from('../swagger/docs/add_damage_report.yml')
def add_damage_report():
    try:
        data = request.get_json()
        message = db_add_new_damage_report(data)
        return jsonify({'message': message}), 201
    except Exception as error:
        return jsonify({'error': str(error)}), 500


# Update a damage report by ID
@damage_management_routes.route('/report/<int:report_id>', methods=['PUT'])
@swag_from('../swagger/docs/update_damage_report.yml')
def update_damage_report(report_id):
    try:
        data = request.get_json()
        message = db_update_damage_report(report_id, data)
        return jsonify({'message': message}), 200
    except Exception as error:
        return jsonify({'error': str(error)}), 500


# Remove a damage report by ID
@damage_management_routes.route('/report/<int:report_id>', methods=['DELETE'])
@swag_from('../swagger/docs/delete_damage_report.yml')
def delete_damage_report(report_id):
    try:
        message = db_remove_damage_report_by_id(report_id)
        return jsonify({'message': message}), 200
    except Exception as error:
        return jsonify({'error': str(error)}), 500
    

# Retrieve all damage reports by car_id
@damage_management_routes.route('/report/car/<int:car_id>', methods=['GET'])
@swag_from('../swagger/docs/get_damage_reports_by_car_id.yml')
def get_damage_reports_by_car_id(car_id):
    try:
        reports = db_retrieve_all_damage_reports_by_car_id(car_id)
        return jsonify(reports), 200
    except Exception as error:
        return jsonify({'error': str(error)}), 500
