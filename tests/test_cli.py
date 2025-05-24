import unittest
from crm_de_alunos.src import main
from unittest.mock import patch
from io import StringIO

class TestCLI(unittest.TestCase):
    def test_versao(self):
        with patch('sys.argv', ['cli.py', '--versao']), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main.main()
            self.assertIn('CRM de Alunos v0.1.0', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
