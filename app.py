from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/budget', methods=['POST'])
def budget():
    budget = request.form['budget']
    expenses = []
    total_expenses = 0
    expense_names = request.form.getlist('expense_name')
    expense_amounts = request.form.getlist('expense_amount')
    for i in range(len(expense_names)):
        name = expense_names[i]
        amount = float(expense_amounts[i])
        expense = Expense(name, amount)
        expenses.append(expense)
        total_expenses += amount
    return render_template('expenses.html', budget=budget, expenses=expenses, total_expenses=total_expenses)


class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


if __name__ == '__main__':
    app.run()
