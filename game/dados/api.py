import requests

class FaseService:
    BASE_URL = "http://localhost:5000/api/Fase"

    @staticmethod
    def buscar_todas_fases():
        try:
            response = requests.get(f"{FaseService.BASE_URL}/listar", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar fases: {e}")
            return []

    @staticmethod
    def buscar_detalhes_fase(fase_id):
        try:
            response = requests.get(f"{FaseService.BASE_URL}/{fase_id}", timeout=10)
            if response.status_code == 200:
                return response.json()
            return None
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar fase {fase_id}: {e}")
            return None

    @staticmethod
    def criar_fase(payload):
        try:
            response = requests.post(
                f"{FaseService.BASE_URL}/inserir",
                json=payload,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao salvar fase: {e}")
            return None