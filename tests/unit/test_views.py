import unittest
from flask import Flask
from unittest.mock import MagicMock
from IO_LOTTERYPB.views import UserRepository, UserController, UserUpdateController, AppSetup

class TestUserAPI(unittest.TestCase):
        def setUp(self):
            self.app = Flask(__name__)
            self.client = self.app.test_client()

            self.user_repository = MagicMock(spec=UserRepository)
            self.app_setup = AppSetup(self.user_repository)
            self.app_setup.configure_injector(self.app.injector)

            # Add routes
            self.app.add_url_rule('/users', view_func=UserController.as_view('user'))
            self.app.add_url_rule('/users/<int:user_id>', view_func=UserUpdateController.as_view('user_update'))

def test_create_user(self):
    user_data = {'name': 'Krzysiu', 'age': 23}
    response = self.client.post('/users', json=user_data)
    self.assertEqual(response.status_code, 201)
    self.assertEqual(response.get_json(), user_data)
    self.user_repository.add.assert_called_once_with(user_data)

def test_update_user(self):
    user_id = 1
    user_data = {'name': 'Krzysiu'}
    self.user_repository.get.return_value = {'id': user_id, 'name': 'Andrzejek', 'age': 25}
    response = self.client.put(f'/users/{user_id}', json=user_data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.get_json(), user_data)
    self.user_repository.get.assert_called_once_with(user_id)
    self.user_repository.update.assert_called_once_with(user_id, user_data)

def test_partial_update_user(self):
    user_id = 1
    user_data = {'age': 23}
    self.user_repository.get.return_value = {'id': user_id, 'name': 'Andrzejek', 'age': 25}
    response = self.client.patch(f'/users/{user_id}', json=user_data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.get_json(), user_data)
    self.user_repository.get.assert_called_once_with(user_id)
    self.user_repository.partial_update.assert_called_once_with(user_id, user_data)

def test_delete_user(self):
    user_id = 1
    self.user_repository.get.return_value = {'id': user_id, 'name': 'Andrzejek', 'age': 25}
    response = self.client.delete(f'/users/{user_id}')
    self.assertEqual(response.status_code, 204)
    self.assertEqual(response.data, b'')
    self.user_repository.get.assert_called_once_with(user_id)
    self.user_repository.delete.assert_called_once_with(user_id)