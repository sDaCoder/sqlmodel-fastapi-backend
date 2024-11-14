from sqlmodel import SQLModel, create_engine

def connect(conn_url: str):
    engine = create_engine(conn_url)
    SQLModel.metadata.create_all(engine)
    print("Connected to the database")
    return engine