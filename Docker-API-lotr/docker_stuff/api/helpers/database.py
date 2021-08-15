class Database:
    db_types = ['mongo', 'mysql']
    host = None
    port = None
    db_name = None
    db_type = None

    def __init__(self, host, port, db, db_type):
        self.host = host
        self.port = port
        self.db_name = db
        self.db_type = db_type.lower()
        if not self.is_valid_type():
            raise NameError(
                f'{db_type} is not available in our configuration: {self.db_types}'
            )

    def is_valid_type(self):
        return True if self.db_type in self.db_types else False

    def connection(self):
        if self.db_type == 'mongo':
            from pymongo import MongoClient
            client = MongoClient(host=self.host, port=self.port)
            return client[self.db_name]
        if self.db_type == 'mysql':
            raise NameError('MYSQL connection not implemented')
