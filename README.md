# Airport
From the django admin application we have the possibility to add flights by their origin and destination cities as well as the duration. 
The database used is SQLite to store and manipulate the data, and that could be done through the admin's friendly interface.
The index page renders all the flights stored in the database.
There are two tables in this project the first is the flight table linked to the airport table via foreign keys.

## To use this application effectively :
1. Don't forget to make and run migrations 
2. Add the flights application to the main project 
3. Finally you should create a super user by the manage.py appropriate command. 
