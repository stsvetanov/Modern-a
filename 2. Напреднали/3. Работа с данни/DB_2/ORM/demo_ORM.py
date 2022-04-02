import sqlalchemy as db

engine = db.create_engine('sqlite:///people.db')
connection = engine.connect()
metadata = db.MetaData()
people = db.Table('person', metadata, autoload=True, autoload_with=engine)
# print(people.columns.keys())
#
# print(repr(metadata.tables['person']))

# # Querying
# #Equivalent to 'SELECT * FROM census'
# query = db.select([people])
#
# ResultProxy = connection.execute(query)
# ResultSet = ResultProxy.fetchall()
# print(ResultSet[:5])
#
# Filtering data
# SQL :
# SELECT * FROM people
# WHERE lname = Petrov

# SQLAlchemy :
query = db.select([people]).where(people.columns.lname == 'Petrov')
result = connection.execute(query)
resultSet = result.fetchall()
print(resultSet)