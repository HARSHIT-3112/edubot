from starlette.middleware.base import BaseHTTPMiddleware
import time
import logging

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = (time.time() - start_time) * 1000
        logging.info(f"{request.method} {request.url.path} completed in {process_time:.2f}ms")
        return response
