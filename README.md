# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Trello

The ToDo app requires a board from a Trello account to sync with for storage.

The `.env` file should contain the following environment variables:

TRELLO_KEY='<key>'
TRELLO_TOKEN='<token>'
TRELLO_BOARD_ID='<board_id>'

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Testing the app

To run the unit tests from the todo_app directory run the following command:
```bash
$ pytest test_ViewModel.py
```

You should see output similar to the following:
```bash
============================= test session starts =================================================================
platform darwin -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: /Users/paulhutchinson/Dev/Corndel/Course/project/DevOps-Course-Starter/todo_app
collected 7 items               
test_ViewModel.py .......       
[100%]
============================== 7 passed in 0.18s ==================================================================
```

To run an individual unit test specify <test_module>::<test_name> as follows:
```bash
$ pytest test_ViewModel.py::test_todo_items
```

## End to End testing

To run the end to end test the following are required:
- Firefox browser
- Geckodriver
- Add location of Geckodriver to Path or set in test_e2e.py

- In VSCode open TestExplorer
- In test_e2e.py run test_task_journey
- Results shown in Debug Console should look like below:

============================= test session starts ==============================
platform darwin -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: /Users/paulhutchinson/Dev/Corndel/Course/ex2/DevOps-Course-Starter
collected 1 item
==DISCOVERED TESTS BEGIN==
{"tests": [{"id": "todo_app/e2etests/test_e2e.py::test_task_journey", "line": 55}], "errors": []}
==DISCOVERED TESTS END==

todo_app/e2etests/test_e2e.py .                                          [100%]

============================== 1 passed in 19.33s ==============================

### Build and Run docker image

The application can be built in development mode which will run with flask with debug functionality.
When the application is built in production mode it will run with gunicorn.

To build and run for development:
```
docker build --target development --tag todo-app:dev .
docker run --env-file ./.env -p 80:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev
```

To build and run for production: 
```
docker build --target production --tag todo-app:prod .
docker run -p 5000:5000 todo-app:prod
```