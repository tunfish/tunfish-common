# create_gw_table.py
from tunfish.library.model import Gateway


def create_gw_table(engine):
    Gateway.__table__.create(bind=engine, checkfirst=True)
