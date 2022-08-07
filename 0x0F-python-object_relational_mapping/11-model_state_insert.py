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

    insert = State(name="Luisiana")
    session.add(insert)
    session.commit()

    print(f"{insert.id}")
