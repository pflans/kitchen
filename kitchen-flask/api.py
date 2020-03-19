import flask
from flask_cors import CORS
from flask import jsonify
import gkeepapi
import json

keep = gkeepapi.Keep()
success = keep.login('patfmurray@gmail.com', '{API KEY}')

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

@app.route('/api/v1/resources/notes/backgrounds', methods=['GET'])
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
