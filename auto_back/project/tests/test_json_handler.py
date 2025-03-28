from project.utils import JSONHandler
import unittest, os#, json

class TestJSONHandler(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_data.json'
        self.json_handler = JSONHandler(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file): os.remove(self.test_file)

    def test_carregar_dados_arquivo_inexistente(self):
        dados = self.json_handler.carregar()
        self.assertEqual(dados, {})

    def test_salvar_e_carregar_dados(self):
        dados_teste = {'chave': 'valor'}
        self.json_handler.salvar(dados_teste)
        dados_carregados = self.json_handler.carregar()
        self.assertEqual(dados_carregados, dados_teste)

    def test_salvar_dados_invalidos(self):
        dados_invalidos = object()
        resultado = self.json_handler.salvar(dados_invalidos)
        self.assertFalse(resultado)

if __name__ == '__main__': unittest.main()