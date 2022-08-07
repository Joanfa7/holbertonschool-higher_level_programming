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
    find_name = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(user, passwd, host, db))

    Sess = sessionmaker(bind=engine)
    session = Sess()

    result = session.query(State).filter_by(name=find_name).first()

    if result is not None:
        print(f"{result.id}")
    else:
        print("Not found")
