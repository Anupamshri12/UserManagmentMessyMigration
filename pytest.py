from unittest.mock import patch
from Services.user_service import *
from Helpers.CommonResponse import *
from CustomException import *



def test_search_users_success():
    
    response = search_users("Ranajan")
    assert response["errorCode"] == ErrorCode.SUCCESS.value
    assert response["errorMessage"] == "Success"

 
def test_search_users_not_found():
    try:
        search_users("Unknown")
    except CustomException as ce:
        assert ce.error_code == ErrorCode.NOT_FOUND
        assert ce.error_message == "Data not found"

def test_search_users_empty_name():
    try:
        search_users("")
    except CustomException as ce:
        assert ce.error_code == ErrorCode.VALIDATION_ERROR
        assert ce.error_message == "Please provide a name to search"

def test_get_all_users():
    
    response = get_all_users() 
    assert response['errorCode'] == ErrorCode.SUCCESS.value
    assert response['errorMessage'] == "Success"

def test_create_user_missing_fields():
    try:
        create_user({}) 
    except CustomException as ce:
        assert ce.error_code == ErrorCode.VALIDATION_ERROR
        assert ce.error_message == "Missing Fields"

  
def test_create_user_invalid_email():
    data = {
        'name': 'Anupam',
        'email' :'qwertyuiop67.com',
        'password': 'Password@123'
    }
    try:
        create_user(data)
    except CustomException as ce:
        assert ce.error_code == ErrorCode.VALIDATION_ERROR
        assert ce.error_message == "Invalid Email"


def test_create_user_invalid_password():
    data = {
        'name': 'Anupam',
        'email': 'user@example.com',
        'password': '123password'  
    }
    try:
        create_user(data)
    except CustomException as ce:
        assert ce.error_code == ErrorCode.VALIDATION_ERROR
        assert ce.error_message == "Invalid Password"


def test_create_user_email_exists():
    data = {
        'name': 'Anupam',
        'email': 'existing@example.com',
        'password': 'Password@123'
    }

    try:
        create_user(data)
    except CustomException as ce:
        assert ce.error_code == ErrorCode.VALIDATION_ERROR
        assert ce.error_message == "Email already exists"
    else:
        assert False, "CustomException not raised for duplicate email"

def test_update_user_success():
    data = {'name': 'New Name', 'email': 'new@example.com'}
    response = update_user(1, data)
    assert response['errorCode'] == ErrorCode.SUCCESS.value
    assert response['errorMessage'] == "User Updated"

def test_update_user_missing_fields():
    try:
        update_user(1, {})  
    except CustomException as ce:
        assert ce.error_code == ErrorCode.VALIDATION_ERROR
        assert ce.error_message == "Missing Fields"


def test_update_user_invalid_email():
    try:
        update_user(1, {'email': 'invalid-email'})
    except CustomException as ce:
        assert ce.error_code == ErrorCode.VALIDATION_ERROR
        assert ce.error_message == "Invalid Email"

def test_update_user_not_found():
    try:
        update_user(999, {'name': 'Test'})
    except CustomException as ce:
        assert ce.error_code == ErrorCode.NOT_FOUND
        assert ce.error_message == "User not found"


def test_login_success():
    data = {
        "email": "Ranjan@gmail.com",
        "password": "Ranjan12@"
    }
    response = login_user(data)
    assert response["errorCode"] == ErrorCode.SUCCESS.value
    assert response["errorMessage"] == "Login Successfull"


def test_login_missing_fields():
    try:
        login_user({})
    except CustomException as ce:
        assert ce.error_code == ErrorCode.VALIDATION_ERROR
        assert ce.error_message == "Missing Fields"

def test_login_invalid_credentials():
    try:
        login_user({"email": "test@example.com", "password": "wrongpass"})
    except CustomException as ce:
        assert ce.error_code == ErrorCode.VALIDATION_ERROR
        assert ce.error_message == "Login Failed"

test_create_user_invalid_email()
test_update_user_not_found()
test_update_user_invalid_email()
test_update_user_missing_fields()
test_update_user_success()
test_get_all_users()
test_search_users_success()
test_search_users_not_found()
test_search_users_empty_name()
test_login_success()
test_login_missing_fields()
test_login_invalid_credentials()