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

conn.commit()
conn.close()

print("Database created and data inserted!")