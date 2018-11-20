# Circulate - Demo App for CircleCI

[![CircleCI](https://circleci.com/gh/CircleCI-Public/circleci-demo-python-flask.svg?style=svg&circle-token=6715e4f37e6b8cee04ea7f1812ac00fb135199f9)](https://circleci.com/gh/CircleCI-Public/circleci-demo-python-flask/)

**Original Author Credit:** This is directly based on Miguel Grinberg's excellent [Flasky](https://github.com/miguelgrinberg/flasky) application.

This is a working application using Python and Flask that you can use to learn how to build, test and deploy with CircleCI 2.0. Follow the [Project Walkthrough](https://circleci.com/docs/2.0/project-walkthrough/) guide here.

It's a 'social blogging' web application similar to Twitter. Users can create accounts, make posts, follow users and comment on posts. You can *circualate* your thoughts and ideas :-)

**IMPORTANT:**

- You **do not need to know Python to follow the guide** in the CircleCI docs.
- You will not need to install or setup a Python environment to follow the tutorial - you can follow along by making edits to config on GitHub if you wish.
- No matter what language or stack you are going to use with CircleCI, we recommend following the walkthrough first, as it introduces concepts about CircleCI that you can then apply to your own project.

## Deployment to Heroku

The application also demonstrates how to deploy to Heroku from CircleCI 2.0. Please consult the [Project Walkthrough](https://circleci.com/docs/2.0/project-walkthrough/) for documentation on how this works.

## Running locally
**Note:** As mentioned above you don't need to run this application locally to learn about using CircleCI.

### 1. Setup your Local Environment & Clone the Circulate Repo

The following commandline instructions are for Mac users. For other operating systems, install Postgres [these](https://www.postgresql.org/download/) instructions, and Python using [these](https://www.python.org/downloads/) instructions.

#### Install Postgres
`$ brew install postgres`

#### Install Python
`$ brew install python`

#### Fork or clone this repository
`$ git clone git@github.com:CircleCI-Public/circleci-demo-python-flask.git`

#### Create and activate a virtual environment
For Ubuntu Linux, use `sudo apt-get install python3-venv`. 
```
$ python3 -m venv venv-name
$ source venv/bin/activate
 ```

### 2. Initialize your PostgreSQL database
`$ createdb circulate`

### 3. Install your dependencies
`$ pip install -r requirements/dev.txt`

### 4. Seed database and create tables
```
$ python manage.py deploy
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
```

### 5. Run Circulate's server and deploy locally.
`python manage.py runserver`

Next, we'll show you how to test the app locally with the Flask development server.

## Testing

The Circulate demo app runs various tests using the command:
`python manage.py test` 

### Unit Tests

Unit testing was applied to:
- database models (using [unittest](https://docs.python.org/3.7/library/unittest.html))
- client view functions (using [Flask Test Client](http://flask.pocoo.org/docs/1.0/testing/))
- API (using [Flask Test Client](http://flask.pocoo.org/docs/1.0/testing/))

### Integration Tests

Integration testing is completed for logging in, etc, using [Selenium](https://www.seleniumhq.org/) and [ChromeDriver](http://chromedriver.chromium.org/).

### Test Report Formatting

It uses [unittest-xml-reporting](https://github.com/xmlrunner/unittest-xml-reporting) for JUNIT style report generation.

## TODO

- add [parallelization](https://circleci.com/docs/2.0/parallelism-faster-jobs/)
- test with multiple python versions (3.6.2 and 3.7.1 currently tested)
- run with coverage on CircleCI
- make email testing work on CircleCI with mailhog
- make email work on the deployed Heroku app
- fill out test details: See the `tests` directory for details.

---
