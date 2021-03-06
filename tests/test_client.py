import urllib
import urllib2
from flask import Flask
from flask_testing import TestCase

TESTING = True

class MyTest(TestCase):

   def create_app(self):
       app = Flask(__name__)
       app.config['TESTING'] = True
       return app


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


   def test_addtask(self):
       """Test that a new task can be added"""
       post_params = {
           'title': u'Learn Javascript',
           'description': u'Work and experiment 1000 hours of Javascript',
           'done': False
       }
       params = urllib.urlencode(post_params)
       response = urllib2.urlopen('http://localhost/addtask',params)
       response_content = response.read()
       self.assertIn("Learn Javascript",response_content)


   def test_deletetask(self):
       """Test that after removing the last task we dont get any Learn Javascript"""
       request = urllib2.Request('http://localhost/deletetask')
       request.get_method = lambda: 'DELETE'
       response = urllib2.urlopen(request)
       response_content = response.read()
       self.assertNotIn("Learn Javascript", response_content)