import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_question_crud():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as ac:
        # create
        payload = {"title": "What is 2+2?", "body": "Simple math", "choices": "4|3|2|1", "answer": "4", "difficulty": 1}
        r = await ac.post('/questions/', json=payload)
        assert r.status_code == 201
        data = r.json()
        qid = data['id']
        assert data['title'] == payload['title']

        # read
        r2 = await ac.get(f'/questions/{qid}')
        assert r2.status_code == 200
        assert r2.json()['id'] == qid

        # list
        r3 = await ac.get('/questions/')
        assert r3.status_code == 200
        assert any(item['id'] == qid for item in r3.json())

        # update
        up = {"title": "What is 3+3?", "answer": "6"}
        r4 = await ac.put(f'/questions/{qid}', json=up)
        assert r4.status_code == 200
        assert r4.json()['title'] == up['title']

        # delete
        r5 = await ac.delete(f'/questions/{qid}')
        assert r5.status_code == 204
        r6 = await ac.get(f'/questions/{qid}')
        assert r6.status_code == 404
