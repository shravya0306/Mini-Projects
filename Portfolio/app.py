from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('portfolio.db')
    conn.row_factory = sqlite3.Row  # allows dict-style access //Each row is of type  sqlite3.Row
    return conn

@app.route('/')
def home():
        return render_template('index.html')


@app.route('/education')
def education():
    conn = get_db_connection()
    education_data = conn.execute(
        'SELECT degree, institute, graduation_info, score FROM education'
    ).fetchall()
    conn.close()

    return render_template('education.html', education=education_data)
    #return render_template('education.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/Contact')
def contact():
    return render_template('ContactMe.html')

if __name__ == '__main__':
    app.run(debug=True)