from os import path

from flask import Flask


file_dir = path.dirname(path.dirname(__file__))
template_path = [file_dir, 'templates']

app = Flask(
    __name__,
    static_folder=path.join(file_dir, 'static'),
    static_url_path='/static',
    template_folder=path.join(*template_path)
)

app.secret_key = 'why would I tell you my secret key?'


from app import views
