class CustomException(Exception):
    def __init__(self, error_code ,error_message= None):
        super().__init__()
        self.error_code = error_code
        self.error_message = error_message
        
       
