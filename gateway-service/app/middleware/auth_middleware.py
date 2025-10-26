from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
import jwt
import os

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "mysecretkey")

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Allow public endpoints
        public_paths = ["/", "/users/login", "/users/register"]
        if any(request.url.path.startswith(path) for path in public_paths):
            return await call_next(request)

        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.state.user = payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            # Instead of crashing, just return a clear error
            raise HTTPException(status_code=401, detail="Invalid token format")

        return await call_next(request)
