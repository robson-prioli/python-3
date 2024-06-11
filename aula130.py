class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.username = None
        self.password = None 
        self.connected = False

    def set_username(self, username):
        self.username = username
    
    def set_password(self, password):
        self.password = password
    
    @classmethod
    def create_with_auth(cls, username, password):
        connection = cls()
        connection.username = username
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('log message.')


c1 = Connection.create_with_auth('Robson', '12345')

