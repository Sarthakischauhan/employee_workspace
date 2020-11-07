import mysql.connector
from mysql.connector import Error 

try :
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="school_project"
    )
except Error as e:
    print(f"Error {e} occurred")


create_employee="""
CREATE TABLE IF NOT EXISTS employee (
    employeeID INT AUTO_INCREMENT,
    name CHAR(50) NOT NULL,
    password VARCHAR(220) NOT NULL,
    code VARCHAR(8) NOT NULL,
    dept CHAR(20) NOT NULL,
    PRIMARY KEY (employeeID)
);
"""

create_bugs="""
CREATE TABLE IF NOT EXISTS bugs (
    bugID INT AUTO_INCREMENT,
    content CHAR(255) NOT NULL,
    raised_by VARCHAR(8) NOT NULL,
    PRIMARY KEY (bugID)
);
"""


def execute_query(query,connection=connection):
    cursor=connection.cursor()
    try :
        cursor.execute(query)
        connection.commit()
        print("Query Complete")

    except Error as e :
        print(f"Error {e} occurred")


def read_data(query,connection=connection):
    cursor=connection.cursor()
    try :
        cursor.execute(query)
        results=cursor.fetchall()
        return results

    except Error as e :
        print(f"Error {e} occurred")    


def push_bugs(bug,user_code,connection=connection):
    cursor=connection.cursor()

    query=f"""
    INSERT INTO
        `bugs` (`content` , `raised_by` )
    VALUES     
        ('{bug}' , '{user_code}');
    """
    try :
        cursor.execute(query)
        connection.commit()
        print("Bug Pushed successfully")
    except Error as e:
        print(f"Error {e} occurred")



