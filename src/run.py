from src.app import app

__author__ = 'Lucas Yum'

app.run(debug=app.config['DEBUG'], port=4990)
