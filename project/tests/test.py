# project/test.py


import unittest

from project import app


class ProjectTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    ########################
    #### helper methods ####
    ########################

    ###############
    #### tests ####
    ###############

    def test_admin_page(self):
        response = self.app.get('/admin', follow_redirects=True)
        self.assertIn(
            b'Admin stuff', response.data)

    def test_auth_page(self):
        response = self.app.get('/auth/auth', follow_redirects=True)
        self.assertIn(
            b'Auth stuff', response.data)

    def test_bucket_page(self):
        response = self.app.get('/bucket/bucket', follow_redirects=True)
        self.assertIn(
            b'Bucket stuff', response.data)






if __name__ == "__main__":
    unittest.main()
