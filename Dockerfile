# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock /app/

# Set Python version for pipenv to use (explicitly set to 3.12)
RUN pipenv --python 3.12 install --deploy --ignore-pipfile || tail -n 10 /root/.pipenv/pipenv-*.log

# Copy the rest of the application code
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Run migrations before starting Gunicorn
CMD ["pipenv", "run", "python", "manage.py", "migrate", "&&", "pipenv", "run", "gunicorn", "mySite.wsgi:application", "--bind", "0.0.0.0:8000"]
