import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from utils.db_connection import execute_query, fetch_one

def test_insert_user_successfully():
    """Should insert a valid user and retrieve it from the database."""
    # Arrange
    name = "Lucas"
    email = "lucas@test.com"
    cpf = "123.456.789-00"

    execute_query(
        "INSERT INTO users (name, email, cpf) VALUES (?, ?, ?);",
        (name, email, cpf)
    )

    # Act
    result = fetch_one("SELECT * FROM users WHERE email = ?", (email,))

    # Assert
    assert result is not None
    assert result["name"] == name
    assert result["email"] == email
    assert result["cpf"] == cpf
