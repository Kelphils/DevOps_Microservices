# !/usr/bin/env bash

# create venv
python3 -m venv ~/.docker

# activate the environment
source ~/.docker/bin/activate

# Build Image
docker build --tag=api .

# List docker images
docker image ls

# Run flask app
docker run -p 8000:5001 api