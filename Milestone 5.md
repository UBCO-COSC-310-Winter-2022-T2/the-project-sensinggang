# Milestone 5

# Checkpoints:

- [ ]  Checkpoint 1: Completion of User facing components of the application
March 30, 2023
- [ ]  Checkpoint 2: Database/API configuration 
April 5, 2023
- [ ]  Checkpoint 3: Project End tests and integration
April 8, 2023
- [ ]  Checkpoint 4: Video 
April 9, 2023
- [ ]  Final Report and Project Completion April 10, 2023

# Checkpoint 1 (Milestone 5 Submission) Summary:

Our expectation was that this checkpoint would be the most difficult; setting up the git, the workflow, and taking on this entirely new concept of IoT are all challenging enough without additionally having to learn a new framework in a language with which we all had limited experience. In this case, reality followed expectation and there were certainly challenges. Initially setting up the virtual environments, Django, and learning to operate within this new framework took a good portion of our time spend on this checkpoint. Luckily, during our planning phases we added buffers to development targets for this very reason, and our estimations were quite accurate, so we’re still operating within our initial time frame. So, with these initial pains behind us, and all of us feeling more confident with the Django framework, we expect a huge boost in our sprint velocity as we prepare for hitting our next checkpoint. A few key mistakes, which we’d like to learn from were: some omissions to the .gitignore, which resulted in painful merge conflicts, the misappropriation of time for low-priority tasks (time spent on UI instead of more core features). We also found that we ran into the stovepipe anti-pattern, especially in regards to the way the the urls work in the MVC format of Django. We had to do some significant refactoring of the homepage code to integrate the login/createAccount code. We were achieving the same result individually, however the ways we were routing and and rendering views/templates were incompatible with each other out of the box. This taught us to plan more thoroughly in regards to the design of the actual code, as well as doing additional research into the MVC pattern that Django uses.

### For this checkpoint, we have successfully:

- Created a homepage
- Created a master template, structured template directories, constructed templates with stages of inheritance, and linked the static CSS files
- Created a unit test for connection
- Created a subscriptions page, allowing users to select and subscribe to sensors
- Generated mock data in the MQTT model
- Implemented unit tests for views
- Implemented unit tests for login and create account
- Created development branch that is part of our CI pipeline and separate from main branch
- Implemented unit tests for broker connection, subscribing/unsubscribing, and publishing
- Established a Kanban board using GitHub Issues
- Established a workflow posting and completing issues on the GitHub Issues board
- Set up CI pipeline using GitHub actions

### CI/Testing:

Up to date so far, we have been creating individual unit tests within all of our own django apps for testing purposes. The comprehensive list of tests can be found under checkpoint 1 as well as within the [tests.py](http://tests.py) files within each of our app branches on our GitHub repo. We have begun shifting to a continuous integration model using GitHub actions. We created a development branch (named CI) that we will push to and have our tests automatically run. It is also setup to automatically run all unit tests for pushing and pulling to main for when we are ready to integrate the parts of our application. Currently, the development branch just runs the tests from the user branch for login/create account. This are stable tests that are known to pass, and everything works as expected. We are currently each doing unit tests for each of our sections. Planning is in place for integration testing and we will use our CI pipeline to first ensure tests pass to the development branch before merging to main.

### Dockerization:

We have done research into dockerization of our application and plan to use it for deployment. Some of the defined steps are:

1. Create a Dockerfile that specifies the environment for our application, such as the base image, the required dependencies, and any additional configuration. 
2. Use docker-compose to define the services and networking for our application, including the Django apps and the database. 
3. Use Docker containers to run application in a self-contained environment, with all the dependencies and configuration in one place.

# *Checkpoint 1:*

# UI: Sam

## Issues (tasks) to do:

- Integrate other pages (login, manage account, subscribe, etc) to the home page
- Clean up the CSS

## Issues done:

- Design login concept drawing
- Design home page concept drawing
- Create home page view
- Create home page model
- Migrate home page database
- Map home page URL
- Create home page template
- Modify View

## Tests:

- Connection unit test

# Subscribing: Mac

## Issues (tasks) to do:

- Write tests for view functions - displaying data, logged in users to access subscriptions
- Explore connection between server and devices
- Display subscription data
- Harness the data flow between server, publishing IoT client, and subscribing client - data can be displayed in the console but having difficulty storing data for users and producing graphs/tables/representations with the data.
- Develop the web page to display the data flow for each subscription
- Write tests for accurate subscription data retrieval
- Write tests for accurate publish data submission

## Issues done:

- Created subscription app
- Passing test for successful subscribe
- Passing test for successful publish
- Passing test for connect
- Passing test for disconnect
- Passing test for unsubscribe
- Map view to URL
- Created subscription view
- Created subscription template html
- Created Sensor List template html
- Views to allow user to select sensors (checkboxes), displays what sensors the user is currently subscribed to, but no accompanying data yet

## Tests:

- test connection to server
- testing the connection parameters: broker address, port, username, and password
- test subscription method
- test for logged in user subscription
- test for non-logged in user subscription
- test publish method
- test data flow from subscription
- test message handling
- test for multiple subscriptions handling
- test to unsubscribe
- test for subscription and publish data matching

# Login: Joss

## Issues (tasks) to do:

- Add style and nav bar format to login/create account
- Integrate Login (joss) and Home page (sam) by merging branches
- Create more unit tests
- Shift focus to next phase of development which focuses on general integration of components, CD, and dockerization

## Issues done:

- Create login app
- Import django authorization and migrate to create necessary database tables
- Create superuser (admin)
- Create basic start/home page
- Map view to url
- Create login page, redirect to home after successful login
- Create logout page , redirect to home after successful login
- Create user registration page
- Signout feature

## Tests (all currently passing):

### Account Creation Unit Tests

- Valid user registration
- Test for duplicate username
- Test for duplicate email
- Test if username is alpha-numeric
- Test for empty fields
- Test for passwords matching on account creation

### Login Unit Tests

- Test a successful login
- Test an invalid login (this also includes empty fields)

# Graphs: Aryan

## Issues (tasks) to do:

- Create a Django view or API endpoint that retrieves the necessary data from the sensors and/or database.
- Return JSON data for graphical representation.
- Implement the necessary code to display the data using the chosen charting library.
- Ensure that the charts and graphs are responsive and mobile-friendly.
- Implement any necessary features, such as zooming or filtering, to improve the user experience.
    - Asynchronous update on the chart representation ie. dynamic data visualization using AJAX and JavaScript

## Issues done:

- Selected Chart.js/matplotlib as a suitable charting library (might change depending on implementation).
    - View created using matplotlib charting library
- Created [models.py](http://models.py) file to store data and pushed on git under “graphs” branch with necessary files
- Testing graphical representation

## Tests:

(**Implemented two tests to make sure correct data is being displayed**)

- Test the graphical representation on different devices and browsers to ensure that it is responsive and mobile-friendly.
    - 1. Test the dynamic data visualization and ensure it is functioning properly
- Test the data displayed on the charts and graphs to ensure that it is accurate and up-to-date.
- Test any necessary features, such as zooming or filtering, to ensure that they are working correctly and improving the user experience.
- Test Asynchronous display of the graphical representation.