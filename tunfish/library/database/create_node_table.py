# create_node_table.py
from tunfish.library.model import WireGuardNode


def create_node_table(engine):
    WireGuardNode.__table__.create(bind=engine, checkfirst=True)
