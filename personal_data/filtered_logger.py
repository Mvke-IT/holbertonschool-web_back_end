#!/usr/bin/env python3
"""
Module that have a function called filter_datum that returns the log message
obfuscated
"""
from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Function called filter_datum that returns the log message obfuscated
    """
    for field in fields:
        message = re.sub("(?<={:s}=)(.*?)(?={:s})".format(field, separator),
                         redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Method to filter values in incoming log records using filter_datum
        """
        message = filter_datum(self.fields, RedactingFormatter.REDACTION,
                               record.msg, RedactingFormatter.SEPARATOR)
        message = logging.LogRecord(record.name, record.levelno, None, None,
                                    message, None, None)
        return super().format(message)


def get_logger() -> logging.Logger:
    """
    Logger should be named "user_data" and only log up to logging.INFO level.
    It should not propagate messages to other loggers. It should have a
    StreamHandler with RedactingFormatter as formatter.
    """
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(handler)

    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a connector to the database
    """

    """
    Environment variables
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME') or 'root'
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD') or ''
    _host = os.getenv('PERSONAL_DATA_DB_HOST') or 'localhost'
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    """
    Connection to DataBase
    """
    conection = mysql.connector.connection.MySQLConnection(
        user=username, password=password, host=_host, database=db_name)

    return conection


def main():
    """ Main """
    db_connection = get_db()
    log = get_logger()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * from users")

    rows = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    for row in rows:
        user_info = '; '.join(f"{column_names[i]}={value}" for i, value in
                              enumerate(row))
        log.info(user_info)


if __name__ == '__main__':
    main()