from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/data/<int:id>')
def index_var(id):
    return render_template("index.html", id=id)

@app.route('/data/<string:src>')
def image_test(src):
    return render_template("view-image.html", img_src='static/'+src)

@app.route("/test/")
def test():
    ls = [1, 2, 3]
    return json.dumps(ls)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)
