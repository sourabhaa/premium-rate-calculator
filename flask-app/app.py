from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')

db = client['PremiumRatesDB']

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/premium-rates', method=['GET'])
def data():
    allData = db['Rates'].find()
    dataj = []
    for data in allData:
      SumInsured = data['SumInsured']
    print(SumInsured)
      
    # rateDetails = db['rates'].find_one(SumInsured={sum-insured}, TierID={city-tier}, Tenure={tenure}  )




if __name__ == '__main__':
    app.debug = True
    app.run()