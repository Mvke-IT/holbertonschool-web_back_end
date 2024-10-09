#!/usr/bin/env python3
""" Module of Session Auth views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views, User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Flask view that handles all routes for the Session authentication.
    """

    email = request.form.get('email')
    password = request.form.get('password')

    if not email or len(email) == 0:
        return jsonify({"error": "email missing"}), 400
    if not password or len(password) == 0:
        return jsonify({"error": "password missing"}), 400

    user_instance = User.search({'email': email})
    if not user_instance or len(user_instance) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    if not user_instance[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    user_id = auth.create_session(user_instance[0].id)
    session_id = os.getenv('SESSION_NAME')
    response = jsonify(user_instance[0].to_json())
    response.set_cookie(session_id, user_id)

    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """
    Flask view that handles all routes for the Session authentication.
    """
    from api.v1.app import auth

    delete_session = auth.destroy_session(request)
    if not delete_session:
        abort(404)
    return jsonify({}), 200
