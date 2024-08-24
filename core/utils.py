class OperationResult:
    def __init__(self):
        self.status = True
        self.http_status = 200
        self.message = "Success"
        self.data = None

    def set_error(self, message, http_status=500):
        self.status = False
        self.http_status = http_status
        self.message = message
        self.data = None

    def set_data(self, data):
        self.data = data

    def to_dict(self):
        return {
            "status": self.status,
            "http_status": self.http_status,
            "message": self.message,
            "data": self.data
        }