from SI507project_final import *
import unittest
import csv
import numpy as np
import random
import itertools
import flask

app = flask.Flask(__name__)

with app.test_request_context('/career_stats/?player_name=Ben Wallace'):
    assert flask.request.path == '/career_stats/'
    assert flask.request.args['player_name'] == 'Ben Wallace'

with app.test_request_context('/bio/?player_name=Ben Wallace'):
    assert flask.request.path == '/bio/'
    assert flask.request.args['player_name'] == 'Ben Wallace'

class TestType(unittest.TestCase):
      def test_assert_is(self):
          self.assertIs(self.rebounds, int)

      def test_assert_is_with_type(self):
          self.assertIs(type(self.assists), int)

if __name__ == "__main__":
    unittest.main(verbosity=2)
