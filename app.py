from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://thomscustom:<Neele21122009>@cluster0.b3iilpr.mongodb.net/?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/')
def home():
    budget = mongo.db.budget.find_one()
    expenses = mongo.db.expenses.find()
    total_expenses = sum([expense['amount'] for expense in expenses])
    remaining_budget = budget['amount'] - total_expenses
    return render_template('home.html', budget=budget['amount'], expenses=expenses, total_expenses=total_expenses, remaining_budget=remaining_budget)

@app.route('/budget', methods=['POST'])
def save_budget():
    budget = request.form['budget']
    mongo.db.budget.update_one({}, {'$set': {'amount': int(budget)}}, upsert=True)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

