import unittest
from HEDIS_data_loader import insert_HEDIS_data
import sqlite3


class TestInsertPatients(unittest.TestCase):
	"""Setup create and teardown PATIENT :memory: database"""
	def setUp(self):
		"""Setup PATIENT :memory: database"""
		self.connection = sqlite3.connect(':memory:')
		self.cursor = self.connection.cursor()

	def tearDown(self):
		"""Teardown PATIENT :memory: database"""
		self.connection.close()

	def test_insert_HEDIS_data(self):
		"""Create PATIENT table :memory: database"""
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS PATIENT (
				Pid INTEGER PRIMARY KEY,
				Fname TEXT,
				Minit TEXT,
				Lname TEXT,
				Bdate DATE,
				Street TEXT,
				City TEXT,
				State TEXT,
				Zip TEXT,
				Phone TEXT,
				Sex TEXT
			)
		""")

		insert_HEDIS_data()
		two = 2
		three = 3
		five = two + three

		# test if 5 were inserted correctly
		self.cursor.execute('SELECT COUNT(*) FROM PATIENT')
		self.assertEqual(self.cursor.fetchone()[0], 5)
		self.assertEqual(self.cursor.fetchone()[0], five)

		self.cursor.execute('SELECT * FROM PATIENT WHERE Pid=1')
		patient = self.cursor.fetchone()
		self.assertEqual(patient[1], 'John')
		self.assertEqual(patient[2], 'A')
		self.assertEqual(patient[3], 'Smith')

		# test other patient records
		# TODO test random first, middle and last from fnames database

if __name__ == "__main__":
	unittest.main()
