from flask import *
from flask_cors import CORS, cross_origin
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
todos= [{"gato":"Guardião", "foto":"https://scontent.fpoa40-1.fna.fbcdn.net/v/t1.0-9/156821323_3285826531643750_2736273613384619373_n.jpg?_nc_cat=111&ccb=1-3&_nc_sid=8bfeb9&_nc_ohc=xDZ4BtiXYxsAX-qGJNc&_nc_ht=scontent.fpoa40-1.fna&oh=091dd8bbcde17830c79e2eb73a5fac76&oe=607178C7"},{"gato":"preta","foto":"https://scontent.fpoa40-1.fna.fbcdn.net/v/t1.0-9/123222427_3177474972478907_7165655200423242901_o.jpg?_nc_cat=100&ccb=1-3&_nc_sid=8bfeb9&_nc_ohc=d3D7TEDCvS4AX_6zYhM&_nc_ht=scontent.fpoa40-1.fna&oh=1d02db384f6bd9b9218e8460b341e85f&oe=60708960"}]

@app.route('/todos', methods=['GET'])
@cross_origin()
def hello_world():
    json_text = jsonify(todos)
    return json_text



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)