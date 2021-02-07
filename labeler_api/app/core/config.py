import os

PROJECT_NAME = os.getenv("PROJECT_NAME", "RescueLabeler")  # Project Name
VERSION = os.getenv("VERSION", "0.1.0")  # Current Version
DEBUG = True  # Run App in debug mode

API_PREFIX = os.getenv("API_PREFIX", "")  # Endpoint prefix for all endpoints

LOG_DIR = os.getenv("LOG_DIR", "./logs")  # Default log output dir

PG_USER = os.getenv("PG_USER", "postgres")  # pg user
PG_PASS = os.getenv("PG_PASS", "")  # pg password
PG_HOST = os.getenv("PG_HOST", "localhost")  # pg host
PG_PORT = os.getenv("PG_PORT", "5432")  # pg port
PG_DBNAME = os.getenv("PG_DBNAME", "rescue_labeler_db")  # pg dbname

# construct engine URI
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DBNAME}"
)
