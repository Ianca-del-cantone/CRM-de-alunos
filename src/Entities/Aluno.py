from Enums.Disciplinas import Disciplina
from ValueObjects.Nota import HistoricoEscolar
from typing import Optional
import uuid

class Aluno:
    """
    Representa um aluno com informações pessoais, matrícula e histórico escolar.
    """
    def __init__(self, nome: str, historico: Optional[HistoricoEscolar] = None) -> None:
        """
        Inicializa um novo aluno.
        """
        self.nome: str = nome
        self.matricula: uuid.UUID = uuid.uuid4()
        self._historico: HistoricoEscolar = historico if historico else HistoricoEscolar()

    @property
    def historico(self) -> HistoricoEscolar:
        """
        Retorna o histórico escolar do aluno.
        """
        return self._historico

    @historico.setter
    def historico(self, novo_historico: HistoricoEscolar) -> None:
        """
        Define um novo histórico escolar para o aluno.
        """
        self._historico = novo_historico

    def cadastrar_nota(self, disciplina: Disciplina, valor: float) -> None:
        """
        Adiciona uma nota ao histórico escolar do aluno.
        """
        self._historico.adicionar_nota(disciplina, valor)

    @property
    def media(self) -> float:
        """
        Calcula e retorna a média das notas do aluno.
        """
        if self._historico.notas:
            return sum(self._historico.notas.values()) / len(self._historico.notas)
        return 0.0

    @property
    def situacao(self) -> bool:
        """
        Retorna True se o aluno está aprovado (média >= 7.0), senão False.
        """
        return self.media >= 7.0
    
    def verificar_situacao(self) -> str:
        """
        Retorna uma string indicando se o aluno está aprovado ou reprovado.
        """
        return "Aprovado" if self.situacao else "Reprovado"