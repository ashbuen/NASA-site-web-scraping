# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# Setup flask
app = Flask(__name__)

# Inline Mongo connection using flask_pymongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
# mongo = PyMongo(app, uri = "mongodb://localhost:27017/mars_db")

# Landing page setup
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Scrape the scrape_mars file and when done return to landing page
@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)

# Redirect to homepage
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)