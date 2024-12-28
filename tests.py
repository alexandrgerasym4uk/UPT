import unittest
from unittest.mock import patch, mock_open
import json
import requests
from UPT import check_internet_connection, check_progress, generate, read_course




class TestCheckInternetConnection(unittest.TestCase):
    
    @patch('requests.get')
    def test_check_internet_connection_success(self, mock_get):
        mock_get.return_value.status_code = 200
        self.assertTrue(check_internet_connection())
        
    @patch('requests.get')
    def test_check_internet_connection_failure(self, mock_get):
        mock_get.side_effect = requests.ConnectionError
        self.assertFalse(check_internet_connection())





progress = [None, [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]

def check_progress():
    global progress
    if all(progress[i][0] == 1 for i in range(1, 6)):
        return 1
    return None

class TestCheckProgress(unittest.TestCase):

    def test_check_progress_success(self):
        global progress
        progress = [None, [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]
        result = check_progress()
        self.assertEqual(result, 1)

    def test_check_progress_failure(self):
        global progress
        progress = [None, [0, 0], [1, 0], [1, 0], [1, 0], [1, 0]]
        result = check_progress()
        self.assertIsNone(result)


class TestGenerate(unittest.TestCase):

    @patch('cohere.Client')
    def test_generate(self, MockCohereClient):
        
        prompt = "Привіт"
        max_t = 100
        result = generate(prompt, max_t)
        
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
