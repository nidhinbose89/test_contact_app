from os import path

from flask import Flask


def make_app(environment):
    file_dir = path.dirname(path.dirname(__file__))
    template_path = [file_dir, 'templates']

    app = Flask(
        __name__,
        static_folder=path.join(file_dir, 'static'),
        static_url_path='/static',
        template_folder=path.join(*template_path)
    )
    if environment == 'dev':
        app.config.update(dict(
            SQLALCHEMY_DATABASE_URI='mysql://root:<password>@localhost:<port_no_eg_3232>/<database_name>?charset=utf8',
            DEBUG=True,
            SECRET_KEY='some key for your application',
            TESTING=False
        )
        )
    else:
        app.config.update(dict(
            SQLALCHEMY_DATABASE_URI='mysql://root:<password>@localhost:<port_no_eg_3232>/<test_database_name>?charset=utf8',
            SECRET_KEY='some key for your application',
            TESTING=True
        )
        )
    return app
