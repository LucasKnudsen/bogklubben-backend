from fastapi import HTTPException


class GlobalAPIException(HTTPException):
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(status_code=status_code, detail=message)
        self.message = message
        self.status_code = status_code
