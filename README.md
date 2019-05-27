A quick and simple example of a REST API built with python.
# Build Instructions
## Requires
* setuptools
* wheel
## Instructions
`python setup.py bdist_wheel`
## Usage
This applicaiton is kicked off by running app.py. To run
behind a wsgi service supply wsgi.py example:
`gunicorn wsgi:app`
