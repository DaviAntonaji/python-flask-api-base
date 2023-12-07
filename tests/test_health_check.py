import requests
import pytest

def test_health_check():
    url = 'http://localhost:5001/'  

    try:
        response = requests.get(url)

        assert response.status_code == 200, f"Erro: Status code inesperado: {response.status_code}"

        assert response.elapsed.total_seconds() < 1.0, "Erro: Tempo de resposta muito longo"

    except requests.ConnectionError as e:
        pytest.fail(f"A API não está disponível. Erro: {e}")

    except Exception as e:
        pytest.fail(f"Ocorreu um erro inesperado: {e}")
