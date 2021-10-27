import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Podcast, Speaker, Episode, setup_db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    app.config['JSON_SORT_KEYS'] = False
  
    '''
    Set up CORS
    '''
    cors = CORS(app, resources={r"/*": {'origins': '*'}})

    '''
    set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization'
        )
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, POST, PATCH, DELETE, OPTIONS'
        )
        return response


    @app.route('/', methods={'GET'})
    def home():
        return jsonify({
            'success': True,
            'message': 'Healthy'
        })

    @app.route('/podcasts', methods={'GET'})
    def get_podcasts():
        query = Podcast.query.all()
        print('-------Query Podcasts-------')
        print(query)
        podcasts = [podcast.format() for podcast in query]
        print('-------Formatted Podcasts-------')
        print(podcasts)
    
        return jsonify({
            'success': True,
            'podcasts': podcasts
        })

    @app.route('/speakers', methods={'GET'})
    def get_speakers():
        query = Speaker.query.all()
        print('-------Query Speakers-------')
        print(query)
        speakers = [speaker.format() for speaker in query]
        print('-------Formatted Speakers-------')
        print(speakers)
    
        return jsonify({
            'success': True,
            'speakers': speakers
        })

    @app.route('/episodes', methods={'GET'})
    def get_episodes():
        query = Episode.query.all()
        print('-------Query Episodes-------')
        print(query)
        episodes = [episode.format() for episode in query]
        print('-------Formatted Episodes-------')
        print(episodes)
    
        return jsonify({
            'success': True,
            'episodes': episodes
        })

    '''
    Error handlers for expected errors
    '''
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400


    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401


    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "forbidden"
        }), 403


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500


    """ @app.errorhandler(AuthError)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.description
        }), error.status_code """

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    #app.run()