from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/budget_app"
mongo = PyMongo(app)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/budgets", methods=["GET", "POST"])
def budget():
    if request.method == "GET":
        budgets = list(mongo.db.budget.find())
        for budget in budgets:
            budget["_id"] = str(budget["_id"])
        return render_template('budget.html', budgets=budgets)
    elif request.method == "POST":
        data = request.get_json()
        result = mongo.db.budget.insert_one(data)
        return jsonify({"inserted_id": str(result.inserted_id)})
  
if __name__ == "__main__":
    app.run(debug=True)



