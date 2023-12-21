host = 'data.codeup.com'
user = 'ursula_2328'
password = 'ZEsOi3USk9qClmhKK80EWvX6pZaO4rTk'
#def get_db_url(user, password, host, database):
#   return f'mysql+pymysql://ursula_2328:ZEsOi3USk9qClmhKK80EWvX6pZaO4rTk@data.codeup.com/employees'
def get_db_url(db, user=user, password=password, host=host):
    return (f'mysql+pymysql://{user}:{password}@{host}/{db}')
#url = f'mysql+pymysql://ursula_2328:ZEsOi3USk9qClmhKK80EWvX6pZaO4rTk@data.codeup.com/employees'