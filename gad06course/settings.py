DB_HOST = "localhost"
DB_NAME = "new_db"
DB_USER = "root"
DB_PASS = "!RootRoot"
DB_PORT = 3306
DB_CONNECTION = "mysql+mysqldb://%s:%s@%s:%s/%s" % (
    DB_USER,
    DB_PASS,
    DB_HOST,
    DB_PORT,
    DB_NAME,
)
