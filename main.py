from fastapi import FastAPI, WebSocket
import aioredis

app = FastAPI()

# Configuração do Redis
redis = aioredis.from_url("redis://localhost", decode_responses=True)

# Rota WebSocket para o chat
@app.websocket("/chat/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()
    room_channel = f"room:{room_id}"
    
    async def forward_messages(channel):
        async for message in redis.pubsub_iter(channel):
            await websocket.send_text(message["data"])

    # Iniciar o encaminhamento de mensagens para o WebSocket
    await redis.subscribe(room_channel)
    await forward_messages(room_channel)

    try:
        while True:
            data = await websocket.receive_text()
            await redis.publish(room_channel, data)
    except Exception:
        await redis.unsubscribe(room_channel)
        await redis.disconnect()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
