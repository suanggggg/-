import asyncio
from httpx import AsyncClient, ASGITransport
from app.main import app

async def main():
    async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
        r = await ac.post('/auth/register', json={'username':'testuser', 'password':'testpass'})
        print('STATUS:', r.status_code)
        try:
            print('JSON:', r.json())
        except Exception:
            print('TEXT:', r.text)

if __name__ == '__main__':
    asyncio.run(main())
