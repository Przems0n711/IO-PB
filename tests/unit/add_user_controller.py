from IO_LOTTERYPB import controllers

def test_can_instantiate_add_user_controller() -> None:
   controller = AddUserController()
   with pytest.raises(NotImplementedError):
    controller.add()


def test_add_user_request_has_json_field() -> None:
    request = AddUserRequest()
    assert request.json

