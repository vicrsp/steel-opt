# Dockerfile - use Python 3.12 and run tests in the `models` folder
FROM python:3.12-slim

WORKDIR /code
# copy whole project into the image

# upgrade pip, install pytest and project dependencies if present
RUN python -m pip install --upgrade pip setuptools wheel && \
    pip install pytest && \
    if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; \
    elif [ -f pyproject.toml ]; then pip install --no-cache-dir .; fi

COPY ./models /code/models

# run tests in the models folder by default
CMD ["pytest", "models", "-q"]