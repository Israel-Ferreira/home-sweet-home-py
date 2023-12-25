class NotFoundError(RuntimeError):
    def __init__(self) -> None:
        self.msg = "Recurso não encontrado"
        super().__init__(self.msg)
