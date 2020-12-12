# Import dependencies
from flask import Flask, render_template, render_template
from flask_pymongo import PyMongo
import scrape_mars

# Setup flask
app = Flask(__name__)

# Mongo connection using flask_pymongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# Landing page setup
@app.route("/")
def index():


# Scrape the scrape_mars file and when done return to landing page
@app.route("/scrape")
def scraper():
    mars = mongo.db.mars_info
    mars_info = scrape_mars.scrape()
    mars.update({}, mars_info, upsert=True)
    return redirect("/", code=382)

if __name__ = "__main__":
    app.run(debug=True)