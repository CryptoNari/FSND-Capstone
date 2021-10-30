import sys
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.base import NOT_EXTENSION
from sqlalchemy.sql.sqltypes import Integer

sys.path.insert(0, '..') # change path to import from parent dir

from app import create_app
from models import test_setup_db, Podcast, Speaker, Episode
from tests.sample import reset_db_tables

"""
Class for Test Cases
"""


class CapstoneTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ["TEST_DATABASE_URL"]
        self.db = SQLAlchemy()
        test_setup_db(self.app, self.database_path)
        query = Podcast.query.all()
        if not query:
            reset_db_tables(self.app)

        self.new_podcast = {
            'author': 'Test author',
            'name': 'Test Name',
            'image': 'image link',
            'podcast_link': 'podcast link'    
        }

        self.search_podcast = {
            'search': 'Robert'
        }

        self.new_speaker = {
            'name': 'Test Name',
            'image': 'image link',
            'twitter': 'podcast link',
            'website': 'weblink'    
        }

        self.search_speaker = {
            'search': 'Michael'
        }

        podcast_query = Podcast.query.first()
        speaker_query = Speaker.query.first()

        self.new_episode = {
            'title': 'Test Name',
            'topics': 'Tets topic',
            'link': 'podcast link',
            'speaker_id': speaker_query.id,
            'podcast_id': podcast_query.id 
        }

        self.search_episode = {
            'search': 'Bitcoin'
        }            
    
    def tearDown(self):
        # Executed after reach test
        pass


    """
    Tests
    """
    # Server status
    def test_get_server_status(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Healthy')


    # GET Database table Endpoints
    def test_get_podcasts(self):
        res = self.client().get('/podcasts')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertNotEqual(len(data['podcasts']), 0)


    def test_get_speakers(self):
        res = self.client().get('/speakers')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertNotEqual(len(data['speakers']), 0)


    def test_get_episodes(self):
        res = self.client().get('/episodes')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertNotEqual(len(data['episodes']), 0)


    # GET id Endpoints + not found
    def test_get_podcast_id(self):
        query = Podcast.query.first()

        res = self.client().get('/podcasts/{}'.format(query.id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['podcasts']['name'], query.name)

    
    def test_get_podcast_id_not_found(self):
        res = self.client().get('/podcasts/{}'.format(12345))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")

    
    def test_get_speaker_id(self):
        query = Speaker.query.first()

        res = self.client().get('/speakers/{}'.format(query.id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['speakers']['name'], query.name)


    def test_get_speaker_id_not_found(self):
        res = self.client().get('/speakers/{}'.format(12345))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")


    def test_get_episode_id(self):
        query = Episode.query.first()

        res = self.client().get('/episodes/{}'.format(query.id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['episodes']['topics'], query.topics)


    def test_get_episode_id_not_found(self):
        res = self.client().get('/episodes/{}'.format(12345))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")

        
    # POST endpoints add data

    def test_create_new_podcast(self):
        res = self.client().post('/podcasts', json=self.new_podcast)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(
            data['podcast']['author'],
            self.new_podcast['author']
        )
        self.assertEqual(
            data['podcast']['name'],
            self.new_podcast['name']
        )
        self.assertEqual(
            data['podcast']['image'],
            self.new_podcast['image']
        )
        self.assertEqual(
            data['podcast']['podcast_link'],
            self.new_podcast['podcast_link']
        )
    
    def test_create_new_speaker(self):
        res = self.client().post('/speakers', json=self.new_speaker)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(
            data['speaker']['name'],
            self.new_speaker['name']
        )
        self.assertEqual(
            data['speaker']['image'],
            self.new_speaker['image']
        )
        self.assertEqual(
            data['speaker']['twitter'],
            self.new_speaker['twitter']
        )
        self.assertEqual(
            data['speaker']['website'],
            self.new_speaker['website']
        )


    # DELETE Endpoints

    def test_delete_podcast(self):
        query = (
            Podcast.query
            .filter(Podcast.author == self.new_podcast['author'])
            .one_or_none()
        )
        podcast_id = query.id
        res = self.client().delete('/podcasts/{}'.format(podcast_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_id'], podcast_id)

    def test_delete_speaker(self):
        query = (
            Speaker.query
            .filter(Speaker.name == self.new_speaker['name'])
            .one_or_none()
        )
        speaker_id = query.id
        res = self.client().delete('/speakers/{}'.format(speaker_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_id'], speaker_id)


if __name__ == "__main__":
    unittest.main()