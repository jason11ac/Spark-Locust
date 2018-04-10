# locust_test.py
# In python, '#' is used to indicate a comment line.
"""
The string within triple-quote is also considered as a comment.
And the triple-quote can be used for multiline comments.
DISCLAIMER: This sample doesn't care about whether the use of API is correct.


In this file, we are simulating the scenario where all requests from users are read intensive.
The user whose name is cs144 would randomly open one of his posts via /editor/post?action=open&username=cs144&postid={num},
where {num} is a random postid.
Note: In this test file, use /editor/post?action=open as the name for the requests. Also, make sure that postid that user opens
should be between 1 and 500. Since our user "cs144" only has 500 posts, he will get nothing otherwise!

"""

import sys, random
from locust import HttpLocust, TaskSet

def writePost(locust):
    postid = random.randint(1, 500) #generate a random number from 1 to 500 (include 1 and 500)
    url = '/editor/post?action=save';
    locust.client.post('/editor/post?action=save&username=cs144&postid=' + str(postid) + '&title=Loading%20Test&body=***Hello%20World!***', name=url)


class MyTaskSet(TaskSet):
    """ the class MyTaskSet inherits from the class TaskSet, defining the behavior of the user """
    tasks = {writePost}
    def on_start(locust):
        """ on_start is called when a Locust start before any task is scheduled """


class MyLocust(HttpLocust):
    """ the class MyLocust inherits from the class HttpLocust, representing an HTTP user """
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000
