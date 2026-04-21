import re

class SanitizadorMonetario:
    
    @staticmethod
    def limpar_valor(entrada: str) -> float:
        """
        Recebe uma string suja do usuário e converte para float seguro.
        Exemplos que ele resolve:
        '50' -> 50.0
        'R$ 50,00' -> 50.0
        '1.500,75' -> 1500.75
        'gastei 15,50' -> 15.5
        """
        if isinstance(entrada, (int, float)):
            return float(entrada)
            
        texto = str(entrada).strip()
        
        match = re.search(r'[\d\.,]+', texto)
        
        if not match:
            raise ValueError("Nenhum valor numérico encontrado na entrada.")
            
        numero_str = match.group()
        
        if '.' in numero_str and ',' in numero_str:
            numero_str = numero_str.replace('.', '')
            numero_str = numero_str.replace(',', '.')
        elif ',' in numero_str:
            numero_str = numero_str.replace(',', '.')
            
        try:
            return float(numero_str)
        except ValueError:
            raise ValueError(f"Não foi possível converter '{entrada}' para um valor financeiro válido.")