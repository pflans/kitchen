import os
import flask
from flask_cors import CORS, cross_origin
from flask import jsonify, render_template
import gkeepapi
import json

keep = gkeepapi.Keep()
success = keep.login('patfmurray@gmail.com', os.environ.get("GOOGLEPASS"))

app = flask.Flask(__name__, static_folder="../kitchen-app/build/static", template_folder="../kitchen-app/build")
#CORS(app, support_credentials=True)
app.config["DEBUG"] = True

@app.route("/")
#@cross_origin(support_credentials=True)
def index():
    return render_template("index.html")

@app.route('/api/v1/resources/notes/backgrounds', methods=['GET'])
#@cross_origin(supports_credentials=True)
def api_all():
    notes = list(keep.find(labels=[keep.findLabel('Background')]))
    notes_arr = [];
    for note in notes:
        notes_arr.append({
            "title": note.title,
            "text": note.text
        });
    return jsonify(notes_arr)

# artLabel = keep.findLabel('Art')
# labels = keep.labels()
# gnotes = keep.find(labels=[keep.findLabel('Art')])
# noteList = list(gnotes)

# @app.route('/', methods=['GET'])
# def home():
#   string = '<ul>'
#   for note in noteList:
#     string += '<li>' + note.text + '</li>'
#   string += '</ul>'
#   return string

app.run(host='0.0.0.0')
