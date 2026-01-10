class DangerException(Exception):
    def __init__(self, msg, code):
        self.msg = msg
        self.code = code
        super().__init__(msg)

    def __str__(self):
        return f"({self.msg}) code: ({self.code})"


val = int(input("Enter Water Level"))
if val < 5000:
    raise DangerException("Water level too low in reactor", 401)
