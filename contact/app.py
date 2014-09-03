
from contact import make_app
from contact.database import init_db


def get_app(environment='dev'):
    app = make_app(environment)
    from contact.views import reg_views
    init_db(app)
    reg_views(app)
    return app

