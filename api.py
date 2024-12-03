from flask import Flask
from flask_pymongo import PyMongo
import os 
from marshmallow import Schema, fields

app = Flask(__name__)
app.config["MONGODB_URL"] = os.getenv("MONGODB_URL")
mongo = PyMongo(app)

class DriverSchema(Schema):
    _id: fields.Str()
    name: fields.Str()
    email: fields.Str()
    phone: fields.Str()
    address: fields.Str()
    rating: fields.Int()
    status: fields.Str()
    license_id: fields.Str()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)