import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    return user_response.json()["authToken"]


def positive_assert(name):
    token = get_new_user_token()
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(name):
    token = get_new_user_token()
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 400


# Prueba 1. 1 caracter permitido
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


# Prueba 2. 511 caracteres permitidos
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("a" * 511)


# Prueba 3. String vacio (0 caracteres)
def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400("")


# Prueba 4. 512 caracteres (excede el limite)
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400("a" * 512)


# Prueba 5. Caracteres especiales permitidos
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")


# Prueba 6. Espacios permitidos
def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(" A Aaa ")


# Prueba 7. Numeros como string, permitidos
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")


# Prueba 8. El parametro "name" no se envia
def test_create_kit_no_name_get_error_response():
    token = get_new_user_token()
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 400


# Prueba 9. Tipo de dato incorrecto (numero en vez de string)
def test_create_kit_number_type_name_get_error_response():
    token = get_new_user_token()
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 400