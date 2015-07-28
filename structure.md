## File Structure ##

├── app/                # Anything connected to the webapp
│   ├── __init__.py     # Core application logic
│   ├── routes/         # Routing
│   │   └── __init__.py # Empty file
│   ├── static/         # Static content
│   │   ├── css/        # CSS stylesheets
│   │   ├── img/        # Images
│   │   └── js/         # JavaScript files
│   └── templates/      # HTML pages
└── run.py              # The boot script

Using VirtualEnv

sudo apt-get install python-virtualenv
virtualenv .
source bin/activate
(blask)$ pip install flask

Freeze depencies:
pip freeze > requirements.txt

install dependencies: pip install -r requirements.txt

every folder needs an init pi in it

Blask
=====

A blog in Flask.

## Running Blask

```
mongod &
virtualenv .
source bin/activate
pip install -r requirements.txt
python reset_db.py         # Optional: wipe the databse
python run.py
```