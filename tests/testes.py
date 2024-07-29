import unittest
import requests


# Testes criados com auxílio do ChatGPT para validação, passando apenas o json de input como parâmetro, o que retornou
# testes que testam o funcionamento de todos os métodos da api de forma rápida e produtiva, e também já comentados.
class TestApi(unittest.TestCase):
    baseUrl = 'http://localhost:8000/api/v1/tarefas'

    def setUp(self):
        # Inicializa os dados de teste
        self.dadosTeste = {
            "titulo": "string",
            "descricao": "string",
            "status": "string"
        }
        self.urlTarefa = self.baseUrl

    def testeGet(self):
        resposta = requests.get(self.urlTarefa)
        self.assertEqual(resposta.status_code, 200)
        self.assertIsInstance(resposta.json(), list)  # ou o tipo esperado

    def testePost(self):
        resposta = requests.post(self.urlTarefa, json=self.dadosTeste)
        self.assertEqual(resposta.status_code, 201)  # Supondo que a criação retorna 201
        dadosResposta = resposta.json()
        self.assertEqual(dadosResposta['titulo'], self.dadosTeste['titulo'])
        self.assertEqual(dadosResposta['descricao'], self.dadosTeste['descricao'])
        self.assertEqual(dadosResposta['status'], self.dadosTeste['status'])

    def testePut(self):
        # Primeiro cria uma tarefa para atualizar
        respostaPost = requests.post(self.urlTarefa, json=self.dadosTeste)
        self.assertEqual(respostaPost.status_code, 201)
        tarefaCriada = respostaPost.json()
        idTarefa = tarefaCriada['id']

        # Dados de atualização
        dadosAtualizados = {
            "titulo": "tituloAtualizado",
            "descricao": "descricaoAtualizada",
            "status": "statusAtualizado"
        }
        resposta = requests.put(f'{self.urlTarefa}/{idTarefa}', json=dadosAtualizados)
        self.assertEqual(resposta.status_code, 202)
        dadosResposta = resposta.json()
        self.assertEqual(dadosResposta['titulo'], dadosAtualizados['titulo'])
        self.assertEqual(dadosResposta['descricao'], dadosAtualizados['descricao'])
        self.assertEqual(dadosResposta['status'], dadosAtualizados['status'])

    def testeDelete(self):
        # Primeiro cria uma tarefa para deletar
        respostaPost = requests.post(self.urlTarefa, json=self.dadosTeste)
        self.assertEqual(respostaPost.status_code, 201)
        tarefaCriada = respostaPost.json()
        idTarefa = tarefaCriada['id']

        # Deleta a tarefa
        resposta = requests.delete(f'{self.urlTarefa}/{idTarefa}')
        self.assertEqual(resposta.status_code, 204)  # Supondo que a exclusão retorna 204

        # Verifica se a tarefa foi realmente deletada
        respostaGet = requests.get(f'{self.urlTarefa}/{idTarefa}')
        self.assertEqual(respostaGet.status_code, 404)  # Supondo que uma tarefa inexistente retorna 404


if __name__ == '__main__':
    unittest.main()
