from fastapi import FastAPI, Depends
import httpx

app = FastAPI()

client = httpx.AsyncClient()

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down, closing HTTP client...")
    await client.aclose()

async def get_client():
    return client

@app.get("/dog")
async def root(client: httpx.AsyncClient = Depends(get_client)):
    response = await client.get("https://dog.ceo/api/breeds/image/random")
    return response.json()