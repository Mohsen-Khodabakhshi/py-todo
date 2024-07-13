from cryptography.fernet import Fernet

from core.settings import app_settings


class Cryptography:
    key = app_settings.secret_key

    async def encrypt(self, message: str):
        return Fernet(self.key).encrypt(message.encode()).decode()

    async def decrypt(self, message: str):
        return Fernet(self.key).decrypt(message.encode()).decode()


cryptography = Cryptography()
