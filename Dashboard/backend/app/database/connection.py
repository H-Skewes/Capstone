""" 
    This file will act as the connection file for
    connecting the database to the rest of the project
    this will probably take lots of trials since as of
    now we do not have an actual server to test connections.

    According to what I read we first need to have 
    python-dotenv installed and msql-connector-python.
"""

import mysql.connector
from mysql.connector import Error

db_config = {
    "host": # The database will be hosted on an Azure server
    "user": # The user will be admin or something else
    "password": # Not sure what the password would be or how it would fit in with our project?
    "database": "Full_DB.db" # Not sure if the .db is needed
}

""" Below we are trying to establish a connection to the database
    and we want it to stay connected. If the database does not 
    connect we want to know that so it will show an error and tell us."""


def create_database_connection():
    try:
        with mysql.connector.connect(**db_config) as connection:
            if connection.is_connected():
                print ("Connected to Full_DB")
            else:
                except Error as e:
                    print(f"\n Connection to Full_DB failed: {e}")

if __name__ == "__main__":
    create_database_connection()
                    
            


