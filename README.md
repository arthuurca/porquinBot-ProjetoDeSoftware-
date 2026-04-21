🐷 porquinhoBot
Um bot para o Telegram desenvolvido em Python que funciona como o seu cofrinho e gerente financeiro pessoal. O porquinhoBot ajuda a registrar receitas, controlar despesas, acompanhar metas e definir tetos de gastos, tudo através de uma interface interativa de botões e comandos simples! E claro, sempre com um amigável "Oinc Oinc!".

⚙️ Como o Código Funciona (Arquitetura)
O projeto foi estruturado utilizando princípios de Programação Orientada a Objetos (POO) e separação de responsabilidades. Aqui está o que cada arquivo faz:

main.py (O Cérebro do Bot): Utiliza a biblioteca python-telegram-bot para escutar comandos e interações de botões. É a camada de interface que conecta o usuário aos métodos do banco de dados e aos modelos lógicos.

models.py (A Lógica de Negócios): Contém as classes que representam o domínio financeiro.

Usa Classes Abstratas (ABC) como Transacao e MetaFinanceira para garantir que classes filhas (Despesa, Receita, MetaSimples) implementem métodos obrigatórios (como obter_impacto() e exibir_status()).

A classe Carteira gerencia o saldo dinâmico agregando transações.

banco.py (A Persistência): A classe DBManager encapsula toda a lógica do SQLite3. Ela cria o arquivo financas.db na pasta data/ e gerencia as tabelas transacoes, orcamentos e metas.

utils.py (As Ferramentas): Contém a classe SanitizadorMonetario. Ela usa Expressões Regulares (re) para limpar os valores digitados pelo usuário (ex: converte "R$ 1.500,50" ou "1500.50" perfeitamente para um float seguro).

exportador.py (O Relatório): A classe ExportadorCSV usa io.StringIO e io.BytesIO para gerar o arquivo CSV de extrato diretamente na memória, sem precisar criar arquivos temporários no disco.

🚀 Como Instalar e Rodar na Sua Máquina
1. Pré-requisitos
Python 3.10 ou superior.

Um token de bot do Telegram (Crie o seu conversando com o @BotFather no Telegram).

2. Passo a Passo
Clone este repositório:

Bash
git clone https://github.com/seu-usuario/porquinBot-ProjetoDeSoftware.git
cd porquinBot-ProjetoDeSoftware
Crie um ambiente virtual para isolar as bibliotecas (recomendado):

Bash
python -m venv venv
# Para ativar no Windows: venv\Scripts\activate
# Para ativar no Linux/Mac: source venv/bin/activate
Instale as dependências necessárias:

Bash
pip install -r requirements.txt
Crie um arquivo chamado .env na raiz do projeto e insira o seu token do Telegram lá dentro:

Snippet de código
TELEGRAM_TOKEN=seu_token_gerado_no_botfather_aqui
Inicie o bot:

Bash
python main.py
Se tudo der certo, você verá a mensagem no terminal: 🐷 PorquinhoBot Online e fazendo Oinc Oinc!

📱 Como Utilizar (Comandos do Telegram)
Abra o chat com o seu bot no Telegram e use os comandos abaixo ou clique no menu interativo enviado com /start.

💰 Movimentações:

/receita <valor> <categoria> - Guarda um dinheirinho no cofre (Ex: /receita 5000 Salario).

/gasto <valor> <categoria> - Registra uma despesa (Ex: /gasto 35.50 Pizza).

/remover <ID> - Apaga um registro caso tenha digitado errado.

📊 Consultas:

/extrato - Mostra o saldo atual e as últimas transações.

/id <numero> - Busca os detalhes de uma transação específica.

/categoria <nome> - Lista todos os gastos e ganhos de uma categoria.

/data MM/YYYY - Filtra o seu histórico por mês e ano.

/exportar - O bot envia um arquivo .csv com todos os seus dados.

🚧 Orçamentos e Limites:

/orcamento <categoria> <valor_teto> - Define o máximo que você quer gastar em algo.

/status - Mostra se você está dentro do limite nos seus orçamentos.

🎯 Metas:

/meta <valor_alvo> <Nome da Meta> - Cria um novo objetivo financeiro.

/poupar <ID_da_meta> <valor> - Deposita dinheiro na sua meta.

/status_metas - Acompanha a porcentagem de conclusão dos seus sonhos!
