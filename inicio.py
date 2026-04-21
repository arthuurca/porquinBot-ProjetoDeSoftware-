class Colaborador:
    def __init__(self, id, nome, cpf, cargo, email, telefone, departamento, data_nascimento, ano_admissao):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.email = email
        self.telefone = telefone
        self.departamento = departamento
        self.data_nascimento = data_nascimento
        self.ano_admissao = ano_admissao
        self.em_ferias = False
        self.data_retorno = None
class menuInterativo:
    def __init__(self, bot):
        self.bot = bot

    def menu(self):
        while True:
            print("\nMenu Interativo do BotRhEla")
            print("1. Consultar Perfil")
            print("2. Listar Colaboradores por Departamento")
            print("3. Contatos Rápidos")
            print("4. Status de Férias")
            print("5. Aniversariantes do Mês")
            print("6. Contratações por Ano")
            print("7. Mural de Vagas")
            print("8. Buscar por CPF")
            print("9. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                nome = input("Digite o nome de nosso colaborador: ")
                perfil = self.bot.consulta_perfil(nome)
                if perfil:
                    print(f"ID: {perfil['id']}, Nome: {perfil['nome']}, Cargo: {perfil['cargo']}")
                else:
                    print("Colaborador não encontrado.")
            elif escolha == '2':
                departamento = input("Digite o nome do departamento: ")
                colaboradores = self.bot.lista_departamento(departamento)
                if colaboradores:
                    print(f"Colaboradores no departamento {departamento}:")
                    for c in colaboradores:
                        print(f"{c.nome} - {c.cargo}\n")
                else:
                    print("Departamento não encontrado ou sem colaboradores ativos.")
            elif escolha == '3':
                nome = input("Digite o nome do colaborador: ")
                contato = self.bot.contatos_rapidos(nome)
                if contato:
                    print(f"Email: {contato['email']}, Telefone: {contato['telefone']}")
                else:
                    print("Colaborador não encontrado.")
            elif escolha == '4':
                nome = input("Digite o nome do colaborador: ")
                status = self.bot.status_ferias(nome)
                if status:
                    print(f"Status: {status['status']}")
                    if 'retorno' in status:
                        print(f"Data de retorno: {status['retorno']}")
                else:
                    print("Colaborador não encontrado.")
            elif escolha == '5':
                mes = input("Digite o mês (1-12): ")
                aniversariantes = self.bot.aniversariantes_mes(int(mes))
                if aniversariantes:
                    print("Aniversariantes do mês:")
                    for c in aniversariantes:
                        print(f"{c.nome} - {c.data_nascimento}")
                else:
                    print("Nenhum aniversariante encontrado.")
            elif escolha == '6':
                ano = input("Digite o ano: ")
                contratados = self.bot.ano_contratacao(ano)
                if contratados:
                    print(f"Contratações em {ano}:")
                    for c in contratados:
                        print(f"{c.nome} - {c.cargo}")
                else:
                    print("Nenhuma contratação encontrada.")
            elif escolha == '7':
                vagas = self.bot.mural_vagas()
                if vagas:
                    for v in vagas:
                        print(f"{v.titulo} - {v.descricao}")
                else:
                    print("Nenhuma vaga disponível.")
            elif escolha == '8':
                cpf = input("Digite o CPF: ")
                colaborador = self.bot.busca_cpf(cpf)
                if colaborador:
                    print(f"Nome: {colaborador.nome}, Cargo: {colaborador.cargo}")
                else:
                    print("Colaborador não encontrado.")
            elif escolha == '9':
                print("Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.colaboradores = []

    def adicionar_colaborador(self, colaborador):
        self.colaboradores.append(colaborador)

    def listar_ativos(self):
        return [c for c in self.colaboradores if not c.em_ferias]

class Vaga:
    def __init__(self, titulo, descricao, departamento):
        self.titulo = titulo
        self.descricao = descricao
        self.departamento = departamento

class BotRhEla:
    def __init__(self):
        self.colaboradores = []
        self.departamentos = {}
        self.vagas = []

    def consulta_perfil(self, nome):
        for c in self.colaboradores:
            if c.nome.lower() == nome.lower():
                return {'id': c.id, 'nome': c.nome, 'cargo': c.cargo}
        return None

    def lista_departamento(self, departamento):
        if departamento in self.departamentos:
            return self.departamentos[departamento].listar_ativos()
        return []

    def contatos_rapidos(self, nome):
        for c in self.colaboradores:
            if c.nome.lower() == nome.lower():
                return {'email': c.email, 'telefone': c.telefone}
        return None

    def status_ferias(self, nome):
        for c in self.colaboradores:
            if c.nome.lower() == nome.lower():
                if c.em_ferias:
                    return {'status': 'Em férias', 'retorno': c.data_retorno}
                else:
                    return {'status': 'Trabalhando'}
        return None

    def aniversariantes_mes(self, mes):
        aniversariantes = []
        for c in self.colaboradores:
            if c.data_nascimento.split('/')[1] == str(mes).zfill(2):
                aniversariantes.append(c)
        return aniversariantes

    def ano_contratacao(self, ano):
        contratados = []
        for c in self.colaboradores:
            if str(c.ano_admissao) == str(ano):
                contratados.append(c)
        return contratados

    def mural_vagas(self):
        return self.vagas

    def busca_cpf(self, cpf):
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        for c in self.colaboradores:
            if c.cpf == cpf_limpo:
                return c
        return None

    def adicionar_colaborador(self, colaborador):
        self.colaboradores.append(colaborador)
        if colaborador.departamento not in self.departamentos:
            self.departamentos[colaborador.departamento] = Departamento(colaborador.departamento)
        self.departamentos[colaborador.departamento].adicionar_colaborador(colaborador)

    def adicionar_vaga(self, vaga):
        self.vagas.append(vaga)

    def menu_interativo(self):
        asdf


if __name__ == "__main__":
    bot = BotRhEla()

    
    