I used JetBrains PyCharm Professional (you can get it free through the school!

First create new project with Flask in Pycharm
![image](https://user-images.githubusercontent.com/25357294/31461087-03590d52-ae8e-11e7-8973-638e25ffd401.png)

It's nice enough that it autocreates the static and template folders
![image](https://user-images.githubusercontent.com/25357294/31461205-6a715e86-ae8e-11e7-86db-11a524ca0099.png)

Then used instructions from https://www.jetbrains.com/help/datagrip/connecting-to-a-database.html to connect to a database

In Pycharm right click the project name and got to "New" then "Data Source"
![image](https://user-images.githubusercontent.com/25357294/31461259-a13b6f4c-ae8e-11e7-8f52-ec1091067d76.png)

Set the drive to Sqlite (Xerial). Leave the Path empty and press OK
![image](https://user-images.githubusercontent.com/25357294/31461306-c3ecaeac-ae8e-11e7-9142-caa31d17d9f1.png)

Enter in whatever you would like your database name to be in the "File" section. I named mine mynewdb.sqlite.
Make sure to "Test Connection". Press "Apply" and then OK
![image](https://user-images.githubusercontent.com/25357294/31461379-f960319e-ae8e-11e7-8d39-98604ce4f85f.png)

Now you can enter in database information and use it to setup the code
Used https://www.tutorialspoint.com/flask/flask_sqlite.htm to help with set up
