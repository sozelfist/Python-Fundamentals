# Use a specific syntax version for Dockerfile
# See more: https://docs.docker.com/engine/reference/builder/
# syntax=docker/dockerfile:1.3

# Use a smaller base image with the specified Python version
ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-alpine

# Set the working directory in the container
WORKDIR /src

# Check if make is installed and install if it is not
RUN if [ ! -x /usr/bin/make ]; then apk add --no-cache make; fi

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt /src/

# Install only necessary build dependencies
RUN apk add --no-cache --virtual .build-deps build-base && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

# Copy the current directory contents into the container at /src
COPY . /src/

# Set the entrypoint to be make
ENTRYPOINT ["make"]

