import json
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request

app = Flask(_name_)
model = tf.keras.models.load_model('recommender_model')
books = pd.read_csv('dataset/books.csv')
book_id = [i+1 for i in range(10000)]
user_id = [7 for i in range(10000)]
X = [book_id, user_id]

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/predict", methods=["POST"])
def predict():

    request_json = request.json
    input = request_json.get('data')
    input = [np.array(x) for x in input]
    input = X
    # predict rating
    num_predict = 6 # banyaknya id buku yang mau diambil
    prediction = model.predict(input)
    prediction = prediction.reshape(-1) 
    #predicted_book_id = (-prediction).argsort()[:num_predict]
    predicted_book_id = [x+1 for x in range(num_predict)]
    predicted_rating = prediction[:numpredict]
    #predicted_rating = np.sort(prediction)[num_predict:][::-1]
    titles = list(books.iloc[predicted_book_id].title)
    image_urls = list(books.iloc[predicted_book_id].small_image_url)
    
    response_json = { "titles" : titles, "image_urls" : image_urls}

    return json.dumps(response_json)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)