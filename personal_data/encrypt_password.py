#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Function that expects one string argument name password and returns
    a salted, hashed password, which is a byte string.
    """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check valid password
    """
    if bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password):
        return True
    return False