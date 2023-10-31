# Use the official Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /src

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt /src

# Install only the new dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /src
COPY . /src

# Check if make is installed and install if it is not
RUN if [ ! -x /usr/bin/make ]; then apt-get update && apt-get install -y make; fi

# Set the entrypoint to be make
ENTRYPOINT [ "make" ]

