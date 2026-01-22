from flask import Flask,render_template,request,jsonify  #imports the Flask class from the flask module
from flask_sqlalchemy import SQLAlchemy  #imports the SQLAlchemy class from the flask_sqlalchemy module
from flask_cors import CORS  #imports the CORS class from the flask_cors module

app=Flask(__name__)  #Creates instance of the Flask class
                     #__name__ is a special variable that represents the name of the module

CORS(app)  #Enables Cross-Origin Resource Sharing (CORS) for the Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:password@localhost/contactsdb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/contactsdb'  #Configures the database URI for SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #Disables modification tracking to save resources

db = SQLAlchemy(app)  #Creates an instance of SQLAlchemy with the Flask app

class Contact(db.Model):  #Defines a model class named Contact that inherits from db.Model
    id = db.Column(db.Integer, primary_key=True)  #Defines an integer column 'id' as the primary key
    name = db.Column(db.String(100), nullable=False)  #Defines a string column 'name' with max length 100
    email = db.Column(db.String(100), nullable=False)  #here nullable false means this field cannot be empty
    message = db.Column(db.Text, nullable=False)  #Defines a text column 'message'

@app.before_request
def create_tables():  #Defines a function to create database tables before each request
    if not hasattr(db, 'tables_created'):  #Checks if the tables have already been created
        db.create_all()  #Creates all tables defined in the models if they don't exist
        db.tables_created = True  

@app.route('/')  #Decorator provided by Flask that defines a route for the root URL
                 #When the user accesses the root URL, the function below will be executed
def index():  #Defines a function named index
    return render_template('index.html')  #Renders the 'index.html' template


@app.route('/submit', methods=['POST'])  #Defines a route for the URL '/submit' that accepts POST requests
def submit():
    data = request.get_json()  #Gets the JSON data sent in the POST request
    name = data.get('name')  #Extracts the 'name' field from the JSON data
    email = data.get('email')  #Extracts the 'email' field from the JSON data
    message = data.get('message')  #Extracts the 'message' field from the JSON data

    new_contact = Contact(name=name, email=email, message=message)  #Creates a new Contact object with the extracted data
    db.session.add(new_contact)  #Adds the new Contact object to the database session
    db.session.commit()  #Commits the session to save the new contact to the database

    response_message=f"Thank you, {name}! Your message has been received."  #Creates a response message
    return jsonify({'message': response_message})  #Returns a JSON response with the message


if __name__ == '__main__':  #Checks if the script is being run directly (not imported as a module)      
    app.run(debug=True)  #Runs the Flask application with debug mode enabled