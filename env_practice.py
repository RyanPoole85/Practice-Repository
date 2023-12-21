host = ''
user = ''
password = ''
#def get_db_url(user, password, host, 
def get_db_url(db, user=user, password=password, host=host):
    return (f'mysql+pymysql://{user}:{password}@{host}/{
