from sqlalchemy import create_engine, ForeignKey, Column, Integer, String

engine = create_engine('sqlite:///sales.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy.orm import relationship, sessionmaker

Session = sessionmaker(bind = engine)
session = Session()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    custid = Column(Integer, ForeignKey('customers.id'))
    invno = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customer", back_populates="invoices")


class Deposit(Base):
    __tablename__ = 'deposits'

    id = Column(Integer, primary_key=True)
    custid = Column(Integer, ForeignKey('customers.id'))
    invno = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customer", back_populates="deposits")


Customer.invoices = relationship("Invoice", order_by=Invoice.id, back_populates="customer")
Customer.deposits = relationship("Deposit", order_by=Deposit.id, back_populates="customer")
Base.metadata.create_all(engine)

c1 = Customer(name = "Gopal Krishna", address = "Bank Street Hydarebad", email = "gk@gmail.com")
c1.invoices = [Invoice(invno = 10, amount = 15000), Invoice(invno = 14, amount = 3850)]
c1.deposits = [Deposit(invno = 10, amount = 15000), Deposit(invno = 14, amount = 3850)]

session.add(c1)
session.commit()

for c, i in session.query(Customer, Invoice).filter(Customer.id == Invoice.custid).all():
   print("ID: {} Name: {} Invoice No: {} Amount: {}".format(c.id,c.name, i.invno, i.amount))

for c, i in session.query(Customer, Deposit).filter(Customer.id == Deposit.custid).all():
   print("ID: {} Name: {} Invoice No: {} Amount: {}".format(c.id,c.name, i.invno, i.amount))