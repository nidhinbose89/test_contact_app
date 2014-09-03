from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def init_db(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=True,
                                             bind=engine))
    app.config['DATABASE_ENGINE'] = engine
    app.config['DATABASE'] = db_session
    Base.query = db_session.query_property()
    db_session.commit()
    # import all modules here that might define models so that they will be registered properly on the metadata.
    # Otherwise  you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)

    @app.teardown_request
    def teardown_request(exception):
        # happens at the end of the request
        app.config['DATABASE'].rollback()


def drop_all_tables(app):
    app.config['DATABASE'].close()
    app.config['DATABASE'].remove()
    Base.metadata.drop_all(bind=app.config['DATABASE_ENGINE'])
