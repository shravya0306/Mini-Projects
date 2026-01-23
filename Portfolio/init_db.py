import sqlite3
#SQLite is already included with Python. No setup, no server, no password.
conn = sqlite3.connect('portfolio.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS education (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    degree TEXT,
    institute TEXT,
    graduation_info TEXT,
    score TEXT
)
''')

# education_data =
# [
#   <sqlite3.Row>,
#   <sqlite3.Row>,
#   <sqlite3.Row>
# ]

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

cur.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL
)
""")

# Optional: avoid duplicates if you run this multiple times
cur.execute("DELETE FROM projects")

cur.executemany("""
INSERT INTO projects (title, description)
VALUES (?, ?)
""", [
    (
        "Personal Portfolio Website (Flask + Bootstrap)",
        "A fully responsive multi-page portfolio website built using Flask, Bootstrap 5, and modular Jinja templates. Includes dedicated pages for Education, Skills, Projects, and Contact, with clean navigation and reusable layouts."
    ),
    (
        "Student Attendance Tracker (Python)",
        "A simple attendance-tracking tool built using Python, CSV storage, and a command-line interface. Allows adding students, marking attendance, and generating daily/overall attendance reports."
    )
])

cur.execute("""
CREATE TABLE IF NOT EXISTS contact (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT
)
""")

# Keep exactly one row (id=1)
cur.execute("""
INSERT OR REPLACE INTO contact (id, name, email, phone, address)
VALUES (1, ?, ?, ?, ?)
""", (
    "Shravya H Somayaji",
    "somayajishravya@gmail.com",
    "+91 8217566721",
    "JP Nagar, Bengaluru, Karnataka, India"
))

conn.commit()
conn.close()

print("Database created and data inserted!")