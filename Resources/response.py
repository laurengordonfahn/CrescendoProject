class Response:
    def __init__(self, success:bool, response=None, message=None):
        self.success = success
        self.response = response
        self.message = message