# -*- coding: ascii -*-
"""
health chek endpoint
====================

"""
from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health_check():
    """
    regular healthcheck endpoint for the server
    """
    return jsonify({"status": "ok"})
