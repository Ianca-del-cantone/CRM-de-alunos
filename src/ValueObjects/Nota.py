from Enums.Disciplinas import Disciplina
from typing import Dict, Optional


class HistoricoEscolar:
    def __init__(self, notas: Optional[Dict[Disciplina, float]] = None) -> None:
        self.notas: Dict[Disciplina, float] = notas if notas is not None else {}

    def adicionar_nota(self, disciplina: Disciplina, valor: float) -> None:
        self.notas[disciplina] = valor

    def to_dict(self) -> dict:
        return {disciplina.name: valor for disciplina, valor in self.notas.items()}

