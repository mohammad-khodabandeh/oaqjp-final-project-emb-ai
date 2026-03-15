# -*- coding: ascii -*-
"""
emotion detection endpoint
==========================

"""
from flask import Blueprint, jsonify

emotion_bp = Blueprint("emotion_bp", __name__)


@emotion_bp.get("/emotionDetector")
def emotion_detection():
    """
    emotion detection endpoint
    """
    return jsonify({"status": "ok"})
