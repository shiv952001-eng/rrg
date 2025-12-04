OPENAI_API_KEY = "demo-key-for-testing"

from fastapi import FastAPI
from aiavatar.adapter.websocket.server import AIAvatarWebSocketServer
import uvicorn

aiavatar_app = AIAvatarWebSocketServer(
    openai_api_key=OPENAI_API_KEY,
    volume_db_threshold=-30,
    debug=True
)

app = FastAPI()
router = aiavatar_app.get_websocket_router()
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "AI Avatar WebSocket Server", "status": "ready"}

if __name__ == "__main__":
    print("\nAI Avatar WebSocket Server Running")
    print("http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
