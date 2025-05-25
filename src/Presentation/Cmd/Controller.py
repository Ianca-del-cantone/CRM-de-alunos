from src.Services.AlunoService import AlunoService

class Controller():
    def __init__(self, aluno_service: AlunoService):
        self.aluno_service = aluno_service

    def do_criar_aluno(self, arg):
        """Cria um novo aluno: criar_aluno NOME"""
        if not arg:
            print("Erro: Nome do aluno é obrigatório. Uso: criar_aluno NOME")
            return
        resultado = self.aluno_service.criar_aluno(arg)
        print(f"Aluno criado com ID: {resultado.matricula}" if resultado else "Falha ao criar aluno")

    def do_editar_aluno(self, arg):
        """Edita um aluno existente: editar_aluno ID NOME"""
        args = arg.split()
        if len(args) < 2:
            print("Erro: São necessários ID e NOME. Uso: editar_aluno ID NOME")
            return
        aluno_id = int(args[0])
        nome = ' '.join(args[1:])
        sucesso = self.aluno_service.editar_aluno(aluno_id, nome)
        if sucesso:
            print(f"Aluno {aluno_id} atualizado para: {nome}")
        else:
            print(f"Aluno com ID {aluno_id} não encontrado")

    def do_listar_alunos(self, arg=None):
        """Lista todos os alunos cadastrados: listar_alunos"""
        alunos = self.aluno_service.listar_alunos()
        if not alunos:
            print("Nenhum aluno cadastrado.")
            return
        for aluno in alunos:
            situacao = self.aluno_service.verificar_situacao(aluno.matricula)
            media = aluno.media
            print(f"ID: {aluno.matricula} | Nome: {aluno.nome} | Situação: {situacao}  | Media: {media}  ")
            print("  Histórico Escolar:")
            for disciplina, nota in aluno.historico.notas.items():
                print(f"    {disciplina.name}: {nota}")
            print("-")

    def do_cadastrar_nota(self, arg):
        """Cadastra uma nota para um aluno: cadastrar_nota MATRICULA DISCIPLINA VALOR"""
        args = arg.split()
        if len(args) < 3:
            print("Erro: São necessários MATRICULA, DISCIPLINA e VALOR. Uso: cadastrar_nota MATRICULA DISCIPLINA VALOR")
            return
        try:
            matricula = int(args[0])
            from src.Core.Enums.Disciplinas import Disciplina
            disciplina = Disciplina[args[1]]
            valor = float(args[2])
        except Exception as e:
            print(f"Erro nos parâmetros: {e}")
            return
        sucesso = self.aluno_service.cadastrar_nota(matricula, disciplina, valor)
        if sucesso:
            print(f"Nota cadastrada para o aluno {matricula} na disciplina {disciplina.name}.")
        else:
            print(f"Aluno com matrícula {matricula} não encontrado.")

    def do_verificar_situacao(self, arg):
        """Verifica a situação do aluno: verificar_situacao MATRICULA"""
        if not arg:
            print("Erro: Matrícula do aluno é obrigatória. Uso: verificar_situacao MATRICULA")
            return
        try:
            matricula = int(arg)
        except Exception:
            print("Erro: Matrícula deve ser um número inteiro.")
            return
        situacao = self.aluno_service.verificar_situacao(matricula)
        print(f"Situação do aluno {matricula}: {situacao}")