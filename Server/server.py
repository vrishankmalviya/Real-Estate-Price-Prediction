from flask import Flask, request, jsonify
import util
from util import price
app= Flask(__name__)

@app.before_first_request
def load_artifacts():
    util.load()


@app.route('/get_location', methods = ['GET'])
def get_location():
    
    response = jsonify({'locations': util.get_location()})
    
    response.headers.add('Access-Control-Allow-Origin','*') 
    
    return response        


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    
    total_sqft = int(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    balcony = int(request.form['balcony'])

    response = jsonify({
        'price': price(location, total_sqft, bath, bhk, balcony)
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response




if __name__=="__main__":
    print("Starting Python Flask server For Home Price Prediction")
    util.load()
    app.run(port=8000)