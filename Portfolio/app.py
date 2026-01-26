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

@app.route('/skills')
def skills():
        return render_template('skills.html')


@app.route('/education')
def education():
    conn = get_db_connection()
    education_data = conn.execute(
        'SELECT degree, institute, graduation_info, score FROM education'
    ).fetchall()
    conn.close()

    return render_template('education.html', education=education_data)
    


@app.route('/projects')
def projects():
    conn = get_db_connection()
    project_data = conn.execute(
        'SELECT name, technology, description FROM projects'
    ).fetchall()
    conn.close()

    return render_template('projects.html', projects=project_data)

@app.route('/certifications')
def certifications():
    conn = get_db_connection()
    certs = conn.execute('SELECT course, MOOC, date FROM certifications').fetchall()
    conn.close()

    certs = list(certs)
    mid = (len(certs) + 1) // 2   # left column gets the extra one when odd

    left = certs[:mid]
    right = certs[mid:]

    return render_template('certifications.html', left=left, right=right)


@app.route('/contact')
def contact():
    conn = get_db_connection()
    contact_data = conn.execute(
        'SELECT name, email, phone, address FROM contact WHERE id = 1'
    ).fetchone()
    conn.close()

    return render_template('ContactMe.html', contact=contact_data)


if __name__ == '__main__':
    app.run(debug=True)