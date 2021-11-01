# CAPSTONE - Udacity Full Stack Web Developer - Nanodegree Course

This is the final project of the Udacity Full Stack Web Developer Nanodegree Course.

The object is to build an API from start to finish and host it.

Below are the skills taught in the courses summarized which are part of this final project:

- Coding in Python 3
- Relational Database Architecture
- Modeling Data Objects with SQLAlchemy
- Internet Protocols and Communication
- Developing a Flask API
- Authentication and Access
- Authentication with Auth0
- Authentication in Flask
- Role-Based Access Control (RBAC)
- Testing Flask Applications
- Deploying Applications


# Install Project Key Dependencies

## Python
Follow the instructions to install the latest version of python for your platform here: [docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

## Virtual Enviornment
It's recommended to work within a virtual environment whenever using Python for projects to keep your dependencies for each project separate and organaized. 
How to set up the virtual environment you can see here: [docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## PIP Dependecies
Once you have setup your venv, you can install the project dependencies inside
the root directory by running:
```
pip3 install -r requirements.txt
```
This command will install all the required packages included in the requirements.txt file

## Key Dependencies

- [Flask](http://flask.pocoo.org/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

Authentification Service:

- [Auth0](https://auth0.com/docs/)

Deployment Service:

- [Heroku](https://www.heroku.com/what)

# Setup your local Postgres DBs
Within the setup.sh file replace the Database Urls with your own Postgres Database Urls
Run the setup.sh file to set the needed environment variables.
Execute
```
python manage.py db upgrade
```
to setup the db models.

# Test Local Installation
Run the following command from the root folder within your venv:
```
python tests/test_app.py
```
Your local installation is set up correctly when all tests pass.

# Run/Start the server
Run the following command from the root folder within your venv:
```
python app.py
```
## Capstone Api Specifications - Podcasts DB

### Models

- Podcast - List of Podcasts
- Speaker - List of Speakers/Podcast Guests  
- Episode - Podcast Episode with speaker 

### Endpoints

-  Healthcheck GET '/'
-  GET '/podcasts', '/speakers' and '/episodes'
-  GET '/podcasts/<id>', '/speakers/<id>' and '/episodes/<id>'
-  POST '/podcasts', '/speakers' and '/episodes'
-  DELETE '/podcasts/<id>', '/speakers/<id>' and '/episodes/<id>'
-  DELETE '/podcasts/<id>', '/speakers/<id>' and '/episodes/<id>'

### Roles

-   Admin
    -   All permissions from 'Registered User'
    -   Can update and delete db entries

-   Registered User:
    -   Can add and search db entries

-   Everyone is able to proceed GET requests (no login necessary)

#### Authentification tags

-   Admin:
    -   'post:data'
    -   'patch:data'
    -   'delete:data'

-   Registered User:
    -   'post:data'

## API Reference

### Getting Started

-   Deployment URL: https://fsnd-capstone2021.herokuapp.com/
-   Local Hosted URL: The app is hosted at default  http://127.0.0.1:5000/

Authentication....

### Error Handling

The following error types are implemented:

- 400: Bad request
- 401: Unauthorized
- 403: Forbidden
- 404: Resource not found
- 422: Not processable
- 500: Internal server error

Errors arre returned in JSON format:

```
{
  "success": false, 
  "error": 404, 
  "message": "resource not found"
}
```
Authentication Errors (401) provide additional info about the error in the form

```
{
    'code': 'authorization_header_missing',
    'description': 'Authorization header is expected.'
}
```

### Endpoints

The following samples are using the deployment URL.
For local testin you have to replace it with the Local hosted Url. 

#### GET ('/')
- General:
    - Fetches the status of the server
    - Request Arguments: None
- Sample:
    - `curl https://fsnd-capstone2021.herokuapp.com/`

- Returns:
```
{
    "success":true,
    "message":"Healthy"
}
```

#### GET ('/podcasts')
- General:
    - Fetches all podcasts and counts speakers and episodes per podcast
    - Request Arguments: None
- Sample:
    - `curl https://fsnd-capstone2021.herokuapp.com/podcasts`

- Returns:
```
{
    "success":true,
    "podcasts":[{
        "id":10,
        "author":"Robert Breedlove",
        "name":"The 'What is money?' Show",
        "image":"https://production.listennotes.com/podcasts/the-what-is-money-show-robert-breedlove-LZHEONsqo51-4XBAzvpCmj0.1400x1400.jpg",
        "podcast_link":"https://open.spotify.com/show/25LPvm8EewBGyfQQ1abIsE",
        "speakers":2,
        "episodes":2
        },
        ...
    ]
}
```

#### GET ('/speakers')
- General:
    - Fetches all speakers and counts episodes per speaker 
    - Request Arguments: None
- Sample:
    - `curl https://fsnd-capstone2021.herokuapp.com/speakers`

- Returns:
```
{
    "success":true,
    "speakers":[{
        "id":10,
        "name":"Michael Saylor",
        "image":"https://unchainedpodcast.com/wp-content/uploads/2021/01/Michael_Saylor.jpg",
        "twitter":"https://twitter.com/saylor",
        "website":"https://www.hope.com",
        "episodes":2},
        ...
    ]
}
```

#### GET ('/episodes')
- General:
    - Fetches all episodes and gets podcast and speaker name
    - Request Arguments: None
- Sample:
    - `curl https://fsnd-capstone2021.herokuapp.com/episodes`

- Returns:
```
{
    "success":true,
    "episodes":[{
        "id":13,
        "title":"The Saylor Series | Episode 1",
        "topics":"Bitcoin"
        ,"podcast_link":"https://open.spotify.com/episode/5vTqGVN513uTGX1yXcKzJu",
        "speaker-id":10,
        "speaker_name":"Michael Saylor",
        "podcast-id":10,
        "podcast_name":"The 'What is money?' Show"
        },
        ...
    ]
}
```

