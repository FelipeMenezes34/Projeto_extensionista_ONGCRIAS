# O Django precisa de um conector para conversar com o MySQL.
# Usamos o PyMySQL porque instala fácil no Windows.
import pymysql

pymysql.version_info = (2, 2, 1, "final", 0)
pymysql.install_as_MySQLdb()
