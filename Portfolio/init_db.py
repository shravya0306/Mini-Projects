import sqlite3
#SQLite is already included with Python. No setup, no server, no password.
conn = sqlite3.connect('portfolio.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

#SQLlite for EDUCATION table
cur.execute('''
CREATE TABLE IF NOT EXISTS education (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    degree TEXT,
    institute TEXT,
    graduation_info TEXT,
    score TEXT
)
''')
cur.execute("DELETE FROM education")
cur.executemany('''
INSERT INTO education (degree, institute, graduation_info, score)
VALUES (?, ?, ?, ?)
''', [
    ('Bachelor of Engineering in Computer Science',
     'RV Institute of Technology & Management, Bangalore',
     'Expected Graduation: June 2028',
     'Current SGPA: 9.5/10 (Semester 3)'),

    ('Online B.Sc in Data Science & Applications',
     'IIT Madras',
     'Enrolled: August 2025 | Foundation Level',
     'CGPA: 8'),

    ('Pre-University Course (PUC)',
     'DEEKSHA PU College, Bangalore',
     'Completed: May 2025 | Karnataka PUE Board',
     'Math: 100/100 • Overall: 95% • PCM: 97%')
])

#SQLlite for PROJECTS table
cur.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL
)
""")
# # Optional: avoid duplicates if you run this multiple times
# cur.execute("DELETE FROM projects")
cur.execute("DELETE FROM projects")
cur.executemany('''
INSERT INTO projects (name, description)
VALUES (?, ?)
''', [
    (
        "Personal Portfolio Website (Flask + Bootstrap)",
        "A fully responsive multi-page portfolio website built using Flask, Bootstrap 5, and modular Jinja templates. Includes dedicated pages for Education, Skills, Projects, and Contact, with clean navigation and reusable layouts."
    ),
    (
        "Student Attendance Tracker (Python)",
        "A simple attendance-tracking tool built using Python, CSV storage, and a command-line interface. Allows adding students, marking attendance, and generating daily/overall attendance reports."
    )
])

#SQLlite for CONTACT table
cur.execute("""
CREATE TABLE IF NOT EXISTS contact (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT
)
""")

cur.execute("""
INSERT OR REPLACE INTO contact (id, name, email, phone, address)
VALUES (1, ?, ?, ?, ?)
""", (
    "Shravya H Somayaji",
    "somayajishravya@gmail.com",
    "+91 8217566721",
    "JP Nagar, Bengaluru, Karnataka, India"
))

#SQLlite for CERTIFICATIONS table      
cur.execute('''
CREATE TABLE IF NOT EXISTS certifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course TEXT,
    MOOC TEXT,
    date TEXT
)
''')

cur.execute("DELETE FROM certifications")

cur.executemany("""
INSERT INTO certifications (course, MOOC, date)
VALUES (?,?,?)
""", [
    (
        "AWS Certified Cloud Practitioner",
        "Amazon Web Services",
        "Issued March 2024"
    ),
    (
        "Google IT Automation with Python Professional Certificate",
        "Coursera",
        "Issued August 2025"
    ),
    (
        " Meta Front-End Developer Professional Certificate",
        "Udemy",
        "Issued December 2025"
    )
])




conn.commit()
conn.close()

print("Database created and data inserted!")