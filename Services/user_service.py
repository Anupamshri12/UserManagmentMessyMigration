from Helpers.CommonResponse import *
from CustomException.custom_exception import *

import re
from Dao.user_dao import (
    fetch_all_users, fetch_user_by_id,
    insert_user, update_user_data, delete_user_by_id,
    search_users_by_name, validate_user_credentials,
    get_user_by_email 
)


EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
PASSWORD_REGEX = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?/~\-]).{8,}$"
)

def get_all_users():
    try:
        data = fetch_all_users()
        if not data:
            raise CustomException(ErrorCode.NOT_FOUND, "Users not found")
        return common_response(ErrorCode.SUCCESS ,data = data)
    except Exception as e:
        return CustomException(ErrorCode.SERVER_ERROR)

def get_user_by_id(user_id):
    try:
        user = fetch_user_by_id(user_id)
        if user:
            return common_response(ErrorCode.SUCCESS  ,data = user)
        raise CustomException(ErrorCode.NOT_FOUND ,"User not found")
    except CustomException as ce:
        raise ce
    except Exception as e:
        raise CustomException(ErrorCode.SERVER_ERROR)

def create_user(data):
    try:
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
           raise CustomException(ErrorCode.VALIDATION_ERROR ,"Missing Fields")

        if not EMAIL_REGEX.match(email):
           raise CustomException(ErrorCode.VALIDATION_ERROR ,"Invalid Email")
        
        if not PASSWORD_REGEX.match(password):
           raise CustomException(ErrorCode.VALIDATION_ERROR ,"Invalid Password")


        if get_user_by_email(email):
           raise CustomException(ErrorCode.VALIDATION_ERROR ,"Email already exists")

        insert_user(name, email, password)
        data = get_user_by_email(email)
        return common_response(ErrorCode.SUCCESS ,"User created Successfully" ,data)
 
    except CustomException as ce:
        raise ce
    except Exception as e:
        raise CustomException(ErrorCode.SERVER_ERROR)

def update_user(user_id, data):
    try:
        user = fetch_user_by_id(user_id)

        if not user:
            raise CustomException(ErrorCode.NOT_FOUND ,"User not found")

        name = data.get('name')
        email = data.get('email')

        if not name and not email:
            raise CustomException(ErrorCode.VALIDATION_ERROR ,"Missing Fields")

        if email and not EMAIL_REGEX.match(email):
            raise CustomException(ErrorCode.VALIDATION_ERROR ,"Invalid Email")

        update_user_data(user_id, name, email)
        data = fetch_user_by_id(user_id)
        return common_response(ErrorCode.SUCCESS ,"User Updated", data)
    
    except CustomException as ce:
        raise ce
    except Exception as e:
        raise CustomException(ErrorCode.SERVER_ERROR)
def delete_user(user_id):
    try:
        user = fetch_user_by_id(user_id)
        if user:
           delete_user_by_id(user_id)
           return common_response(ErrorCode.SUCCESS ,error_message="User Deleted")

        raise CustomException(ErrorCode.NOT_FOUND ,"User not Found")
    
    except CustomException as ce:
        raise ce
    except Exception as e:
        raise CustomException(ErrorCode.SERVER_ERROR)

def search_users(name):
    try:
        if not name:
            raise CustomException(ErrorCode.VALIDATION_ERROR ,"Please provide a name to search")
        data = search_users_by_name(name)

        if not data:
            raise CustomException(ErrorCode.NOT_FOUND, "Data not found")
        
        return common_response(ErrorCode.SUCCESS ,data = data)
    
    except CustomException as ce:
         raise ce
    except Exception as e:
        raise CustomException(ErrorCode.SERVER_ERROR)

def login_user(data):
    try:
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise CustomException(ErrorCode.VALIDATION_ERROR ,"Missing Fields")

        if validate_user_credentials(email, password):
            return common_response(ErrorCode.SUCCESS ,error_message="Login Successfull")
        raise CustomException(ErrorCode.VALIDATION_ERROR ,"Login Failed")
    
    except CustomException as ce:
        raise ce

    except Exception as e:
        raise CustomException(ErrorCode.SERVER_ERROR)
