#!/usr/bin/python3

import unittest
import MySQLdb
import os
from console import HBNBCommand

class testmysqlstorage(unittest.TestCase):
    """This class definition is for the purposes of testing the MySQL storage."""

    def setclass(x):
        """This set's up the test environment before any tests are run on it."""

        x.db = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )

        x.cur = x.db.cursor()

    def tearclassdown(x):
        """This cleans up the test setup after all test are run."""
        x.cur.close()
        x.db.close()

    def setUp(self):
        """This function resets the database state prior to each tests."""
        self.cur.execute("DELETE FROM states.""")
        self.db.commit()

    def create_test_states(self):
        """This test creates a new state in the database."""
        self.cur.execute("SELECT COUNT(*) FROM states")
        init_count = self.cur.fetchone()[0]

        HBNBCommand().onecmd("create State name='California'")

        self.cur.execute("SELECT COUNT(*) FROM states")
        next_count = self.cur.fetchone()[0]

        self.assertEqual(init_count, next_count + 1)

if __name__ == "__main__":
    unittest.main()
