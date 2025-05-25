from src.Core.Entities.Aluno import Aluno
from src.Core.Entities.Professor import Professor
from src.Core.Entities.Turma import Turma

class Db:
    def __init__(self):
        # Dicionários simulando tabelas do banco de dados
        self.alunos: dict[int, Aluno] = {}        # chave: id_aluno, valor: objeto Aluno
        self.professores: dict[int, Professor] = {}   # chave: id_professor, valor: objeto Professor
        self.turmas: dict[int, Turma] = {}        # chave: id_turma, valor: objeto Turma
        # Adicione outros dicionários conforme necessário

    # Aluno ______________________________________________________________________
    # Adiciona um aluno e gera a matrícula automaticamente
    def adicionar_aluno(self, aluno : Aluno):
        # Gera a próxima matrícula disponível
        if self.alunos:
            proxima_matricula = max(self.alunos.keys()) + 1
        else:
            proxima_matricula = 1
        aluno.matricula = proxima_matricula
        self.alunos[aluno.matricula] = aluno
        return aluno

    # Edita os dados de um aluno pelo id
    def editar_aluno(self, aluno_id: int, novo_aluno: Aluno):
        if aluno_id in self.alunos:
            self.alunos[aluno_id] = novo_aluno

    # Remove um aluno pelo id
    def excluir_aluno(self, aluno_id: int):
        if aluno_id in self.alunos:
            del self.alunos[aluno_id]

    # Retorna a lista de todos os alunos
    def listar_alunos(self):
        return list(self.alunos.values())
    

    # Professor __________________________________________________________________
    # Adiciona um professor e gera a matrícula automaticamente
    def adicionar_professor(self, professor: Professor):
        # Gera a próxima matrícula disponível para professor
        if self.professores:
            proxima_matricula = max(self.professores.keys()) + 1
        else:
            proxima_matricula = 1
        professor.matricula = proxima_matricula
        self.professores[professor.matricula] = professor
        return professor

    # Edita os dados de um professor pelo id
    def editar_professor(self, professor_id: int, novo_professor: Professor):
        if professor_id in self.professores:
            self.professores[professor_id] = novo_professor

    # Remove um professor pelo id
    def excluir_professor(self, professor_id: int):
        if professor_id in self.professores:
            del self.professores[professor_id]

    # Retorna a lista de todos os professores
    def listar_professores(self):
        return list(self.professores.values())


    # Turma ______________________________________________________________________
    # Adiciona uma turma e gera o id automaticamente
    def adicionar_turma(self, turma: Turma):
        # Gera o próximo id disponível para turma
        if self.turmas:
            proximo_id = max(self.turmas.keys()) + 1
        else:
            proximo_id = 1
        turma.id = proximo_id
        self.turmas[turma.id] = turma
        return turma

    # Edita os dados de uma turma pelo id
    def editar_turma(self, turma_id: int, nova_turma: Turma):
        if turma_id in self.turmas:
            self.turmas[turma_id] = nova_turma

    # Remove uma turma pelo id
    def excluir_turma(self, turma_id: int):
        if turma_id in self.turmas:
            del self.turmas[turma_id]

    # Retorna a lista de todas as turmas
    def listar_turmas(self):
        return list(self.turmas.values())


