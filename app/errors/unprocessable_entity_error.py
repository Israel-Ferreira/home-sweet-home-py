class UnprocessableEntityError(RuntimeError):
    def __init__(self, msg) -> None:
        self.msg = msg
        self.status_code = 422
        super().__init__(msg)