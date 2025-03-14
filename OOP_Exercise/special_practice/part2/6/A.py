# 6. Singleton Pattern (Relevance for ML):

# A. Implement the Singleton pattern to ensure only one instance of a class like DatabaseConnection is created.

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            print('creating a database connection.')
            cls._instance = super().__new__(cls)
        else:
            print('using the exiting database conncetion')

        return cls._instance
    
    def connect(self):
        print('connected to the ml database')


db1 = DatabaseConnection()
db1.connect()

db2 = DatabaseConnection()
db2.connect()