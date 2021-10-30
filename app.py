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

    # reset_db_tables(app) # delete tables and fill with sample data
    
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
        
        if query:
            podcast = query.format()
            return jsonify({
                'success': True,
                'podcasts': podcast
            })
        else:
            abort(404)


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
        
        if query:
            speaker = query.format()
            return jsonify({
                'success': True,
                'podcasts': speaker
            })
        else:
            abort(404)


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
        
        if query:
            episode = query.format()
            return jsonify({
                'success': True,
                'podcasts': episode
            })
        else:
            abort(404)
        

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
                # Search in Podcasts for author and name
                query_author = (
                    Podcast.query
                    .filter(Podcast.author.ilike("%{}%".format(search)))
                )
                author_results = [podcast.format() for podcast in query_author]

                query_name = (
                    Podcast.query
                    .filter(Podcast.name.ilike("%{}%".format(search)))
                )
                name_results = [podcast.format() for podcast in query_name]

                search_count = len(name_results)+len(author_results)

                result = {
                    'success': True,
                    'author_search': author_results,
                    'name_search': name_results,
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
                    'podcast': podcast.format()
                }

        except IndexError:
            db.session.rollback()
            print(sys.exc_info())
            abort(422)

        finally:
            db.session.close()

        return jsonify(result)


    @app.route('/speakers', methods=['POST'])
    def create_search_speaker():
        body = request.get_json()
        new_name = body.get('name', None)
        new_image_link = body.get('image', None)
        new_twitter_link = body.get('twitter', None)
        new_website_link = body.get('website', None)
        search = body.get('search', None)

        try:
            if search:
                # Search in Speakers for names
                
                query_name = (
                    Speaker.query
                    .filter(Speaker.name.ilike("%{}%".format(search)))
                )
                name_results = [speaker.format() for speaker in query_name]

                search_count = len(name_results)

                result = {
                    'success': True,
                    'name_search': name_results,
                    'results': search_count
                }
            else:
                # POST a new question
                speaker = Speaker(
                    name=new_name,
                    image=new_image_link,
                    twitter=new_twitter_link,
                    website=new_website_link
                )
                speaker.insert()
                result = {
                    'success': True,
                    'speaker': speaker.format()
                }

        except IndexError:
            db.session.rollback()
            print(sys.exc_info())
            abort(422)

        finally:
            db.session.close()

        return jsonify(result)

    
    @app.route('/episodes', methods=['POST'])
    def create_search_episodes():
        body = request.get_json()
        new_title = body.get('title', None)
        new_topics = body.get('topics', None)
        new_podcast_link = body.get('link', None)
        new_speaker_id = body.get('speaker_id', None)
        new_podcast_id = body.get('podcast_id', None)
        search = body.get('search', None)

        try:
            if search:
                # Search in Episodes for titles and topics
                
                query_title = (
                    Episode.query
                    .filter(Episode.title.ilike("%{}%".format(search)))
                )
                title_results = [episode.format() for episode in query_title]

                query_topics = (
                    Episode.query
                    .filter(Episode.topics.ilike("%{}%".format(search)))
                )
                topics_results = [episode.format() for episode in query_topics]

                search_count = len(title_results)+len(topics_results)

                result = {
                    'success': True,
                    'title_search': title_results,
                    'topics_search': topics_results,
                    'results': search_count
                }
            else:
                # POST a new question
                episode = Episode(
                    title=new_title,
                    topics=new_topics,
                    link=new_podcast_link,
                    speaker_id=new_speaker_id,
                    podcast_id=new_podcast_id
                )
                episode.insert()
                result = {
                    'success': True,
                    'episode': episode.format()
                }

        except IndexError:
            db.session.rollback()
            print(sys.exc_info())
            abort(422)

        finally:
            db.session.close()

        return jsonify(result)

    '''
    DELETE Endpoints
    '''

    @app.route('/podcasts/<int:podcast_id>', methods=['DELETE'])
    def delete_podcast(podcast_id):
        try:
            podcast = Podcast.query.get(podcast_id)
            podcast.delete()
            result = {
              'success': True,
            }
        except IndexError:
            db.session.rollback()
            print(sys.exc_info())
            if podcast is None:
                abort(404)
            else:
                abort(422)

        finally:
            db.session.close()

        return jsonify(result)
        

    @app.route('/speakers/<int:speaker_id>', methods=['DELETE'])
    def delete_speaker(speaker_id):
        try:
            speaker = Speaker.query.get(speaker_id)
            speaker.delete()
            result = {
              'success': True,
            }
        except IndexError:
            db.session.rollback()
            print(sys.exc_info())
            if speaker is None:
                abort(404)
            else:
                abort(422)

        finally:
            db.session.close()

        return jsonify(result)

    @app.route('/episodes/<int:episode_id>', methods=['DELETE'])
    def delete_episode(episode_id):
        try:
            episode = Episode.query.get(episode_id)
            episode.delete()
            result = {
              'success': True,
            }
        except IndexError:
            db.session.rollback()
            print(sys.exc_info())
            if episode is None:
                abort(404)
            else:
                abort(422)

        finally:
            db.session.close()

        return jsonify(result)

    '''
    PATCH Endpoints
    '''
    @app.route('/podcasts/<int:podcast_id>', methods=['PATCH'])
    def update_podcast(podcast_id):
        body = request.get_json()
        new_author = body.get('author', None)
        new_name = body.get('name', None)
        new_image = body.get('image', None)
        new_podcast_link = body.get('podcast_link', None)
        

        try:
            podcast = Podcast.query.get(podcast_id)
            podcast.author = new_author
            podcast.name = new_name
            podcast.image = new_image
            podcast.podcast_link = new_podcast_link
            
            result = {
              'success': True,
              'podcast': podcast.format()
            }
        except IndexError:
            db.session.rollback()
            print(sys.exc_info())
            if podcast is None:
                abort(404)
            else:
                abort(422)

        finally:
            db.session.close()

        return jsonify(result)


    @app.route('/speakers/<int:speaker_id>', methods=['PATCH'])
    def update_speaker(speaker_id):
        body = request.get_json()
        new_name = body.get('name', None)
        new_image = body.get('image', None)
        new_twitter = body.get('twitter', None)
        new_website = body.get('website', None)
        

        try:
            speaker = Speaker.query.get(speaker_id)
            speaker.name = new_name
            speaker.image = new_image
            speaker.twitter = new_twitter
            speaker.website = new_website
            
            result = {
              'success': True,
              'speaker': speaker.format()
            }
        except IndexError:
            db.session.rollback()
            print(sys.exc_info())
            if speaker is None:
                abort(404)
            else:
                abort(422)

        finally:
            db.session.close()

        return jsonify(result)
    
    @app.route('/episodes/<int:episode_id>', methods=['PATCH'])
    def update_episode(episode_id):
        body = request.get_json()
        new_title = body.get('title', None)
        new_topics = body.get('topics', None)
        new_podcast_link = body.get('link', None)
        new_speaker_id = body.get('speaker_id', None)
        new_podcast_id = body.get('podcast_id', None)

        try:
            episode = Episode.query.get(episode_id)
            episode.title = new_title
            episode.topics = new_topics
            episode.link = new_podcast_link
            episode.speaker_id = new_speaker_id
            episode.podcast_id = new_podcast_id
            result = {
              'success': True,
              'episode': episode.format()
            }
        except IndexError:
            db.session.rollback()
            print(sys.exc_info())
            if episode is None:
                abort(404)
            else:
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