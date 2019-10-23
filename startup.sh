#!bin/bash
export FLASK_APP=run.py
export FLASK_ENV=production
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000
export FLASK_RUN_CERT=cert.pem
export FLASK_RUN_KEY=key.pem
pip3 install flask-sqlalchemy
pip3 install flask-bcrypt
pip3 install flask-login
pip3 install flask-wtf
pip3 install wtforms-sqlalchemy