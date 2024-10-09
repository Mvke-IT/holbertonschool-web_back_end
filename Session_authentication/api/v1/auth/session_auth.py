#!/usr/bin/env python3
"""
Class SessionAuth that inherits from Auth.
"""
from api.v1.auth.auth import Auth
from api.v1.views.users import User
import uuid


class SessionAuth(Auth):
    """
    Methods (create_session and user_id_for_session_id) for storing and
    retrieving a link between a User ID and a Session ID.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Method that creates a Session ID for a user_id
        """
        if not user_id or not isinstance(user_id, str):
            return None
        id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[id] = user_id
        return id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Method that returns a User ID based on a Session ID.
        """
        if not session_id or not isinstance(session_id, str):
            return None
        user_value = SessionAuth.user_id_by_session_id.get(session_id)
        return user_value

    def current_user(self, request=None):
        """
        Method that returns a User instance based on a cookie value
        """
        session_id = super().session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Method that deletes the user session / logout
        """
        if not request:
            return False

        session_id: str = super().session_cookie(request)
        if session_id is None:
            return False

        user_id: str = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            pass
        return True
