from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine('sqlite:///user_data.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    controller = Column(Integer)

    boiler_temp = relationship("BoilerTemp", backref="user")
    buffer_temp = relationship("BufferTemp", backref="user")
    mfb_temp = relationship("MFBTemp", backref="user")


class BoilerTemp(Base):
    __tablename__ = 'boiler_temp'

    id = Column(Integer, primary_key=True)
    controller_id = Column(Integer, ForeignKey('users.controller'))
    value = Column(Integer)
    time_stamp = Column(TIMESTAMP(timezone=False), nullable=False)


class BufferTemp(Base):
    __tablename__ = 'buffer_temp'

    id = Column(Integer, primary_key=True)
    controller_id = Column(Integer, ForeignKey('users.controller'))
    value = Column(Integer)
    time_stamp = Column(TIMESTAMP(timezone=False), nullable=False)


class MFBTemp(Base):
    __tablename__ = 'mfb_temp'

    id = Column(Integer, primary_key=True)
    controller_id = Column(Integer, ForeignKey('users.controller'))
    value = Column(Integer)
    time_stamp = Column(TIMESTAMP(timezone=False), nullable=False)


Base.metadata.create_all(engine)

user_1 = User(email="user@email.com", password="pass", controller=1)
user_1.boiler_temp = [BoilerTemp(value=50, time_stamp=datetime.now()), BoilerTemp(value=50, time_stamp=datetime.now())]
user_1.buffer_temp = [BufferTemp(value=40, time_stamp=datetime.now()), BufferTemp(value=40, time_stamp=datetime.now())]
user_1.mfb_temp = [MFBTemp(value=90, time_stamp=datetime.now()), MFBTemp(value=90, time_stamp=datetime.now())]


session.add(user_1)
session.commit()

for u, d in session.query(User, BoilerTemp).filter(User.controller == BoilerTemp.controller_id).all():
    print(f"User email: {u.email} Controller ID: {u.controller} Value: {d.value} Timestamp: {d.time_stamp}")

for u, d in session.query(User, BufferTemp).filter(User.controller == BufferTemp.controller_id).all():
    print(f"User email: {u.email} Controller ID: {u.controller} Value: {d.value} Timestamp: {d.time_stamp}")

for u, d in session.query(User, MFBTemp).filter(User.controller == MFBTemp.controller_id).all():
    print(f"User email: {u.email} Controller ID: {u.controller} Value: {d.value} Timestamp: {d.time_stamp}")
    print(d.user.email)

