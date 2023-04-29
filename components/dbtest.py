from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.orm import sessionmaker, declarative_base
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel

# Create a SQLAlchemy engine to connect to a database
engine = create_engine('sqlite:///example.db', echo=True)
database = QSqlDatabase.addDatabase('QSQLITE')
database.setDatabaseName('example.db')
if not database.open():
    print(database.lastError().text())
    

# Create a declarative base class
Base = declarative_base()

# Define a SQLAlchemy model class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create the database schema
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a PySide6 application
app = QApplication([])

# Create a main window
window = QMainWindow()
window.setWindowTitle('Users')

# Create a table view
table_view = QTableView(window)
table_view.setSortingEnabled(True)
table_view.setSelectionBehavior(QTableView.SelectRows)
table_view.setSelectionMode(QTableView.SingleSelection)
table_view.setEditTriggers(QTableView.NoEditTriggers)

# Create a query model
query_model = QSqlQueryModel(window)
query_model.setQuery('SELECT * FROM users', QSqlDatabase.addDatabase('QSQLITE'))

# Set the query model on the table view
table_view.setModel(query_model)

# Populate the database with some test data
session = Session()
session.add_all([
    User(name='Alice', age=25),
    User(name='Bob', age=30),
    User(name='Charlie', age=35),
    User(name='Dave', age=40),
])
session.commit()

# Refresh the query model to show the test data in the table view
query_model.setQuery('SELECT * FROM users', QSqlDatabase.addDatabase('QSQLITE'))

# Add the table view to the main window
window.setCentralWidget(table_view)
window.resize(400, 300)
window.show()

# Run the PySide6 event loop
app.exec()