from flask import Flask, jsonify, request, abort
from flask.views import MethodView
from flask_injector import FlaskInjector
from injector import inject, injectable
from typing import Tuple

app = Flask(__name__)


class UserRepository:
    def add(self, user: dict) -> None:
        pass

    def get(self, user_id: int) -> dict:
        pass

    def delete(self, user: dict) -> None:
        pass


class UserController(MethodView):
    @inject
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def post(self) -> Tuple[dict, int]:
        user = request.json
        self.user_repository.add(user)
        return jsonify(user), 201


class UserUpdateController(MethodView):
    @inject
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def put(self, user_id: int) -> Tuple[dict, int]:
        user = self.user_repository.get(user_id)
        if not user:
            abort(404)

        user.update(request.json)

        return jsonify(request.json), 200

    def patch(self, user_id: int) -> Tuple[dict, int]:
        user = self.user_repository.get(user_id)
        if not user:
            abort(404)

        key = list(request.json.keys())[0]
        user[key] = request.json[key]

        return jsonify(request.json), 200

    def delete(self, user_id: int) -> Tuple[str, int]:
        user = self.user_repository.get(user_id)
        if not user:
            abort(404)

        self.user_repository.delete(user)

        return '', 204


app.add_url_rule('/users', view_func=UserController.as_view('user'))
app.add_url_rule('/users/<int:user_id>', view_func=UserUpdateController.as_view('user_update'))


@injectable
class AppSetup:
    @inject
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def configure_injector(self, binder) -> None:
        binder.bind(UserRepository, to=self.user_repository)


FlaskInjector(app=app, modules=[AppSetup()])