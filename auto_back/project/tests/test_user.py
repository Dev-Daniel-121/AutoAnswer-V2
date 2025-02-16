import unittest
import os
from project.models import SistemaUsuarios
from project.services import UserService

class TestUserSystem(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_usuarios.json'
        self.sistema_usuarios = SistemaUsuarios()
        self.sistema_usuarios.json_handler.file_path = self.test_file
        self.user_service = UserService()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_criar_usuario(self):
        self.user_service.criar_usuario(nome='João', sobrenome='Silva', tipo_conta='Aluno', ra='123456789', dg_ra='0', uf_ra='SP')
        usuarios = self.sistema_usuarios.carregar_usuarios()
        self.assertEqual(len(usuarios), 1)
        self.assertIn('1', usuarios)

    def test_atualizar_usuario(self):
        self.user_service.criar_usuario(nome='João', sobrenome='Silva', tipo_conta='Aluno', ra='123456789', dg_ra='0', uf_ra='SP')
        resultado = self.user_service.atualizar_usuario(id_usuario='1', nome='Maria', sobrenome='Santos')
        self.assertTrue(resultado)
        usuarios = self.sistema_usuarios.carregar_usuarios()
        self.assertEqual(usuarios['1'].nome, 'Maria')
        self.assertEqual(usuarios['1'].sobrenome, 'Santos')

    def test_deletar_usuario(self):
        self.user_service.criar_usuario(nome='João', sobrenome='Silva', tipo_conta='Aluno', ra='123456789', dg_ra='0', uf_ra='SP')
        resultado = self.user_service.deletar_usuario(id_usuario='1')
        self.assertTrue(resultado)
        usuarios = self.sistema_usuarios.carregar_usuarios()
        self.assertEqual(len(usuarios), 0)

if __name__ == '__main__':
    unittest.main()