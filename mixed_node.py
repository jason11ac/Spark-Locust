# locust_test.py
# In python, '#' is used to indicate a comment line.
"""
The string within triple-quote is also considered as a comment.
And the triple-quote can be used for multiline comments.
DISCLAIMER: This sample doesn't care about whether the use of API is correct.
"""

import sys, random
from locust import HttpLocust, TaskSet

updatef = {
   "title": "Loading Test",
   "body": "***Hello World!***"
}

def editPost(locust):
    """ define a function in python whose name is previewPage and the argument is locust """
    postid = random.randint(1, 500) # generate a random number from 1 to 500 (include 1 and 500)
    url_prefix = '/api/cs144/';
    locust.client.put(url_prefix + str(postid), name="/api/cs144", data=updatef)

def previewPage(locust):
    """ define a function in python whose name is previewPage and the argument is locust """
    postid = random.randint(1, 500) # generate a random number from 1 to 500 (include 1 and 500)
    url_prefix = '/blog/cs144/';
    locust.client.get(url_prefix + str(postid), name="/blog/cs144")

class MyTaskSet(TaskSet):
    """ the class MyTaskSet inherits from the class TaskSet, defining the behavior of the user """
    tasks = {editPost: 1, previewPage: 9}
    def on_start(locust):
        """ on_start is called when a Locust start before any task is scheduled """
        response = locust.client.get("/login?username=cs144&password=password&redirect=/blog/cs144")
        if response.status_code != 200:
            print("FAIL to start with posting data to server. Make sure that your server is running.")
            sys.exit();

class MyLocust(HttpLocust):
    """ the class MyLocust inherits from the class HttpLocust, representing an HTTP user """
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000