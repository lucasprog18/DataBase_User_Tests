# Database User Validation Tests

This repository contains a simple and lightweight suite of automated tests written in Python to validate the behavior and consistency of a SQLite-based user registration database.

## 📌 Purpose

To ensure data integrity, insertion validity, and constraint enforcement in a sample database simulating a real-world user management system.

## ✅ What is being tested

- Successful insertion of valid users
- Unique email enforcement
- Presence of required fields (name, email, CPF)
- CPF and email format validation
- Accurate row count and content checks

## 🧰 Stack

- Python 3.10+
- SQLite3 (built-in)
- pytest
- Faker (optional)

## 📁 Project structure

```
db_user_tests/
├── tests/
│   ├── test_create_user.py
│   └── test_validation_rules.py
├── db/
│   ├── schema.sql
│   └── seed_users.sql
├── utils/
│   └── db_connection.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 How to run

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run tests:

```bash
pytest
```

## 📦 Database

- The project uses SQLite3 and does not require any external server setup.
- Schema and seed data files are located in the `db/` directory.

## 📋 Notes

- All test comments and codebase are written in English for international-readiness.
- Safe to run locally; no external services or sensitive data involved.


