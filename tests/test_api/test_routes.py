from fastapi.testclient import TestClient

from application.main import app
from models.grupo import Grupo

client = TestClient(app)


def test_retrieve_grupo(mocker):
    grupo_id = 1
    expected_grupo = Grupo(id=grupo_id, nome="teste", nome_exibicao="Teste")
    mocker.patch("repository.grupo.repo_retrieve_grupo", return_value=expected_grupo)

    response = client.get("/api/grupo/1")

    assert response.status_code == 200
