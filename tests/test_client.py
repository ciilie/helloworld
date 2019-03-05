import urllib2
from flask import Flask
from flask_testing import TestCase

TESTING = True

class MyTest(TestCase):

   def create_app(self):
       app = Flask(__name__)
       app.config['TESTING'] = True
       return app

   # executed prior to each test
   def setUp(self):
       pass

   # executed after each test
   def tearDown(self):
      pass



   def test_serverup(self):
       response = urllib2.urlopen(self.get_server_url('http://localhost/'))
       self.assertEqual(response.code, 200)


   def test_gettasks(self):
       response = urllib2.urlopen(self.get_server_url('http://localhost/gettasks'))
       self.assertContains(response, "Buy groceries")

