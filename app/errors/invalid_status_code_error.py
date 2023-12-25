class InvalidStatusCodeError(RuntimeError):

    def __init__(self):
        super().__init__("Error: Status de Erro HTTP Inválido")