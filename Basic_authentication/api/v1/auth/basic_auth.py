#!/usr/bin/env python3
"""
Module has a class llamed BasicAuth
"""
from api.v1.auth.auth import Auth
from codecs import decode
import base64
from typing import Union, TypeVar
from ..views.users import User


class BasicAuth(Auth):
    """
    Class BasicAuth that inherits from Auth
    """

    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """
        Method that returns the Base64 part of the Authorization header for a
        Basic Authentication
        """
        if not authorization_header or type(authorization_header) is not str\
                or "Basic " not in authorization_header[:6]:
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Method that returns the decoded value of a Base64 string
        'base64_authorization_header'
        """
        try:
            if not base64_authorization_header or\
                    type(base64_authorization_header) is not str:
                return None
            base = base64_authorization_header.encode()
            base = base64.b64decode(base)
            return decode(base, 'utf-8', 'strict')
        except base64.binascii.Error:
            return None
        except UnicodeDecodeError:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> Union[str, str]:
        """
        Method that returns the user email and password from the Base64
        decoded value.
        """
        if not decoded_base64_authorization_header or \
                type(decoded_base64_authorization_header)\
                is not str or ':' not in decoded_base64_authorization_header:
            return None, None

        base_split = decoded_base64_authorization_header.split(':', 1)
        email, pwd = base_split[0], base_split[1]

        return email, pwd

    def user_object_from_credentials(self, user_email: str, user_pwd: str)\
            -> TypeVar('User'):
        """
        Method that returns the User instance based on his email and password.
        """
        user_lists = User.search({'email': user_email})
        if not user_email or type(user_email) is not str or not user_pwd or\
                type(user_pwd) is not str or len(user_lists) == 0 or\
                not user_lists[0].is_valid_password(user_pwd):
            return None
        return user_lists[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that overloads Auth and retrieves the User instance for
        a request.
        """
        user = super().authorization_header(request)
        user = self.extract_base64_authorization_header(user)
        user = self.decode_base64_authorization_header(user)
        user, pwd = self.extract_user_credentials(user)
        user = self.user_object_from_credentials(user, pwd)

        return user
