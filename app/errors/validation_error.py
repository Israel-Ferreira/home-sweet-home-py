class ValidationError(RuntimeError):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)
