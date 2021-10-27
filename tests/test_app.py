import sys
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

sys.path.insert(0, '..') # change path to import from parent dir

from app import create_app
from models import test_setup_db, Podcast, Speaker, Episode


"""
Class for Test Cases
"""

class CapstoneTestCase(unittest.TestCase):
    def insert_db_test_data(self):
        podcast = Podcast(name="Test Podcast")
        podcast.insert()


    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ["TEST_DATABASE_URL"]
        self.db = SQLAlchemy()
        test_setup_db(self.app, self.database_path)
        self.insert_db_test_data()
            
    
    def tearDown(self):
        # Executed after reach test
        pass

    """
    Tests
    """
    def test_get_server_status(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Healthy')

    def test_db_table_podcast(self):
        test = Podcast.query.first()
      
        self.assertEqual(test.name, 'Test Podcast')

    def test_get_podcasts(self):
        res = self.client().get('/podcasts')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_speakers(self):
        res = self.client().get('/speakers')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_episodes(self):
        res = self.client().get('/episodes')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    

if __name__ == "__main__":
    unittest.main()