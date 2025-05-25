import httpx

# Shared async HTTP client - reusable between services.

async_client = httpx.AsyncClient()