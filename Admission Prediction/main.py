from flask import Flask, render_template, request, jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__)   #initializing App name

@app.route('/',method = ['GET'])    #route for home page
@cross_origin()
def homePage():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)