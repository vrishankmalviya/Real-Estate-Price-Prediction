from flask import Flask, request, jsonify
app= Flask(__name__)

@app.route('/hello')
def get_location():
    
    response = jsonify({'locations':util.get_location()})
    
    response.headers.add('Access-Control-Allow-Origin','*') 
    
    return response        
    return "hii"



if __name__=="__main__":
    print("Starting Python Flask server For Home Price Prediction")
    app.run(port=8000)