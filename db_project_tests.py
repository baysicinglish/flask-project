import sqlite3
import unittest
import db_project

class ProjectTests(unittest.TestCase):

    def setUp(self):
        self.database = db_project.Database()

    def test_connect_returns_database_connection_object(self):
        self.assertTrue(isinstance(self.database.connect('test.sqlite3'), object))

    #def test_main_connects_to_database(self):

    

