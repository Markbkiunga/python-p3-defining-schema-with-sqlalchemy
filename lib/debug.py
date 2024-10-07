#!/usr/bin/env python3

from sqlalchemy import create_engine

from sqlalchemy_sandbox import Base, Student


if __name__ == "__main__":
    engine = create_engine("sqlite:///students.db")
    Base.metadata.create_all(engine)
