# create_router_table.py
from tunfish.library.model import Router


def create_router_table(engine):
    Router.__table__.create(bind=engine, checkfirst=True)
