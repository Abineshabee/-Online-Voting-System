#import Flask
from flask import Flask , render_template , request


#Generate Captcha
import Gcaptcha
global captcha_text 
#EPIC verify And MockData
import MockData

#database
import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
        host='localhost',
        database='ovs',
        user='root',
        password='Abinesh1010'
    )
if connection.is_connected():
    print('Connected to MySQL database')
else :
    print("Failed to insert record into MySQL table.")

# Creating a cursor object
cursor = connection.cursor()

# Prepare SQL query to insert a record into the database
insert_query = """INSERT INTO vote
                      ( epicno , candidate , vote )
                      VALUES (%s, %s ,%s)"""

elist = [ ]

app = Flask(__name__)


def save_captcha_to_file(captcha_text):
    with open( r"D:\.vscode\OVS\captcha.txt" , "w") as file:
        file.write(captcha_text)

def get_captcha_from_file():
    with open( r"D:\.vscode\OVS\captcha.txt" , "r") as file:
        captcha_text = file.read().strip()
    return captcha_text





@app.route('/OnlineVotingSystem')
def index( ) :
    return render_template("index.html")


@app.route('/OnlineVotingSystem/login')
def login( ) :

    captcha_text  = Gcaptcha.generate_captcha()
    save_captcha_to_file(captcha_text)
    return render_template("login.html" )

@app.route('/OnlineVotingSystem/login/vote' , methods = [ 'POST' , 'GET' ]) 
def verify( ) :

    if request.method == 'POST' :
        epicno = request.form.get('epicno')
        captch = request.form.get('captcha')
        captcha_text = get_captcha_from_file()

        print("{\n")

        print(f"Entered EPIC Number         : { epicno } ")
        print(f"Entered Captcha             : { captch } ")
        print(f"Real EPIC Number Status     : { MockData.is_valid_epic_number( epicno ) } ")
        print(f"Real Captcha Data           : { captcha_text } ")

        print("\n}")


        if( MockData.is_valid_epic_number(epicno) != True ) :
            return f"<p>{MockData.FalseE}</p>"

        if( captcha_text != captch ) :
            return f"<p>{Gcaptcha.FalseC}</p>"

        if ( MockData.is_valid_epic_number(epicno) == True ) and ( captcha_text == captch ) :

            # Execute the SELECT query to check if the epicno exists
            query = "SELECT * FROM vote WHERE epicno = %s"
            cursor.execute(query, (epicno,))
        
            # Fetch one row, if exists
            row = cursor.fetchone()
            if row:
                print(f"\n[\nEpicno '{epicno}' already exists in the database.\n]\n")
                return render_template("submited.html")
            else:
                print(f"\n[\nEpicno '{epicno}' does not exist in the database.\n]\n")


            mock_voter_details = MockData.get_mock_voter_details(epicno)

            elist.append(epicno)

            vi = mock_voter_details['voter_id']
            nm = mock_voter_details['name']
            gn = mock_voter_details['gender']
            ag = mock_voter_details['age'] 
            mo = '+91'+ mock_voter_details['mobile']
            st = mock_voter_details['state']
            ad = mock_voter_details['address']
            co = mock_voter_details['country']

            print("\n{\n")
            
            print(f"Voter ID : { vi }")
            print(f"Name     : { nm }")
            print(f"Gender   : { gn }")
            print(f"Age      : { ag }")
            print(f"Mobile   : { mo }")
            print(f"State    : { st }")
            print(f"Address  : { ad }")
            print(f"Country  : { co }")

            print("\n}\n")

    
            return render_template("vote.html", vi=vi , nm=nm , gn=gn , ag=ag , mo=mo , ad=ad )
        

@app.route('/c1', methods = [ 'POST' , 'GET' ])
def candidate1( ) :

    try :
        # Define your data
        data_to_insert = ( elist[0] , "VELUCHAMY P" , 1 )

    except :

        return render_template("submited.html")

    # Execute the SQL query
    cursor.execute(insert_query, data_to_insert)

    # Commit changes to the database
    connection.commit()
    print("\n{\n From DATABASE : Record inserted successfully.\n}\n")

    elist.clear()
    print("\n{\n elist :", elist ,"\n}\n")

    return render_template('submit.html')


@app.route('/c2', methods = [ 'POST' , 'GET' ])
def candidate2( ) :

    try :
        # Define your data
        data_to_insert = ( elist[0] , "AISHA GUPTA A" , 1 )

    except :

        return render_template("submited.html")

    # Execute the SQL query
    cursor.execute(insert_query, data_to_insert)

    # Commit changes to the database
    connection.commit()
    print("\n{\n From DATABASE : Record inserted successfully.\n}\n")

    elist.clear()
    print("\n{\n elist :", elist ,"\n}\n")

    return render_template('submit.html')
   

@app.route('/c3', methods = [ 'POST' , 'GET' ])
def candidate3( ) :

    try :
        # Define your data
        data_to_insert = ( elist[0] , "ARJUN SHARMA S" , 1 )

    except :

        return render_template("submited.html")

    # Execute the SQL query
    cursor.execute(insert_query, data_to_insert)

    # Commit changes to the database
    connection.commit()
    print("\n{\n From DATABASE : Record inserted successfully.\n}\n")

    elist.clear()
    print("\n{\n elist :", elist ,"\n}\n")

    return render_template('submit.html')


@app.route('/c4', methods = [ 'POST' , 'GET' ])
def candidate4( ) :

    try :
        # Define your data
        data_to_insert = ( elist[0] , "ANANYA SINGH A" , 1 )

    except :

        return render_template("submited.html")

    # Execute the SQL query
    cursor.execute(insert_query, data_to_insert)

    # Commit changes to the database
    connection.commit()
    print("\n{\n From DATABASE : Record inserted successfully.\n}\n")

    elist.clear()
    print("\n{\n elist :", elist ,"\n}\n")

    return render_template('submit.html')


@app.route('/c5', methods = [ 'POST' , 'GET' ])
def candidate5( ) :

    try :
        # Define your data
        data_to_insert = ( elist[0] , "ADITYA G" , 1 )

    except :

        return render_template("submited.html")

    # Execute the SQL query
    cursor.execute(insert_query, data_to_insert)

    # Commit changes to the database
    connection.commit()
    print("\n{\n From DATABASE : Record inserted successfully.\n}\n")

    elist.clear()
    print("\n{\n elist :", elist ,"\n}\n")

    return render_template('submit.html')


@app.route('/c6', methods = [ 'POST' , 'GET' ])
def candidate6( ) :

    try :
        # Define your data
        data_to_insert = ( elist[0] , "MEERA REDDY M" , 1 )

    except :

        return render_template("submited.html")

    # Execute the SQL query
    cursor.execute(insert_query, data_to_insert)

    # Commit changes to the database
    connection.commit()
    print("\n{\n From DATABASE : Record inserted successfully.\n}\n")

    elist.clear()
    print("\n{\n elist :", elist ,"\n}\n")

    return render_template('submit.html')


@app.route('/nota', methods = [ 'POST' , 'GET' ])
def nota( ) :

    try :
        # Define your data
        data_to_insert = ( elist[0] , "NOTA" , 1 )

    except :

        return render_template("submited.html")

    # Execute the SQL query
    cursor.execute(insert_query, data_to_insert)

    # Commit changes to the database
    connection.commit()
    print("\n{\n From DATABASE : Record inserted successfully.\n}\n")

    elist.clear()
    print("\n{\n elist :", elist ,"\n}\n")

    return render_template('submit.html')


if __name__ == '__main__' :

    app.run(debug=True)