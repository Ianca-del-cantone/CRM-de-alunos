import cmd
from src.Infra.Db import Db  
from src.Presentation.Cmd.Controller import Controller

class CRMDeAlunosShell(cmd.Cmd):
    intro = 'Bem-vindo ao CRM de Alunos. Digite help ou ? para listar os comandos.\n'
    prompt = '(crm) '
    db = Db()

    def __init__(self):
        super().__init__()
        self.controller = Controller(self.db)
        self._register_commands()

    def _register_commands(self):
        for attr in dir(self.controller):
            if attr.startswith('do_'):
                method = getattr(self.controller, attr)
                # Cria um wrapper que mantém a referência correta
                def create_wrapper(method):
                    def wrapper(_self, arg):
                        return method(arg)
                    wrapper.__doc__ = method.__doc__
                    return wrapper
                
                setattr(self.__class__, attr, create_wrapper(method))

    def default(self, line):
        print(f"Comando não reconhecido: {line}")
        print("Digite 'help' para ver os comandos disponíveis.")

    def emptyline(self):
        pass  # Não faz nada quando uma linha vazia é digitada

def main():
    try:
        CRMDeAlunosShell().cmdloop()
    except KeyboardInterrupt:
        print("\nSaindo do CRM de Alunos...")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()