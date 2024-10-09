#!/usr/bin/env python3
""" filtered logger """
from typing import List
import re
import logging
from os import environ
import mysql.connector

PII_FIELDS = "email", "name", "ssn", "password", "phone"  # Fields that contain Personally Identifiable Information (PII)

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Redacts specified fields in a message."""
    result = message  # Initialize result with the original message
    for field in fields:  # Iterate over each field that needs to be redacted
        construct = f"(?<={field}=)(.*?)(?={separator})"  # Construct regex pattern to find the field's value
        result = re.sub(construct, redaction, result)  # Replace the field's value with the redaction string
    return result  # Return the redacted message

class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class to redact PII in log messages."""

    REDACTION = "***"  # String used to replace PII
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"  # Log message format
    SEPARATOR = ";"  # Separator used in log messages

    def __init__(self, fields: List[str]):
        """Constructor to initialize the formatter with fields to redact."""
        super(RedactingFormatter, self).__init__(self.FORMAT)  # Initialize the base Formatter with the format
        self.fields: List[str] = fields  # Store the fields to be redacted

    def format(self, record: logging.LogRecord) -> str:
        """Formats the log record and redacts PII."""
        message: str = super().format(record)  # Get the formatted log message
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)  # Redact PII in the message

def get_logger() -> logging.Logger:
    """Creates and configures a logger with PII redaction.

    Returns:
        logging.Logger: Configured logger instance
    """
    result: logging.Logger = logging.getLogger("user_data")  # Create a logger named "user_data"
    result.setLevel(logging.INFO)  # Set the logging level to INFO
    result.propagate = False  # Prevent log messages from being propagated to higher-level loggers
    handler = logging.StreamHandler()  # Create a stream handler for logging to the console
    handler.setFormatter(RedactingFormatter(PII_FIELDS))  # Set the formatter to redact PII
    result.addHandler(handler)  # Add the handler to the logger
    return result  # Return the configured logger

def get_db() -> mysql.connector.connection.MySQLConnection:
    """Establishes a connection to the MySQL database.

    Returns:
        mysql.connector.connection.MySQLConnection: Database connection object
    """
    return mysql.connector.connect(
        user=environ.get("PERSONAL_DATA_DB_USERNAME"),  # Get the database username from environment variables
        password=environ.get("PERSONAL_DATA_DB_PASSWORD"),  # Get the database password from environment variables
        host=environ.get("PERSONAL_DATA_DB_HOST"),  # Get the database host from environment variables
        database=environ.get("PERSONAL_DATA_DB_NAME")  # Get the database name from environment variables
    )