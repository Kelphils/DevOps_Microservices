FROM python:3.7.3-stretch

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . flask_app/web.py /app/

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

## Expose port no
Expose port 80

# Run app.py at container launch
CMD ["python", "web.py"]
## Complete Step 1:
# Create a Working Directory

## Complete Step 2:
# Copy source code to working directory

## Complete Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013

## Complete Step 5:
# Run app.py at container launch
