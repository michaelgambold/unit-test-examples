# Unit Test Examples

This repo has examples of how to do unit testing/mocking/spying with different
programing languages/frameworks.

There is a different project/folder for each variation that will contain it's
own README on how to run the project. The format will be
`PROGRAMMING_LANGUAGE-TESTING_FRAMEWORK`.

Every example will implement same functionality (as far as code goes) and
will test/mock/spy on the same thing. This will give a direct comparison
for the different programming language/testing frameworks.

Code coverage reporting (at some level) will also be included for reference.

## Test Scenario

The testing scenario is pretty simple. There will be a main function that will
simply return the reponse from an "API" module that has a "get data" method.
In this method it will execute a HTTP request to an endpoint that doesn't exist
in real life.

We will then create tests on the API method simulating the HTTP requests
for the following status codes (200, 404 and 500). This will return data,
null/None or throw an exception respectively. This means that a HTTP request
will be executed but it will be intercepted and processed locally with the
response we define in the tests.

The main function will then be tested with the same tests as the previous
paragraph (i.e. return data, null/None or exception) however we will be
mocking the "get data" method. This means that when testing the main function
a HTTP request will never actually occur.
