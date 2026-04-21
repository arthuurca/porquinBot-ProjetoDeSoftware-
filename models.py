from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    def __init__(self, valor: float, categoria: str, descricao: str = ""):
        self._valor = abs(valor)
        self._categoria = categoria
        self._descricao = descricao
        self._data = datetime.now()

    @property
    def valor(self) -> float:
        return self._valor

    @property
    def categoria(self) -> str:
        return self._categoria.capitalize()

    @property
    def data_formatada(self) -> str:
        return self._data.strftime("%d/%m/%Y %H:%M")

    @abstractmethod
    def obter_impacto(self) -> float:
        pass

class Despesa(Transacao):
    def obter_impacto(self) -> float:
        return -self._valor

class Receita(Transacao):
    def obter_impacto(self) -> float:
        return self._valor

class Carteira:
    def __init__(self):
        self._lista_transacoes: list[Transacao] = []
        self._saldo_atual = 0.0

    @property
    def saldo(self) -> float:
        return self._saldo_atual

    def adicionar_transacao(self, t: Transacao):
        self._lista_transacoes.append(t)
        self._saldo_atual += t.obter_impacto()

    def get_extrato(self) -> str:
        if not self._lista_transacoes:
            return "Nenhuma transação registrada."
        
        extrato = "--- Extrato Atual ---\n"
        for t in self._lista_transacoes:
            tipo = "⬆️" if t.obter_impacto() > 0 else "⬇️"
            extrato += f"{tipo} {t.categoria}: R$ {t.valor:.2f}\n"
        extrato += f"---------------------\nSaldo: R$ {self._saldo_atual:.2f}"
        return extrato

class MetaFinanceira(ABC):
    def __init__(self, nome: str, valor_alvo: float):
        self._nome = nome
        self._valor_alvo = valor_alvo
        self._valor_poupado = 0.0

    def poupar(self, valor: float):
        if valor > 0: self._valor_poupado += valor

    @abstractmethod
    def exibir_status(self) -> str:
        pass

class MetaSimples(MetaFinanceira):
    def exibir_status(self) -> str:
        percent = (self._valor_poupado / self._valor_alvo) * 100 if self._valor_alvo > 0 else 0
        return f"🎯 {self._nome}: {percent:.1f}% concluído."

class MetaComPrazo(MetaFinanceira):
    def __init__(self, nome: str, valor_alvo: float, dias: int):
        super().__init__(nome, valor_alvo)
        self._dias_restantes = dias

    def exibir_status(self) -> str:
        return f"⏰ {self._nome}: Faltam {self._dias_restantes} dias para atingir R$ {self._valor_alvo:.2f}"

class Orcamento:
    def __init__(self, categoria: str, teto: float, gasto_atual: float = 0.0):
        self._categoria = categoria
        self._teto = teto
        self._gasto_atual = gasto_atual

    @property
    def categoria(self): return self._categoria

    @property
    def teto(self): return self._teto

    @property
    def progresso(self):
        return (self._gasto_atual / self._teto) * 100 if self._teto > 0 else 0

    def obter_status(self) -> str:
        restante = self._teto - self._gasto_atual
        if restante <= 0:
            return f"⚠️ *ALERTA:* O teto de {self._categoria} foi excedido em R$ {abs(restante):.2f}!"
        return f"✅ {self._categoria}: R$ {self._gasto_atual:.2f} de R$ {self._teto:.2f} ({self.progresso:.1f}%)"