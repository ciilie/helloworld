from flask import Flask
from flask_testing import TestCase

TESTING = True

class MyTest(TestCase):
   # executed prior to each test
   def setUp(self):
      app.config['TESTING'] = True
      app.config['WTF_CSRF_ENABLED'] = False
      app.config['DEBUG'] = False
      self.app = app.test_client()
      self.assertEqual(app.debug, False)

   # executed after each test
   def tearDown(self):
      pass

   def create_app(self):
       app = Flask(__name__)
       app.config['TESTING'] = True
       return app


   def test_returncode(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


   def test_gettasks(self):
       response = self.app.get('/gettasks', follow_redirects=True)
       self.assertContains(response, "Buy groceries")
