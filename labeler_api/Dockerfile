# Latest fastapi base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Initalize container with requirements
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy app directory
COPY ./app /app/app

# Default PG Host for connecting to host postgres instance from container
ENV PG_HOST host.docker.internal
