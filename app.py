from flask import Flask, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'zxc'
app.config['MYSQL_DB'] = 'mydb'
mysql=MySQL(app)
@app.route('/')
def hello():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
    cursor.execute("SELECT title,description,url FROM mytable ORDER BY RAND() LIMIT 1") 
    result = cursor.fetchone()   
    print(result['description']) 
    if (result['description']=='[removed]' or result['description']=='[deleted]'):
        result["description"]='' 

    return render_template("onepager.html", result = result)

if __name__ == '__main__':
    app.run()