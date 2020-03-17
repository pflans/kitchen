import flask
import gkeepapi


keep = gkeepapi.Keep()
success = keep.login('patfmurray@gmail.com', 'uunmqnvciqhgnhph')

artLabel = keep.findLabel('Art')
labels = keep.labels()
gnotes = keep.find(labels=[keep.findLabel('Art')])
noteList = list(gnotes)

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])

def home():
  string = '<ul>'
  for note in noteList:
    string += '<li>' + note.text + '</li>'
  string += '</ul>'
  return string


app.run(host='0.0.0.0')
