import os

PROJECT_NAME = os.getenv("PROJECT_NAME", "RescueLabeler")  # Project Name
VERSION = os.getenv("VERSION", "0.1.0")  # Current Version
DEBUG = False  # Run App in debug mode

API_PREFIX = os.getenv("API_PREFIX", "")  # Endpoint prefix for all endpoints
