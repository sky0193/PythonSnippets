import asyncio
import websockets

async def receive_message(websocket, path):
    async for message in websocket:
        print(f"Empfangene Nachricht: {message}")

async def main():
    server = await websockets.serve(receive_message, "localhost", 10021)
    print("Server läuft auf Port 10021")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
