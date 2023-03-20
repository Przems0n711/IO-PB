from dataclasses import dataclass

from IO_LOTTERYPB.repositories import UserRepository

@dataclass
class AddUserRequest:
    json: dict


class AddUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def add(self, request: AddUserRequest) -> None:
        self._repository.add()
        print(request.json)


class GetUserController:
    def get(self, id: int):
        raise NotImplementedError

class UserController:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_all_users(self):
        raise NotImplementedError()

    def get_user_by_id(self, user_id):
        raise NotImplementedError()

    def create_user(self, user):
        return self.user_repository.create_user(user)

    def update_user(self, user_id, user):
        return self.user_repository.update_user(user_id, user)

    def delete_user(self, user_id):
        raise NotImplementedError()