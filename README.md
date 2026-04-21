🐷 porquinhoBot

Um bot para o Telegram desenvolvido em Python que funciona como o seu cofrinho e gerente financeiro pessoal. O porquinhoBot ajuda a registrar receitas, controlar despesas, acompanhar metas e definir tetos de gastos, tudo através de uma interface interativa de botões e comandos simples! E claro, sempre com um amigável "Oinc Oinc!".

--------------------------------------------------

⚙️ Como o Código Funciona (Arquitetura)

O projeto foi estruturado utilizando princípios de Programação Orientada a Objetos (POO) e separação de responsabilidades.

main.py (O Cérebro do Bot):
Utiliza a biblioteca python-telegram-bot para escutar comandos e interações de botões. É a camada de interface que conecta o usuário aos métodos do banco de dados e aos modelos lógicos.

models.py (A Lógica de Negócios):
Contém as classes que representam o domínio financeiro.
- Usa Classes Abstratas (ABC) como Transacao e MetaFinanceira
- Garante implementação de métodos obrigatórios (obter_impacto(), exibir_status())
- A classe Carteira gerencia o saldo dinamicamente

banco.py (A Persistência):
A classe DBManager encapsula toda a lógica do SQLite3.
- Cria o arquivo financas.db na pasta data/
- Gerencia as tabelas: transacoes, orcamentos e metas

utils.py (As Ferramentas):
Contém a classe SanitizadorMonetario.
- Usa Expressões Regulares (re)
- Converte valores como "R$ 1.500,50" ou "1500.50" para float seguro

exportador.py (O Relatório):
A classe ExportadorCSV:
- Usa io.StringIO e io.BytesIO
- Gera arquivos CSV diretamente na memória
- Evita arquivos temporários

--------------------------------------------------

🚀 Como Instalar e Rodar na Sua Máquina

1. Pré-requisitos
- Python 3.10 ou superior
- Token de bot do Telegram (via BotFather)

2. Passo a Passo

Clone o repositório:
git clone https://github.com/seu-usuario/porquinBot-ProjetoDeSoftware.git
cd porquinBot-ProjetoDeSoftware

Crie um ambiente virtual:
python -m venv venv

Ativar ambiente:
Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

Crie um arquivo .env:
TELEGRAM_TOKEN=seu_token_aqui

Execute o bot:
python main.py

Saída esperada:
🐷 PorquinhoBot Online e fazendo Oinc Oinc!

--------------------------------------------------

📱 Como Utilizar (Comandos do Telegram)

💰 Movimentações:
- /receita <valor> <categoria>
  Ex: /receita 5000 Salario

- /gasto <valor> <categoria>
  Ex: /gasto 35.50 Pizza

- /remover <ID>

📊 Consultas:
- /extrato
- /id <numero>
- /categoria <nome>
- /data MM/YYYY
- /exportar

🚧 Orçamentos:
- /orcamento <categoria> <valor_teto>
- /status

🎯 Metas:
- /meta <valor_alvo> <Nome da Meta>
- /poupar <ID_da_meta> <valor>
- /status_metas

--------------------------------------------------

💡 Observações

- Projeto baseado em POO
- Código organizado e modular
- Fácil de expandir

🐷 Oinc Oinc! Controle suas finanças de forma simples e divertida!
