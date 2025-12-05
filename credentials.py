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
        self.space_url = os.getenv("3DSpaceURL", "<3DSpaceURL>")
        self.compass_url = os.getenv("3DCompassURL", "<3DCompassURL>")
        self.passport_url = os.getenv("3DPassportURL", "<3DPassportURL>")
        self.tenant = os.getenv("tenant", "<tenant>")
        self.role = os.getenv("ROLE", "<ROLE>")
        self.company = os.getenv("COMPANY", "<COMPANY>")
        self.collaborative_space = os.getenv("COLLABORATIVE_SPACE", "<COLLABORATIVE_SPACE>")
        self.engitems = os.getenv("ENGITEMS", "<ENGITEMS>")


# Instância padrão para importação direta:
creds = EnvCredentials()
