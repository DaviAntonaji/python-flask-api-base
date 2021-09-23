#### Hello, this project is a base for developing APIS using Python with FLASK library connected to a MySQL database. 😁
------------
##### 👨🏻‍💻 About the project
###### The project is a base for the development of an API in Python, with the main functions of an API, with a route that needs JWT authentication, and a login that generates a JWT token

- 🤔 The models folder was made for SQLs operations and object returns
- 💻 The resources folder is where the requests and responses routes and logic are, where the defs represent the request method (GET, POST, PUT and DELETE), usually being GET for queries, POST for registrations, PUT for updates and DELETE for deleting
- 🤔  The functions folder was made to use functions created externally, for example a calculation used in several models and resources
- 💻   The tokenpass folder has encryption functions and the JWT tokens part
------------
##### Installation

- Python installation is required (Yes, really, you're not looking for a Python API without having python installed, are you?)
- Python min version: 3.8.0
- Enter the project folder in a terminal and run the command 
```
pip3 install -r requirements.txt
```
- Run the following command to start the application
```
python3 app.py

# If you are using a linux machine use an "&" at the end of the command, this will make it run in the background
```
------------

##### Comments

- ###### Environment variables are in the .env file. It is in this file that you put the database access credentials, and other constants that are changed from development, to testing and to production

