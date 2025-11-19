import pytest
import uuid
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.db import base as db_base


@pytest.mark.asyncio
async def test_assessment_crud():
    # ensure all tables exist (tests run against dev sqlite file)
    db_base.Base.metadata.create_all(bind=db_base.engine)

    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        # create user first
        uname = f"assess_user_{uuid.uuid4().hex[:8]}"
        r = await ac.post('/auth/register', json={'username': uname, 'password':'TestPass123!'})
        assert r.status_code == 201
        user = r.json()
        uid = user['id']

        # create assessment
        payload = {'user_id': uid, 'type': 'mock_interview', 'media_ref': None}
        r2 = await ac.post('/assessments/', json=payload)
        assert r2.status_code == 201
        a = r2.json()
        aid = a['id']

        # read
        r3 = await ac.get(f'/assessments/{aid}')
        assert r3.status_code == 200
        assert r3.json()['id'] == aid

        # list by user
        r4 = await ac.get(f'/assessments/user/{uid}')
        assert r4.status_code == 200
        assert any(it['id'] == aid for it in r4.json())

        # submit a system score
        score = {"technical": 85, "communication": 78}
        r5 = await ac.post(f'/assessments/{aid}/score', json={"system_score": score})
        assert r5.status_code == 200
        updated = r5.json()
        assert updated['id'] == aid
        assert updated['system_score'] == score

        # fetch results endpoint
        r6 = await ac.get(f'/assessments/{aid}/results')
        assert r6.status_code == 200
        assert r6.json().get('system_score') == score
