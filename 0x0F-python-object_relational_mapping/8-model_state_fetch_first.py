#!/usr/bin/python3
""" script that lists all states form the data base hbtn_0e_0_usa"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    host = 'localhost'
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(user, passwd, host, db))

    Sess = sessionmaker(bind=engine)
    session = Sess()

    result = session.query(State).order_by(State.id).first()

    if result is None:
        print("Nothing")
    else:
        print(f"{result.id}: {result.name}")
