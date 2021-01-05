FROM python:3.9.1

# Install Flask.
RUN pip install Flask

# Create the directories.
RUN mkdir templates

# Copy the different files.
COPY api.py api.py
COPY templates/base.html templates/base.html
COPY templates/login.html templates/login.html
COPY procfile procfile
COPY heroku.yml heroku.yml

CMD ["python", "api.py"]