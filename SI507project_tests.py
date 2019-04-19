import sqlite3
import unittest


class FINALSQLiteDBTests(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect("nba_players.db") # Connecting to database that should exist
		self.cur = self.conn.cursor()

	def test_for_nba_players_table(self):
		self.cur.execute("select id, playerid, season, team, fg_pct, rebounds, assists, points from nba_players where id = '1'")
		data = self.cur.fetchone()
		self.assertEqual(data,(1, 1112, '1996-97', 'WAS', 0.348, 58, 2, 38), "Testing data that results from selecting id 1")

	def test_nba_insert_works(self):
		player = (50, 5467, '1998-99', 'DET', 0.980, 20, 80, 270)
		ch = (50, 5467, '1998-99', 'DET', 0.980, 20, 80, 270)
		self.cur.execute("insert or ignore into nba_players(id, playerid, season, team, fg_pct, rebounds, assists, points) values (?, ?, ?, ?, ?, ?, ?, ?)", player)
		self.conn.commit()

		self.cur.execute("select id, playerid, season, team, fg_pct, rebounds, assists, points from nba_players where playerid = '5467'")
		data = self.cur.fetchone()
		self.assertEqual(data,ch,"Testing another select statement after a sample insertion")

	def test_for_nba_teams_table(self):
		res = self.cur.execute("select * from nba_teams")
		data = res.fetchall()
		self.assertTrue(data, 'Testing that you get a result from making a query to the nba_teams table')

	def test_foreign_key_nba(self):
		res = self.cur.execute("select * from nba_players INNER JOIN nba_teams ON nba_players.team = nba_teams.abbrev")
		data = res.fetchall()
		self.assertTrue(data, "Testing that result of selecting based on relationship between nba_players and nba_teams does work")
		self.assertTrue(len(data) in [29, 30, 39, 40], "Testing that there is in fact the amount of data entered that there should have been -- based on this query of everything in both tables.{}".format(len(data)))

	def tearDown(self):
		self.conn.commit()
		self.conn.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
