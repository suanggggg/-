from uvicorn import Config, Server
from app.main import app

if __name__ == '__main__':
    config = Config(app=app, host="127.0.0.1", port=8000, loop="asyncio", lifespan="on")
    server = Server(config)
    server.run()
