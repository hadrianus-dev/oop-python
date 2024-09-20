class DatabaseConnection:
    def __init__(self) -> None:
        self.connection = None

    def connect(self) -> None:
        self.connection = True


class DatabaseRepository:
    def __init__(self, conection: DatabaseConnection) -> None:
        self.__connection = conection

    def read_data(self) -> list:
        if self.__connection.connect:
            return [1, 2, 3, 4]
        return None
    
class UseCase:
    def __init__(self, repository: DatabaseRepository) -> None:
        self.__repository = repository

    def calculate(self) -> list:
        data = self.__repository.read_data()
        if not data:
            print('No data found')
        else:
            response = 0
            for d in data: 
                response += d
            print(f'Result is: {response}')

conn = DatabaseConnection()
conn.connect()

repository = DatabaseRepository(conn)
usecase = UseCase(repository)

usecase.calculate()

