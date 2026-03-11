from flask import Flask
from flask_cors import CORS
import config
import crud

app = Flask(__name__)

# Load configuration
app.config['SECRET_KEY'] = config.SECRET_KEY
CORS(app)
#put functionsss
# Register routes
@app.route('/')
def index():
    return "Hello from Flask!"
#DELETE
@app.route('/hello',methods=["GET"])
def hello():
    return "hi"

@app.route("/todos", methods=["POST"])
def create_todo_route():
    #create
    return {}

#u can create two routes same name but diff meth
@app.route("/todos", methods=["GET"])
def get_todo_route():
    return{}

@app.route("/todos", methods=["PUT"])
def update_todo_route():
    return {}

@app.route("/todos" , methods=["DELETE"])
def delete_todo_route():
    return{}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
