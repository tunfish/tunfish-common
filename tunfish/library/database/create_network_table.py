from tunfish.library.model import Network


def create_network_table(engine):
    Network.__table__.create(bind=engine, checkfirst=True)
