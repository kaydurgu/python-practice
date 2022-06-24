class DataBase:
    __instance = None
    def __new__(cls, *args, **kwargs)->object:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, name, port) -> None:
        self.name = name
        self.surname = port
        
db = DataBase('MySql', '8088')
db2 = DataBase('Sqlite', '8080')

print (db, db2) #ссылыка на один и тот же объект
