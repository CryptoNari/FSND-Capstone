import os
import sys
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Podcast, Speaker, Episode, setup_db, db
from tests.sample import reset_db_tables                    


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    app.config['JSON_SORT_KEYS'] = False

    reset_db_tables(app) # delete tables and fill with sample data
    
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

    '''
    GET Endpoints
    '''

    @app.route('/', methods={'GET'})
    def home():
        return jsonify({
            'success': True,
            'message': 'Healthy'
        })

    @app.route('/podcasts', methods={'GET'})
    def get_podcasts():
        query = Podcast.query.all()
        podcasts = [podcast.format() for podcast in query]

        return jsonify({
            'success': True,
            'podcasts': podcasts
        })

    @app.route('/podcasts/<int:podcast_id>', methods={'GET'})
    def get_podcast_id(podcast_id):
        query = Podcast.query.filter(Podcast.id == podcast_id).one_or_none()
        podcast = query.format()

        return jsonify({
            'success': True,
            'podcasts': podcast
        })

    @app.route('/speakers', methods={'GET'})
    def get_speakers():
        query = Speaker.query.all()
        speakers = [speaker.format() for speaker in query]
    
        return jsonify({
            'success': True,
            'speakers': speakers
        })
    
    @app.route('/speakers/<int:speaker_id>', methods={'GET'})
    def get_speaker_id(speaker_id):
        query = Speaker.query.filter(Speaker.id == speaker_id).one_or_none()
        speaker = query.format()

        return jsonify({
            'success': True,
            'podcasts': speaker
        })

    @app.route('/episodes', methods={'GET'})
    def get_episodes():
        query = Episode.query.all()
        episodes = [episode.format() for episode in query]

        return jsonify({
            'success': True,
            'episodes': episodes
        })
    
    @app.route('/episodes/<int:episode_id>', methods={'GET'})
    def get_episode_id(episode_id):
        query = Episode.query.filter(Episode.id == episode_id).one_or_none()
        episode = query.format()

        return jsonify({
            'success': True,
            'podcasts': episode
        })

    '''
    POST Endpoints
    '''

    @app.route('/podcasts', methods=['POST'])
    def create_search_podcast():
        body = request.get_json()
        new_author = body.get('author', None)
        new_name = body.get('name', None)
        new_image_link = body.get('image', None)
        new_podcast_link = body.get('podcast_link', None)
        search = body.get('search', None)

        try:
            if search:
                # Search in author and name in Podcasts
                query_author = (
                    Podcast.query
                    .filter(Podcast.author.ilike("%{}%".format(search)))
                )
                
                query_name = (
                    Podcast.query
                    .filter(Podcast.name.ilike("%{}%".format(search)))
                )

                search_count = len(query_name)+len(query_author)

                result = {
                    'success': True,
                    'author_search': query_author,
                    'name_search': query_name,
                    'results': search_count
                }
            else:
                # POST a new question
                podcast = Podcast(
                    author=new_author, name=new_name,
                    image=new_image_link, podcast_link=new_podcast_link
                )
                podcast.insert()
                result = {
                    'success': True,
                    'question': podcast.format()
                }

        except IndexError:
            db.session.rollback()
            print(sys.exc_info())
            abort(422)

        finally:
            db.session.close()

        return jsonify(result)

    

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