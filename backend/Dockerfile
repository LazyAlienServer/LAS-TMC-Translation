# Pull Base Image
FROM python:3.13.2-slim-bullseye

# Set Environment Variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set Work Directory
WORKDIR /code

# Install Dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy Project
COPY . .
