# Credentials for DS Cloud
import os
from dotenv import load_dotenv


class EnvCredentials:
    """
    Carrega variáveis do .env para serem reutilizadas em outros módulos.
    """

    def __init__(self, env_path: str = ".env") -> None:
        load_dotenv(env_path)
        # Aceita tanto "user" quanto "username" no .env
        self.user = os.getenv("user") or os.getenv("username", "<username>")
        self.password = os.getenv("password", "<password>")
        self.base_url = os.getenv("BASEURL", "<BASEURL")
        self.space_url = os.getenv("3DSpaceURL") or os.getenv("3DSPACE", "<3DSpaceURL>")
        self.compass_url = os.getenv("3DCompassURL") or os.getenv("3DCOMPASS", "<3DCompassURL>")
        self.passport_url = os.getenv("3DPassportURL") or os.getenv("3DPASSPORT", "<3DPassportURL>")
        self.tenant = os.getenv("tenant") or os.getenv("TENANT", "<tenant>")
        self.role = os.getenv("ROLE", "<ROLE>")
        self.company = os.getenv("COMPANY", "<COMPANY>")
        self.collaborative_space = os.getenv("COLLABORATIVE_SPACE", "<COLLABORATIVE_SPACE>")
        self.engitems = os.getenv("ENGITEMS", "<ENGITEMS>")


# Instância padrão para importação direta:
creds = EnvCredentials()
