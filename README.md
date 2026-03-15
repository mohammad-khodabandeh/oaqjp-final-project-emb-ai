# Repository for final project

A lightweight Flask web application that analyzes input text and returns
emotion scores together with the dominant emotion using an external NLP
emotion detection service.

## Project Structure

    final_project/
    ├── EmotionDetection/
    │   ├── __init__.py
    │   └── emotion_detection.py
    ├── templates/
    │   └── index.html
    ├── static/
    │   └── mywebscript.js
    ├── tests/
    │   └── test_emotion_detection.py
    ├── server.py
    ├── requirements.txt
    ├── development.txt
    └── pyproject.toml

## Install Dependencies

Install runtime dependencies:

    pip3 install -r requirements.txt

Install development dependencies (testing + linting):

    pip3 install -r development.txt

## Run the Application

Start the Flask server:

    python3 server.py

The application will be available at:

    http://localhost:5000

## Run Tests

Run the full test suite:

    python3 -m pytest

Run a specific test file:

    python3 -m pytest tests/test_emotion_detection.py

## Notes

-   Emotion analysis logic is implemented in
    `EmotionDetection/emotion_detection.py`.
-   The Flask web server is defined in `server.py`.
-   Unit tests verify the dominant emotion for sample inputs.

