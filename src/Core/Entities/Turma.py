from src.Core.Enums.Disciplinas import Disciplina
from src.Core.Entities.Aluno import Aluno

class Turma:
    def __init__(self, disciplina: Disciplina):
        self.disciplina = disciplina
        self.alunos : list[Aluno] = []
        self.id : int

    def adicionar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)