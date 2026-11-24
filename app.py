from flask import Flask, render_template

# 1. Create a Flask application instance
app = Flask(__name__)

# 2. Define the route for the home page ("/")
@app. route("/")
def home():
    # Look inside the 'templates' folder and serve index.html
    return render_template("index.html")

# 3. Run the server when this file is executed directly
if __name__== "__main__":
    app.run(debug=True)