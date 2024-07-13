import jwt
from datetime import datetime, timedelta

from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from core.settings import jwt_settings, app_settings


class JWTHandler:
    security: HTTPBearer = HTTPBearer()
    secret_key: str = app_settings.secret_key
    algorithm: str = jwt_settings.algorithm
    payload: dict = {
        "iat": datetime.utcnow(),
    }

    async def encode_user(self, username: str) -> str:
        self.payload.update(
            {
                "exp": datetime.utcnow() + timedelta(minutes=jwt_settings.access_token_expire_minutes),
                "sub": username,
            }
        )
        return jwt.encode(self.payload, self.secret_key, algorithm=self.algorithm)

    async def decode_token(self, token):
        payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        return payload

    async def auth_wrapper(
        self, auth: HTTPAuthorizationCredentials = Security(security)
    ) -> str:
        try:
            payload = await self.decode_token(auth.credentials)
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Signature has expired"
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )
        except KeyError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


jwt_handler = JWTHandler()
