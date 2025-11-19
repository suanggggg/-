import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.db import base as db_base
import uuid


@pytest.mark.asyncio
async def test_register_login_and_me(tmp_path):
    # ensure DB tables exist
    db_base.Base.metadata.create_all(bind=db_base.engine)
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        uname = f"testuser_{uuid.uuid4().hex[:8]}"
        # register
        r = await ac.post('/auth/register', json={"username": uname, "password": "testpass"})
        assert r.status_code == 201
        data = r.json()
        assert data['username'] == uname
        # token via OAuth2 form
        r2 = await ac.post('/auth/token', data={"username": uname, "password": "testpass"})
        assert r2.status_code == 200
        token = r2.json()['access_token']
        # me
        r3 = await ac.get('/auth/me', headers={"Authorization": f"Bearer {token}"})
        assert r3.status_code == 200
        me = r3.json()
        assert me['username'] == uname
        assert me['points_balance'] == 1000
