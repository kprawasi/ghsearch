
import unittest
import app
import search
#tests
class TestGHSearchBackend(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True 

    def test_search_projects_no_query(self):
        response = self.app.get('/search')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing query parameter', str(response.data))

    def test_search_projects_with_query(self):
        response = self.app.get('/search?q=test')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_search_github(self):
        results = search.search_github('test')
        self.assertIsInstance(results, list)
        if results:
            self.assertIn('name', results[0])
            self.assertIn('url', results[0])

if __name__ == '__main__':
    unittest.main()
