from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import sys
sys.path.append('../DogMatch')
from BE.configuration import DB_CONNECTION

Base = declarative_base()


def createConnection() -> sessionmaker:
    engine = create_engine(DB_CONNECTION)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    return Session


def delete_row(session, variable_name, variable, row_class):
    kwargs = {variable_name: variable}
    animal_to_delete = session.query(row_class).filter_by(**kwargs).first()
    if animal_to_delete:
        session.delete(animal_to_delete)

    session.commit()


def get_table(session, table_class):
    """
    Returns all rows from the given table.
    """
    return session.query(table_class).all()


def row_exists(session, variable_name, variable, row_class):
    kwargs = {variable_name: variable}
    return session.query(row_class).filter_by(**kwargs).first() is not None


def get_foreign_key_id(session, model, token: str) -> int:
    """Helper function to get the foreign key ID from the dictionary table"""
    return session.execute(select(model.id).where(model.token == token)).scalar_one()
