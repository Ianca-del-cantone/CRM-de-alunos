import cmd

class CRMDeAlunosShell(cmd.Cmd):
    intro = 'Bem-vindo ao CRM de Alunos. Digite help ou ? para listar os comandos.\n'
    prompt = '(crm) '
    alunos = []

    def do_cadastrar(self, arg):
        'Cadastrar um novo aluno: cadastrar <nome> <idade>'
        partes = arg.split()
        if len(partes) < 2:
            print('Uso: cadastrar <nome> <idade>')
            return
        nome = partes[0]
        try:
            idade = int(partes[1])
        except ValueError:
            print('Idade deve ser um número inteiro.')
            return
        self.alunos.append({'nome': nome, 'idade': idade})
        print(f'Aluno {nome} cadastrado com sucesso!')

    def do_listar(self, arg):
        'Listar todos os alunos cadastrados'
        if not self.alunos:
            print('Nenhum aluno cadastrado.')
            return
        for idx, aluno in enumerate(self.alunos, 1):
            print(f"{idx}. Nome: {aluno['nome']}, Idade: {aluno['idade']}")

    def do_sair(self, arg):
        'Sair do programa'
        print('Saindo...')
        return True

def main():
    CRMDeAlunosShell().cmdloop()

if __name__ == "__main__":
    main()
