"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template
import connexion

# options = {'swagger_path': 'c:/users/kircho/appdata/local/programs/python/python37/lib/site-packages/swagger_ui'}
# create the application instance
app = connexion.App(__name__, specification_dir="/")

# Cead the swagger.yml file to configure the endpoints
# app.add_api("swagger.yml")
app.add_api("swagger_sol.yml")


# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='127.0.0.1', debug=True)
