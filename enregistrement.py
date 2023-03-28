import sqlite3

def create_table():
    # Connect to the database
    conn = sqlite3.connect('budget.db')

    # Create a table to store the budget data
    conn.execute('''CREATE TABLE IF NOT EXISTS budget
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     date TEXT,
                     budget REAL,
                     expenses REAL,
                     total REAL,
                     difference REAL)''')

    # Close the database connection
    conn.close()

def save_data(date, budget, expenses, total, difference):
    # Connect to the database
    conn = sqlite3.connect('budget.db')

    # Insert the new data into the budget table
    conn.execute('INSERT INTO budget (date, budget, expenses, total, difference) VALUES (?, ?, ?, ?, ?)',
                 (date, budget, expenses, total, difference))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

def load_data():
    # Connect to the database
    conn = sqlite3.connect('budget.db')

    # Retrieve the budget data from the database
    data = conn.execute('SELECT * FROM budget').fetchall()

    # Close the database connection
    conn.close()

    # Return the budget data as a list of dictionaries
    return [{'date': row[1], 'budget': row[2], 'expenses': row[3], 'total': row[4], 'difference': row[5]} for row in data]


from flask import Flask, g

app = Flask(__name__)

@app.route('/')
def home():
    db = get_db()
    # Do something with the database...
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

from pymongo import MongoClient

client = MongoClient('mongodb://172.93.85.70/32/')
db = client['my_database']

@app.route('/save_data')
def save_data():
    # Récupérer les données de la base de données
    data = get_data_from_database()

    # Écrire les données dans un fichier CSV
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Nom', 'Valeur'])
        for row in data:
            writer.writerow([row['nom'], row['valeur']])

    return 'Les données ont été sauvegardées avec succès dans le fichier data.csv.'