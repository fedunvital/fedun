from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        raise NotImplementedError("Method must be implemented")

class MySQLDatabase(Database):
    def save(self, data):
        print("Saving to MySQL", data)

class SqlLite(Database):
    def save(self, data):
        print("Saving to SqlLite", data)

class UserService:
    def __init__(self, database):
        self.db = database

    def register(self, user):
        self.db.save(user)

# Використання
db = SqlLite()
service = UserService(db)
service.register({"name": "Vitalii"})
