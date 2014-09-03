#!flask/bin/python

from contact.app import get_app
app = get_app()

app.run(debug=True)
