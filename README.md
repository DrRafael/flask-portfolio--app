# Flask Portfolio Web Application with SQLAlchemy

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.1%2B-red.svg)](https://www.sqlalchemy.org/)

A full-stack Flask web application utilizing **SQLAlchemy ORM** for relational data mapping, secure **Werkzeug** password hashing, and dynamic server-side template rendering.

---

## 🚀 Key Features

* **Relational ORM Mapping**: Declarative SQLite database models using `Flask-SQLAlchemy`.
* **Secure Authentication**: Password hashing and verification using `Werkzeug.security` (`generate_password_hash`, `check_password_hash`).
* **Efficient Database Queries**: O(1) indexed lookup queries (`filter_by`) replacing linear table scans.
* **CRUD Functionality**: Full web form lifecycle for creating, reading, and querying card entries.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Framework**: Flask
* **ORM / Database**: Flask-SQLAlchemy, SQLite
* **Security**: Werkzeug

---

## ⚙️ Configuration & Setup

### 1. Clone the repository
git clone https://github.com/DrRafael/flask-portfolio-app.git
cd flask-portfolio-app

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the application
python main.py

---

**Author**: QA Automation Engineer & Python Developer
