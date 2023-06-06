import pytest
from codigo.bytebank import Funcionario
from pytest import mark

class TestClass:

    @pytest.fixture
    def nome(self):
        return 'Teste'

    @pytest.fixture
    def idade(self):
        return '13/03/2000'

    @pytest.fixture
    def salario(self):
        return 1111

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self,nome,salario):
        # Given-Contexto
        entrada = '13/03/2000'
        esperado = 23
        Funcionario_test = Funcionario(nome, entrada, salario)
        #When-Ação
        resultado = Funcionario_test.idade()
        #Then-desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_apenas_Carvalho(self,salario,idade):
        # Given-Contexto
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'
        lucas = Funcionario(entrada, idade, salario)
        #When-Ação
        resultado = lucas.sobrenome()
        #Then-desfecho
        assert resultado == esperado

    def test_diminuir_o_salarios_dos_diretores_quando_receber_100000_deve_retomar_90000(self,nome,idade):
        #Given-Contexto
        entrada_salario = 100000
        entrada_nome = 'Paulo'
        esperado = 90000
        funcionario_teste = Funcionario(entrada_nome, idade, entrada_salario)
        #When-Ação
        funcionario_teste.decrescimo_salario()
        resultado = 90000
        #then-desfecho
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_deve_retorna_100(self,nome,idade):
        #Given-Contexto
        entrada = 1000
        esperado = 100
        funiconario_test = Funcionario(nome,idade,entrada)
        #When-Ação
        resultado = funiconario_test.calcular_bonus()
        #then-desfecho
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self,nome,idade):
        with pytest.raises(Exception):
            entrada = 100000000  # given

            funconario_teste = Funcionario(nome, idade, entrada)
            resultado = funconario_teste.calcular_bonus()  # when

            assert resultado  # then

