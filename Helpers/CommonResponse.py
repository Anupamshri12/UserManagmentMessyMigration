from enum import Enum

class ErrorCode(Enum):
    SUCCESS = 0
    VALIDATION_ERROR = 1
    NOT_FOUND = 2
    SERVER_ERROR = 3


ERROR_MESSAGES = {
    ErrorCode.SUCCESS: "Success",
    ErrorCode.VALIDATION_ERROR: "Validation failed.",
    ErrorCode.NOT_FOUND: "Resource not found.",
    ErrorCode.SERVER_ERROR: "Internal server error."
}


def common_response(error_code = ErrorCode.SUCCESS , error_message = None,data=None):

        if error_message == None:
            error_message = ERROR_MESSAGES.get(error_code, "Unknown error") 

        return{
        "errorCode": error_code.value,
        "errorMessage": error_message,
        "data": data
        }
