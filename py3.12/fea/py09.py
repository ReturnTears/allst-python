from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    age = Column(Integer)

engine = create_engine('sqlite:///meory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.add(User(name='yangyang',age=18))
pyista = session.query(User)\
    filter(User.age > 18)\
    filter(User.name == 'yangyang')\
    first()
    #.update({User.age:User.age+1})

print(pyista.id)

