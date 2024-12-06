# Damage Management API 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Swagger](https://img.shields.io/badge/swagger-%2385EA2D.svg?style=for-the-badge&logo=swagger&logoColor=black)
![Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)  

A robust, scalable Flask-based API for managing damage reports, designed with modern Python development best practices.

## Project Overview

The Damage Management API streamlines operations for managing vehicle damage reports, including creating, updating, and querying report records. Built with Flask, SQLite, and Docker, it follows a RESTful design pattern and includes detailed Swagger documentation for ease of use.

---

## Key Features

### Technical Highlights
- **Modern Python Stack**: Built with Flask, SQLite, and Swagger for scalable and maintainable development.
- **RESTful API Design**: Provides full CRUD operations for damage reports.
- **Automatic Database Initialization**: Database setup and schema creation included.
- **Interactive Documentation**: Swagger UI for testing and learning API endpoints.
- **Flexible Error Handling**: Standardized JSON responses for errors.

### Functional Capabilities
- Retrieve all damage reports
- Retrieve specific reports by ID or car ID
- Add, update, or delete damage reports
- Flexible integration with external systems

---

## Architectural Design

### System Components

1. **Web Framework**: Flask
   - Lightweight, fast, and easy to extend
   - Provides routing and request handling

2. **Database**: SQLite
   - Serverless, embedded database
   - Handles data storage with automatic table creation

3. **Documentation**: Swagger (via Flasgger)
   - Swagger/OpenAPI specification generation
   - Simple testing interface for endpoints

---

## 📂 Project Structure
```
car-management-service/
│
├── app.py                   # Main application entry point
├── database/
│   └── initialization.py    # Database setup and data loading
│
├── api/
│   └── routes.py            # API endpoint definitions
│
├── repositories/
│   └── repository.py        # Database interaction methods
│
└── swagger/
    ├── config.py            # Swagger configuration
    └── docs/                # Swagger documentation specs
```


---

## API Endpoints

### Base URL: `/api/v1/damage-management`

| Method | Endpoint                                         | Description                                      |
|--------|-------------------------------------------------|--------------------------------------------------|
| GET    | `/api/v1/damage-management/all`                 | Retrieve all damage reports                     |
| GET    | `/api/v1/damage-management/report/<report_id>`  | Retrieve a specific damage report by its ID     |
| GET    | `/api/v1/damage-management/rental/car/<car_id>` | Retrieve all damage reports for a specific car  |
| POST   | `/api/v1/damage-management/report`              | Add a new damage report                         |
| PUT    | `/api/v1/damage-management/report/<report_id>`  | Update an existing damage report by its ID      |
| DELETE | `/api/v1/damage-management/report/<report_id>`  | Remove a damage report by its ID                |

---

## Documentation

### Swagger UI
Interactive API documentation available at: '../api/v1/docs'

---




python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


