import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from utils.db_connection import execute_query, fetch_one

def setup_function():
    """Cleans the users table before each test for isolation."""
    execute_query("DELETE FROM users;")


def test_insertion_without_email_should_fail():
    """Should raise an error when inserting a user without an email."""
    with pytest.raises(Exception):
        execute_query(
            "INSERT INTO users (name, cpf) VALUES (?, ?);",
            ("NoEmail User", "999.999.999-99")
        )

def test_insertion_without_cpf_should_fail():
    """Should raise an error when inserting a user without a CPF."""
    with pytest.raises(Exception):
        execute_query(
            "INSERT INTO users (name, email) VALUES (?, ?);",
            ("MissingCPF", "cpf@test.com")
        )


def test_insertion_without_name_should_fail():
    """Should raise an error when inserting a user without a name."""
    with pytest.raises(Exception):
        execute_query(
            "INSERT INTO users (email, cpf) VALUES (?, ?);",
            ("nameless@example.com", "123.456.789-99")
        )

def test_duplicate_cpf_should_fail():
    """Should raise an error when inserting a user with duplicate CPF."""
    cpf = "999.888.777-66"
    user1 = ("Ana", "ana@example.com", cpf)
    user2 = ("João", "joao@example.com", cpf)

    execute_query(
        "INSERT INTO users (name, email, cpf) VALUES (?, ?, ?);",
        user1
    )

    with pytest.raises(Exception):
        execute_query(
            "INSERT INTO users (name, email, cpf) VALUES (?, ?, ?);",
            user2
        )

def test_user_count_after_multiple_inserts():
    """Should insert 3 users and verify the total count in the database."""
    users = [
        ("User 1", "user1@example.com", "111.222.333-44"),
        ("User 2", "user2@example.com", "222.333.444-55"),
        ("User 3", "user3@example.com", "333.444.555-66"),
    ]

    for user in users:
        execute_query("INSERT INTO users (name, email, cpf) VALUES (?, ?, ?);", user)

    count = fetch_one("SELECT COUNT(*) as total FROM users;")["total"]
    assert count == 3




