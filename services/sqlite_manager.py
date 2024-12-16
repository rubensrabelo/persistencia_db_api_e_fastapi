import sqlite3
from contextlib import contextmanager


@contextmanager
def get_cursor(connection):
    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        cursor.close()


def create_table():
    ...


def add_data():
    ...


def update_data():
    ...


def remove_data():
    ...
