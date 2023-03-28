from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/budget_app"
mongo = PyMongo(app)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/budget", methods=["GET", "POST"])
def budgets():
    if request.method == "GET":
        budgets = list(mongo.db.budget.find())
        for budget in budgets:
            budget["_id"] = str(budget["_id"])
        return render_template('budgets.html', budgets=budgets)
    elif request.method == "POST":
        data = request.get_json()
        result = mongo.db.budget.insert_one(data)
        return jsonify({"inserted_id": str(result.inserted_id)})
  
@app.route('/budget')
def budgets():
    budgets = mongo.db.budget.find()
    return render_template('budget.html', budget=budgets)


if __name__ == "__main__":
    app.run(debug=True)



