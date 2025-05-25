from src.Core.Enums.Disciplinas import Disciplina
from src.Core.Entities.Turma import Turma 
from src.Core.Entities.Aluno import Aluno


class Professor:

    def __init__(self):
        self.nome: str
        self.matricula: int
        self.disciplinas: list[Disciplina] = []
        self.turmas: list[Turma] = []

    def cadastrar_aluno(self, aluno: Aluno) -> None:
        for turma in self.turmas:
            turma.adicionar_aluno(aluno)

    def logar(self, nome: str, matricula: int) -> bool:
        """
        Simula o login do professor verificando nome e matrícula.
        """
        return self.nome == nome and self.matricula == matricula



