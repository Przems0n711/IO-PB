from flask import Flask, Response, request, jsonify
from flask_restful import Resource, Api

from IO_LOTTERYPB.controllers import AddUserController, AddUserRequest

app = Flask(__name__)
api = Api(app)

class UserController(Resource):
    def post(self):
        dto = request.get_json()
        return {"message": "User created", "data": dto}, 201
        
class OtherController(Resource):
    def post(self):
        raise NotImplementedError

api.add_resource(UserController, '/users')
api.add_resource(OtherController, '/other')

def handle_not_implemented_error(e):
    return {"message": "Not Implemented"}, 501

@app.post("/other")
def add_user() -> Response:
    othercontroller = AddOtherController
    othercontroller.add(request=AddUserRequest(json=request.json))
    return jsonify(request.json)

@app.post("/users")
def add_user() -> Response:
    controller = AddUserController()
    controller.add(request=AddUserRequest(json=request.json))
    return jsonify(request.json)
