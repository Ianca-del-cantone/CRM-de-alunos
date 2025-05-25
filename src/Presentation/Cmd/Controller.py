from src.Infra.Db import Db

class Controller():
    def __init__(self, db: Db):
        self.db: Db = db

    def do_criar_aluno(self, arg):
        """Cria um novo aluno: criar_aluno NOME"""
        if not arg:
            print("Erro: Nome do aluno é obrigatório. Uso: criar_aluno NOME")
            return
        
        from src.Core.Entities.Aluno import Aluno
        aluno = Aluno(arg)
        resultado = self.db.adicionar_aluno(aluno)
        print(f"Aluno criado com ID: {resultado.matricula}" if resultado else "Falha ao criar aluno")

    def do_editar_aluno(self, arg):
        """Edita um aluno existente: editar_aluno ID NOME"""
        args = arg.split()
        if len(args) < 2:
            print("Erro: São necessários ID e NOME. Uso: editar_aluno ID NOME")
            return
        
        aluno_id = int(args[0])
        nome = ' '.join(args[1:])
        
        aluno = self.db.alunos.get(aluno_id)
        if aluno:
            aluno.nome = nome
            self.db.editar_aluno(aluno_id, aluno)
            print(f"Aluno {aluno_id} atualizado para: {nome}")
        else:
            print(f"Aluno com ID {aluno_id} não encontrado")

    def do_listar_alunos(self, arg=None):
        """Lista todos os alunos cadastrados: listar_alunos"""
        alunos = self.db.listar_alunos()
        if not alunos:
            print("Nenhum aluno cadastrado.")
            return
        for aluno in alunos:
            print(f"ID: {aluno.matricula} | Nome: {aluno.nome}")