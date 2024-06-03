import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:10021"
    async with websockets.connect(uri) as websocket:
        message = "Hallo"
        print(f"Sende Nachricht: {message}")
        await websocket.send(message)

if __name__ == "__main__":
    asyncio.run(send_message())
