# challenge-flask-api

## Context

This project is the last one about deployement. We use different tools we saw in our course like Docker and Flask.

## Description

In this project, I have to deploy an app coded with [Flask](https://flask.palletsprojects.com/en/1.1.x/).

To do so, I created a [Docker](https://docs.docker.com/) container and tried to deploy it with Heroku.

## Usage

You can run the "api.py" you'll be able to access different pages on your local server.

In another hand, you can create and run a Docker container using the "Dockerfile".

## Python libraries

The needed libraries are in the requirement.txt. To install it, use the command below:  

`conda create --name <env> --file requirements.txt`

We use pandas for cleaning the data, geopy to get some new data.

*Links to the official documentation of libraries :*
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Docker](https://docs.docker.com/)

## To do

- Find a solution to be able to deploy the api on the web.

One solution could be:
```
Try changing your Procfile content like this:

web: gunicorn run:app -b "0.0.0.0:$PORT" -w 3

Where run is the name of the main application file denoting run.py
```

- Make prettier pages for the website.

-----
### Author

*Melvin Leroy, junior AI developer at BeCode*
