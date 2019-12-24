from django.test import TestCase,Client

# Create your tests here.

class BlogTestCase(TestCase):

    def setUp(self):
        self.c=Client()

    def testIndex_access(self):
        res=self.c.get('/')

        #status code => 200 OK
        #status code => 302 Redirect
        #status code => 404 Not Found
        self.assertEqual(200,res.status_code)

    def test_fail_access(self):
        res=self.c.get('/unknown')
        self.assertEqual(404,res.status_code)
