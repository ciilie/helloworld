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
       """test that the response code is 200"""
       response = urllib2.urlopen('http://localhost/')
       response_content = response.read()
       self.assertEqual(response.code, 200)


   def test_gettasks(self):
       """Test that the default tasks return correctly"""
       response = urllib2.urlopen('http://localhost/gettasks')
       response_content = response.read()
       self.assertIn("Buy groceries",response_content)

