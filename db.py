
class DatabaseSettings:

    @staticmethod
    def get_db():
        user = "admin_desafio"
        password = "$#@!desafio"
        host = "localhost"
        database = "DesafioCrudDB"
        return "mysql+pymysql://{}:{}@{}/{}".format(user, password, host, database)
