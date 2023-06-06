from codigo.bytebank import Funcionario

#lucas = Funcionario('Lucas Carvalho', '13/03/2000',1000)
#print(lucas.idade())

def teste_idade():
    Funcionario_teste = Funcionario('Teste', '15/12/2001', 1111)
    print(f'Teste = {Funcionario_teste.idade()}')

teste_idade()