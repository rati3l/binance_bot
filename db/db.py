from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql.expression import func
from .models import Base, Next_Operation, Score


class DB:
    def __init__(self, database_path, echo=False):
        self.engine = create_engine(f'sqlite:///{database_path}', echo=echo)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        Base.metadata.create_all(self.engine)
    
    def session_insert(self, row):
        session = self.Session()
        session.add(row)
        session.commit()
        session.close()
    
    def get_last(self, table):
        session = self.Session()
        try:
            ret_val = session.query(table.value).filter(table.id == session.query(func.max(table.id))).first()[0]
        
        # type error will happen at first run on fresh database
        except TypeError:
            ret_val = None

        session.close()
        return ret_val

    def push_next_operation(self, value):
        operation = Next_Operation(value=value)
        self.session_insert(operation)

    def get_next_operation(self):
        return self.get_last(Next_Operation)
    
    def push_score(self, score):
        operation = Score(value=score)
        self.session_insert(operation)

    def get_score(self):
        return self.get_last(Score)
    