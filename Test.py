import sql as sql
from flask import Flask, render_template, request
import os
import sqlite3


#create an SQLite database
conn = sqlite3.connect("mynewdb.sqlite")
print ("Opened database successfully")
#closes database
conn.close()


#creates the application instance
app = Flask(__name__)


#Inital login form (user.html) that asks for username and password
@app.route('/')
def home():
    return render_template("User.html")


#Form data is posted to the '/login' URL which binds to the
#Login() function. When user presses submit. Code is run
@app.route('/login',methods = ['GET', 'POST'])
def login():
    #Post grabs from html file?
    if request.method == 'POST':

        #try to get username and password and add to
        #database
        try:
            username = request.form['username']
            pw = request.form['pw']

            #connect to database and save as con
            with sql.connect("mynewdb.sqlite") as con:

                #Connect database (con) to cursor. Use bound database to cursor
                #to fetch results

                c = con.cursor()

                #Excute SQLite commands could also create schema for this
                c.execute ("INSERT INTO users (userName,password)"
                             "VALUES (?,?)",(username,pw) )

                #Commit database information
                con.commit()
                msg =("successfully added")


        #If unable to add to database. Rollback database
        except:
            con.rollback()
            msg = ("unable to copy")

        #Use results html to displays message to inform user if the
        #username has been added to the database or not
        finally:
            return render_template("results.html", msg=msg)
            #close database
            con.close()


#Main run
if __name__ == '__main__':
    app.run()
