from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password1234'
app.config['MYSQL_DB'] = 'STUDENTBOOK'
app.config['MYSQL_HOST'] = '146.148.119.225'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM STUDENTS''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

@app.route("/add")
def addNew():
	cur = mysql.connect.cursor()
	cur.execute('''INSERT INTO STUDENTS (studentName, email) values ("second student", "secondstudent@mydit.ie ")''')
	return 'new student added'

@app.route("/update")
def updateRecord():
	return 'updated student'

@app.route("/delete")
def deleteRecord():
	return 'record deleted'


if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000
