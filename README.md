# 🧪 DB_USER_TESTS — Automated validation for user registration with SQLite

This project implements a robust suite of automated tests to validate the logic, rules, and persistence of a user registration system using a local SQLite database. The solution includes modular organization, database seeding, and rule validation — designed to simulate realistic QA scenarios and improve code reliability.

---

## ✅ Main Goals Achieved

- Automated validation of user creation with custom business rules
- Reusable database setup with schema and data seeding scripts
- Dynamic test database initialization with `init_db.py`
- Validation of edge-case inputs (empty fields, duplicates, invalid formats)
- Use of `pytest` fixtures and modular structure for clarity and reuse
- Centralized database connection handling
- Practical QA-style project with local persistence and test separation

---

## 📘 What I Learned

- How to write automated tests for a database-backed system
- Creating reusable test environments using SQL + Python
- Using `conftest.py` to manage test database setup and teardown
- Writing unit tests that validate both logic and persistence
- How to simulate real-world QA scenarios and rule validations
- Structuring a test project for readability and extensibility
- Isolating test logic from utilities and setup routines

---

## 🛠 Technologies & Tools

- Python
- Pytest
- SQLite
- SQL (DDL & DML)
- VS Code
- Git & GitHub

---

## 🧪 Included Tests

- ✅ User creation with valid data
- 🚫 Attempted creation with invalid or missing fields
- 🔁 Duplicate user rejection
- 📏 Validation of business rules (e.g., name length, required fields)
- 🔍 Assertions that data is correctly stored in the database
- 💥 Handling of invalid formats and extreme input values

---

## 📁 Final Project Structure

DB_USER_TESTS/
├── db/
│   ├── schema.sql              # SQL DDL script to create tables             
│   ├── seed_users.sql          # Optional SQL data seeding script           
│   └── users.db                # SQLite test database file                  
├── tests/
│   ├── conftest.py             # Pytest fixtures for DB setup               
│   ├── test_create_user.py     # Tests for valid and invalid user creation  
│   └── test_validation_rules.py# Tests for rule validation and edge cases   
├── utils/
│   └── db_connection.py        # Centralized DB connection helper           
├── .gitignore                  # Excludes venv, DBs, cache                  
├── init_db.py                  # Python script to initialize the database   
├── requirements.txt            # Python dependencies                        
├── seed_db.py                  # Optional seeding runner script             
└── README.md                   # Project documentation                      

---

## 🧭 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/lucasprog18/DB_USER_TESTS.git
cd DB_USER_TESTS

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize the test database
python init_db.py

# 5. Run all tests
pytest -v

# 6. (Optional) Seed data into the database
python seed_db.py
```

---

## 🚀 Possible Future Improvements

- Add type hinting and static validation with `mypy`
- Integrate with GitHub Actions for CI/CD test execution
- Extend to test more CRUD operations (update, delete)
- Switch to an in-memory SQLite engine for faster tests
- Modularize business logic for easier mocking and unit-level isolation
- Add test coverage reports with `pytest-cov`
- Convert rules into formal schema validation (e.g., with Pydantic)

---

## ✅ Conclusion

This project demonstrates how to combine automated testing, database handling, and validation logic into a clean, testable structure that mirrors real-world QA demands. It's ideal for junior QA engineers, automation developers, or anyone learning how to test systems with persistence layers in a professional way.

---

By Lucas Gonçalves Da Silva


