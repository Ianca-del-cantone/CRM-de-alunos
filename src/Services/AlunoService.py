from src.Core.Enums.Disciplinas import Disciplina
from src.Infra.Db import Db
from src.Core.Entities.Aluno import Aluno

class AlunoService:
    def __init__(self, db: Db):
        self.db: Db = db

    def criar_aluno(self, nome: str):
            """Cria um novo aluno"""
            aluno = Aluno(nome)
            resultado = self.db.adicionar_aluno(aluno)
            return resultado
    
    def cadastrar_nota(self, matricula: int, disciplina: Disciplina, valor: float):
        """Cadastra uma nota para um aluno"""
        aluno = self.db.obter_aluno(matricula)
        if aluno:
            aluno.cadastrar_nota(disciplina, valor)
            self.db.editar_aluno(matricula, aluno)
            return True
        return False
    
    def verificar_situacao(self, matricula: int) -> str:
        """Verifica a situação do aluno (aprovado ou reprovado)"""
        aluno = self.db.obter_aluno(matricula)
        if aluno:
            return aluno.verificar_situacao()
        return "Aluno não encontrado"   
    
    def listar_alunos(self):
        """Lista todos os alunos cadastrados"""
        return self.db.listar_alunos()
    
    def editar_aluno(self, aluno_id: int, nome: str) -> bool:
        """Edita o nome de um aluno existente"""
        aluno = self.db.obter_aluno(aluno_id)
        if aluno:
            aluno.nome = nome
            self.db.editar_aluno(aluno_id, aluno)
            return True
        return False




