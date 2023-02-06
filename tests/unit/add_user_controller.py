from IO_LOTTERYPB.controllers import AddUserController, AddUserRequest
from tests.integrations.test_users import UserPayloadFactory


def test_can_instantiate_add_user_controller(capsys) -> None:
    controller = AddUserController()
    payload = UserPayloadFactory()
    request = AddUserRequest(json=payload)
    controller.add(request=request)
    actual = capsys.readouterr().out
    expected = f"{payload}\n"
    assert actual == expected


def test_add_user_request_has_json_field() -> None:
    payload = UserPayloadFactory()
    request = AddUserRequest(json=payload)
    assert request.json
