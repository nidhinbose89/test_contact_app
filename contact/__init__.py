from app import make_app
from database import init_db


def get_app():
    app = make_app()
    from contact.views import reg_views
    init_db(app)
    reg_views(app)
    return app
