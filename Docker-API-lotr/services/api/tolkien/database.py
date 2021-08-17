from pymongo.errors import ConnectionFailure


class Database:
    db_types = ['mongo', 'mysql']
    host = None
    port = None
    db_name = None
    db_type = None

    def __init__(self, db_data):
        self.load_data(db_data)
        if not self.is_valid_type():
            raise NameError(
                f'{db_data.get("db_type", "-")} is not available in our configuration: '
                f'{self.db_types}'
            )

    def is_valid_type(self):
        return True if self.db_type in self.db_types else False

    def get_database(self):
        if self.db_type == 'mongo':
            from pymongo import MongoClient
            client = MongoClient(host=self.host, port=self.port)
            return client[self.db_name]
        if self.db_type == 'mysql':
            raise NameError('MYSQL connection not implemented')

    def load_data(self, db_data):
        self.host = db_data['host']
        self.port = db_data['port']
        self.db_name = db_data['db_name']
        self.db_type = db_data['db_type']

    def get_connection(self, app):
        connection = None
        try:
            connection = self.get_database()
        except ConnectionFailure:
            err_msg = "Server not available"
            app.logger.info(err_msg)
        return connection
