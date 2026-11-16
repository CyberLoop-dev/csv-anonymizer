import unittest
from main import pseudonym

class CsvAnonymizerTests(unittest.TestCase):
    def test_is_deterministic_for_same_salt(self):
        self.assertEqual(pseudonym("a@example.test", "secret"), pseudonym("a@example.test", "secret"))

    def test_changes_with_salt(self):
        self.assertNotEqual(pseudonym("a@example.test", "one"), pseudonym("a@example.test", "two"))

if __name__ == "__main__":
    unittest.main()
