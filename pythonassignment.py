import pymysql
users = pymysql.connect(host="localhost",user="utkarsh",passwd="pass",database="users")
def userexists(username):
    cursor = users.cursor()
    query = "SELECT * from users where username = '%s'" % (username,)
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result)==1:
        return True
    else:
        raise Exception('username not in database')

    

