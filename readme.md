installation:
pip install -r requirements.txt

to host:
use wsgi like gunicorn
`pip install gunicorn`
`gunicorn -w {num workers} --chdir {path to app} wsgi:app`
