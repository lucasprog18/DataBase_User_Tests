# Pytest configuration file with shared fixtures for all test modules

import pytest
from utils.db_connection import execute_query

# This fixture is automatically applied to every test (autouse=True)
# It runs before each test function and ensures that the 'users' table is empty
@pytest.fixture(autouse=True)
def clean_users_table():
    """Truncate the users table before each test to ensure isolation."""
    execute_query("DELETE FROM users;")
