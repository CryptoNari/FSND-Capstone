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
The following instructions are based on a linux cli environment and can vary on different operating systems.

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
You can follow the postgres [Documentation](https://www.postgresql.org/docs/14/tutorial-createdb.html)to set up your local database
    -   Main DB
    -   Test DB    
Within the setup.sh file replace the Database Urls with your own Postgres Database Urls
Run the setup.sh file to set the needed environment variables for the following steps.

Execute:
```
python manage.py db upgrade
```
to setup the db models.

# Authentification
Due to a hard limit of the web_token expiry of 1 day(dee following [thread](https://community.auth0.com/t/how-to-change-the-access-token-expiry/10222/9)),
it could be necessary to update the JWT Access tokens in the setup.sh file.

Go to the 

[Auth0 Login](https://fseduc.eu.auth0.com/authorize?audience=Capstone&response_type=token&client_id=bSgXoBEDSZqwv66BZJcU8TvzR71qaW3q&redirect_uri=https://127.0.0.1:8080/login-results)

and use the following login credentials to get new valid tokens:

Admin: capstoneadmin@fsnd.com PW: Capstone!2021
User: capstoneuser@fsnd.com PW: Capstone!2021

In the browser address line you get the a redirection with a new valid access token:

https://127.0.0.1:8080/login-results#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNCZ2MtOVdzcGxMaDJ3dFp3cVZfNCJ9.eyJpc3MiOiJodHRwczovL2ZzZWR1Yy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE4MTA4ZWNlM2M2MTgwMDZhYjhiY2Q4IiwiYXVkIjoiQ2Fwc3RvbmUiLCJpYXQiOjE2MzYwMTMwMjMsImV4cCI6MTYzNjA5OTQyMywiYXpwIjoiYlNnWG9CRURTWnF3djY2QlpKY1U4VHZ6UjcxcWFXM3EiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkYXRhIiwicGF0Y2g6ZGF0YSIsInBvc3Q6ZGF0YSJdfQ.ZtwLF7KOyTexshxz8qStZCrVRemaPWlIIGE-h-CCQb4i8FQqImHNt-x5N9ck9COgUdJrHcho-0aaLf3LZYmXUwnHZnf5_VmMqIgEkR5GDxBiKd9SWk1Sul3yLMlx3-jaBkEWcuOnyHZm-S1xpbs3wWJU_kCTZFmPWbpiPLLGorrYkJZxN3zhYvzmKiAaR0ykQEc4aaAqCZrcgS5ENsqxvZCN485LfMjq3dl3B79hCGS-NbDP3XRNMbFr8YNEZEOyBzOsbf_0QOdEkmUro2_pbuIqeKPWLhKaMv3-1mGV4aU-L6oxBHOYymBYNqI8PSwzEuzwRYkWLjGnwnJnQf80DA&expires_in=86400&token_type=Bearer


Copy the access token and replace it inside the setup.sh file.

To logout a user use the following link:

[Logout](https://fseduc.eu.auth0.com/v2/logout?client_id=bSgXoBEDSZqwv66BZJcU8TvzR71qaW3q&returnTo=https://127.0.0.1:8080/logout)

# Execute Bash file with environment variables

To setup the necessary environment variables execute:
```
source setup.sh
```

# Test Local Installation
Run the following command from the root folder within your venv:
```
python tests/test_app.py
```
Your local installation is set up correctly when all tests pass.

# Run/Start the local dev server
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
-  PATCH '/podcasts/<id>', '/speakers/<id>' and '/episodes/<id>'
-  DELETE '/podcasts/<id>', '/speakers/<id>' and '/episodes/<id>'

### Roles

-   Admin
    -   All permissions from 'Registered User'
    -   Can update and delete db entries

-   User:
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

To successfully run the curl requests, Authentication tokens are provided in the setup.sh file
If not already done, run the setup.sh file to set the environment variables.

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

#### GET ('/podcasts/int:podcast_id')
- General:
    - Fetches podcast of given podcast_id
- Sample:
    - `curl https://fsnd-capstone2021.herokuapp.com/podcasts/19`

- Returns:
```
{
    "success":true,
    "podcast":{
        "id":19,
        "author":"Robert Breedlove",
        "name":"The 'What is money?' Show",
        "image":"https://production.listennotes.com/podcasts/the-what-is-money-show-robert-breedlove-LZHEONsqo51-4XBAzvpCmj0.1400x1400.jpg",
        "podcast_link":"https://open.spotify.com/show/25LPvm8EewBGyfQQ1abIsE",
        "speakers":2,
        "episodes":4
    }
}
```

#### GET ('/speakers/int:speaker_id')
- General:
    - Fetches speaker of given speaker_id
- Sample:
    - `curl https://fsnd-capstone2021.herokuapp.com/speakers/7`

- Returns:
```
{
    "success":true,
    "speaker":{
        "id":7,
        "name":"Michael Saylor",
        "image_link":"https://unchainedpodcast.com/wp-content/uploads/2021/01/Michael_Saylor.jpg",
        "twitter_link":"https://twitter.com/saylor",
        "website_link":"https://www.hope.com",
        "episodes":2
    }
}
```

#### GET ('/episodes/int:episode_id')
- General:
    - Fetches episode of given id
- Sample:
    - `curl https://fsnd-capstone2021.herokuapp.com/episodes/9`

- Returns:
```
{
    "success":true,
    "episode":{
        "id":9,
        "title":"The Saylor Series | Episode 1",
        "topics":"Bitcoin","podcast_link":"https://open.spotify.com/episode/5vTqGVN513uTGX1yXcKzJu",
        "speaker_id":7,
        "speaker_name":"Michael Saylor",
        "podcast_id":19,
        "podcast_name":"The 'What is money?' Show"
    }
}
```

#### POST ('/podcasts')

- General:
    - Post new podcast or search podcast depending on request data
    
 ##### New Podcast

    Request data {
        'author'='Author name',  # String
        'name'='Podcast Name',  # String
        'image'='Image Link',   # String
        'podcast_link'='podcast_link'    # String
    }

- Authentification
    - needs Bearer Token with Authorization header 'post:data'
- Sample:
    ```
    curl --request POST https://fsnd-capstone2021.herokuapp.com/podcasts \
    -d '{"author":"Test","name":"Test","image":"Test","podcast_link":"Test"}' \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $ADMIN_TOKEN"
    ```

- Returns:
```
{
    "success":true,
    "podcast":{
        "id":27,
        "author":"Test",
        "name":"Test",
        "image":"Test",
        "podcast_link":"Test",
        "speakers":0,
        "episodes":0
    }
}
```

##### search Podcast

- search in Podcasts for author and name

    Request data {
        'search'='Robert',  # String
    }

- Authentification
    - needs Bearer Token with Authorization header 'post:data'
- Sample:
    ```
    curl --request POST https://fsnd-capstone2021.herokuapp.com/podcasts \
    -d '{"search":"Robert"}' \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $ADMIN_TOKEN"
    ```

- Returns:
```
{
    "success":true,
    "author_search":[
        {
            "id":19,
            "author":"Robert Breedlove",
            "name":"The 'What is money?' Show",
            "image":"https://production.listennotes.com/podcasts/the-what-is-money-show-robert-breedlove-LZHEONsqo51-4XBAzvpCmj0.1400x1400.jpg",
            "podcast_link":"https://open.spotify.com/show/25LPvm8EewBGyfQQ1abIsE",
            "speakers":2,
            "episodes":2
        }
    ],
    "name_search":[],
    "results":1
}
```

#### POST ('/speakers')

- General:
    - Post new speaker or search speaker depending on request data
    
 ##### New Speaker

    Request data {
        'name'='Speaker name',  # String
        'image_link'='Image link',  # String
        'twitter_link'='Twitter Link',   # String
        'website_link'='Podcast link'    # String
    }

- Authentification
    - needs Bearer Token with Authorization header 'post:data'

- Sample:
    ```
    curl --request POST https://fsnd-capstone2021.herokuapp.com/speakers \
    -d '{"name":"Test","image_link":"Test","twitter_link":"Test","website_link":"Test"}' \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $ADMIN_TOKEN"
    ```

- Returns:
```
{
    "success":true,
    "speaker":{
        "id":13,
        "name":"Test",
        "image_link":"Test",
        "twitter_link":"Test",
        "website_link":"Test",
        "episodes":0
    }
}
```

##### search Speaker

- search in Speakers for Speaker name

    Request data {
        'search'='Michael',  # String
    }

- Authentification
    - needs Bearer Token with Authorization header 'post:data'

- Sample:
    ```
    curl --request POST https://fsnd-capstone2021.herokuapp.com/speakers \
    -d '{"search":"Michael"}' \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $ADMIN_TOKEN"
    ```

- Returns:
```
{
    "success":true,
    "name_search":[
        {
            "id":7,"name":"Michael Saylor",
            "image_link":"https://unchainedpodcast.com/wp-content/uploads/2021/01/Michael_Saylor.jpg",
            "twitter_link":"https://twitter.com/saylor",
            "website_link":"https://www.hope.com",
            "episodes":1
        }
    ],
    "results":1
}
```

#### POST ('/episodes')

- General:
    - Post new episode or search speaker depending on request data
    
 ##### New Episode

    Request data {
        'title'='Title',  # String
        'topics'='Topics',  # String
        'podcast_link'='Podcast link'    # String
        'podcast_id'= 23,  # Integer, ForeignKey Podcast.id
        'speaker_id'= 9   # Integer, ForeignKey Speaker.id
    }

- Authentification
    - needs Bearer Token with Authorization header 'post:data'

- Sample:
    ```
    curl --request POST https://fsnd-capstone2021.herokuapp.com/episodes \
    -d '{"title":"Test","topics":"Test","podcast_link":"Test","podcast_id":23,"speaker_id":9}' \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $ADMIN_TOKEN"
    ```

- Returns:
```
{
    "success":true,
    "episode":{
        "id":17,
        "title":"Test",
        "topics":"Test",
        "podcast_link":"Test",
        "speaker_id":9,
        "speaker_name":"Raoul Pal",
        "podcast_id":23,
        "podcast_name":"The Defiant"
    }
}
```

##### search Episodes

- search in Episodes for Episode title and topics

    Request data {
        'search'='Ethereum',  # String
    }

- Authentification
    - needs Bearer Token with Authorization header 'post:data'

- Sample:
    ```
    curl --request POST https://fsnd-capstone2021.herokuapp.com/episodes \
    -d '{"search":"Ethereum"}' \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $ADMIN_TOKEN"
    ```

- Returns:
```
{
    "success":true,
    "title_search":[
        {
            "id":11,
            "title":"The biggest, clearest bet of all is Ethereum",
            "topics":"Ethereum",
            "podcast_link":"https://open.spotify.com/episode/77Q1Ngg76PuexnZDRzSniO",
            "speaker_id":9,
            "speaker_name":"Raoul Pal",
            "podcast_id":23,"podcast_name":"The Defiant"
        }
    ],
    "topics_search":[
        {
            "id":11,
            "title":"The biggest, clearest bet of all is Ethereum",
            "topics":"Ethereum",
            "podcast_link":"https://open.spotify.com/episode/77Q1Ngg76PuexnZDRzSniO",
            "speaker_id":9,
            "speaker_name":"Raoul Pal",
            "podcast_id":23,
            "podcast_name":"The Defiant"
        }
    ],
    "results":2
}
```

#### PATCH ('/podcasts/int:podcast_id')

- General:
    - Update podcast of given podcast id

    Request data {
        'author'='Author name',  # String
        'name'='Podcast Name',  # String
        'image'='Image Link',   # String
        'podcast_link'='podcast_link'    # String
    }

- Authentification
    - needs Bearer Token with Authorization header 'patch:data'

- Sample:
    ```
    curl --request PATCH https://fsnd-capstone2021.herokuapp.com/podcasts/19 \
    -d '{"author":"Robert Breedlove","name":"The What is money? Show ","image":"Test_Update","podcast_link":"https://open.spotify.com/show/25LPvm8EewBGyfQQ1abIsE"}' \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $ADMIN_TOKEN"
    ```

- Returns:
```
{
    "success":true,
    "podcast":{
        "id":19,
        "author":"Robert Breedlove",
        "name":"The What is money? Show ",
        "image":"https://production.listennotes.com/podcasts/the-what-is-money-show-robert-breedlove-LZHEONsqo51-4XBAzvpCmj0.1400x1400.jpg",
        "podcast_link":"https://open.spotify.com/show/25LPvm8EewBGyfQQ1abIsE",
        "speakers":2,
        "episodes":2
    }
}
```

#### PATCH ('/speakers/int:speaker_id')

- General:
    - Update Speaker of given Speaker id

    Request data {
        'name'='Speaker name',  # String
        'image_link'='Image link',  # String
        'twitter_link'='Twitter Link',   # String
        'website_link'='Podcast link'    # String
    }

- Authentification
    - needs Bearer Token with Authorization header 'patch:data'

- Sample:
    ```
    curl --request PATCH https://fsnd-capstone2021.herokuapp.com/speakers/9 \
    -d '{"name":"Raoul Pal","image_link":"Test_Update","twitter_link":"https://twitter.com/RaoulGMI","website_link":"https://www.realvision.com/"}' \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $ADMIN_TOKEN"
    ```

- Returns:
```
{
    "success":true,
    "speaker":{
        "id":9,
        "name":"Raoul Pal",
        "image_link":"Test_Update",
        "twitter_link":"https://twitter.com/RaoulGMI",
        "website_link":"https://www.realvision.com/",
        "episodes":2
    }
}
```
#### PATCH ('/episodes/int:episode_id')

- General:
    - Update Episode of given Episode id

    Request data {
        'title'='Speaker name',  # String
        'topics'='Speaker name',  # String
        'podcast_link'='Podcast link'    # String
        'podcast_id'= 23,  # Integer, ForeignKey Podcast.id
        'speaker_id'= 9   # Integer, ForeignKey Speaker.id
    }

- Authentification
    - needs Bearer Token with Authorization header 'patch:data'

- Sample:
    ```
    curl --request PATCH https://fsnd-capstone2021.herokuapp.com/episodes/13 \
    -d '{"title":"What traditional Investors think of Bitcoin","topics":"Bitcoin","podcast_link":"Test_Update","podcast_id":21,"speaker_id":9}' \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $ADMIN_TOKEN"
    ```

- Returns:
```
{
    "success":true,
    "episode":{
        "id":13,
        "title":"What traditional Investors think of Bitcoin",
        "topics":"Bitcoin",
        "podcast_link":"Test_Update",
        "speaker_id":9,
        "speaker_name":"Raoul Pal",
        "podcast_id":21,
        "podcast_name":"The What Bitcoin Did Podcast"
    }
}
```

#### DELETE ('/podcasts/int:podcast_id')

- General:
    - DELETE podcast of given podcast id
    - All depended Episodes has to be deleted first.

- Authentification
    - needs Bearer Token with Authorization header 'delete:data'
- Sample:
    ```
    curl --request DELETE https://fsnd-capstone2021.herokuapp.com/podcasts/28 \
    -H "Authorization: Bearer $ADMIN_TOKEN"
    ```

- Returns:
```
{
    "success":true,
    "deleted_id":28
}
```

#### DELETE ('/speakers/int:speaker_id')

- General:
    - Delete Speaker of given Speaker id
    - All depended Episodes has to be deleted first.

- Authentification
    - needs Bearer Token with Authorization header 'delete:data'
- Sample:
    ```
    curl --request DELETE https://fsnd-capstone2021.herokuapp.com/speakers/15 \
    -H "Authorization: Bearer $ADMIN_TOKEN"
    ```

- Returns:
```
{
    "success":true,
    "deleted_id":15
}
```
#### DELETE ('/episodes/int:episode_id')

- General:
    - Delete Episode of given Episode id

- Authentification
    - needs Bearer Token with Authorization header 'delete:data'
- Sample:
    ```
    curl --request DELETE https://fsnd-capstone2021.herokuapp.com/episodes/18 \
    -H "Authorization: Bearer $ADMIN_TOKEN"
    ```

- Returns:
```
{
    "success":true,
    "deleted_id":18
}
```