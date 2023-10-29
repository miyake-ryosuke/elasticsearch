from jose import JWTError, jwt
from fastapi import HTTPException

JWT_KEY = "12345"

class authJwt():
    secret_key = JWT_KEY
    def jwt_encode(self, payload):
        return jwt.encode(payload, self.secret_key, algorithm="HS256")

    def jwt_decode(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except JWTError:
            raise HTTPException(status_code=404, detail="jwt is not valid")

