#!/usr/bin/env python3
"""
Doc
"""
from flask import request
from typing import List, TypeVar
import os


def remove_slash(string: str) -> str:
    """
    Funtion that removes forward slash
    """
    if string[-1] == '/':
        string = string[:-1]
    return string


class Auth():
    """ Doc """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Doc """
        if not path or not excluded_paths or len(excluded_paths) == 0:
            return True
        excluded_path = [remove_slash(paths) for paths in excluded_paths]
        if remove_slash(path) not in excluded_path:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """ Doc """
        if request and 'Authorization' in request.headers.keys():
            return request.headers['Authorization']
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Doc """
        return None

    def session_cookie(self, request=None):
        """
        Method that returns a cookie value from a request:
        """
        if not request:
            return None
        cookie_key = os.getenv('SESSION_NAME')

        return request.cookies.get(cookie_key)
