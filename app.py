from flask import Flask
from Controllers.user_controller import user_bp

from flask import Flask, jsonify
from CustomException.custom_exception import CustomException
from Helpers.CommonResponse import common_response
from Helpers.CommonResponse import *

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(user_bp)

    @app.errorhandler(CustomException)
    def handle_custom_exception(error):
        status_code = 200
        response = common_response(
            error_code=error.error_code,
            error_message = error.error_message,
            data=None
        )
        if(error.error_code == ErrorCode.NOT_FOUND):
            status_code = 404
        elif(error.error_code == ErrorCode.VALIDATION_ERROR):
            status_code = 400
        else:
            status_code = 500
        return jsonify(response) ,status_code
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
