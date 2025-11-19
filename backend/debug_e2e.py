import time
import httpx

BASE = 'http://127.0.0.1:8000'

def main():
    username = f"e2e_user_{int(time.time())}"
    password = "TestPass123!"
    print('Registering user:', username)
    try:
        r = httpx.post(f"{BASE}/auth/register", json={"username": username, "password": password})
        print('REGISTER status:', r.status_code)
        try:
            print('REGISTER body:', r.json())
        except Exception:
            print('REGISTER text:', r.text)
    except Exception as e:
        print('REGISTER error:', e)
        return

    # token via OAuth2 form
    try:
        r2 = httpx.post(f"{BASE}/auth/token", data={"username": username, "password": password})
        print('TOKEN status:', r2.status_code)
        try:
            print('TOKEN body:', r2.json())
        except Exception:
            print('TOKEN text:', r2.text)
    except Exception as e:
        print('TOKEN error:', e)
        return

    if r2.status_code != 200:
        print('Token request failed, aborting')
        return

    token = r2.json().get('access_token')
    if not token:
        print('No access_token in response')
        return

    # me
    try:
        headers = {"Authorization": f"Bearer {token}"}
        r3 = httpx.get(f"{BASE}/auth/me", headers=headers)
        print('ME status:', r3.status_code)
        try:
            print('ME body:', r3.json())
        except Exception:
            print('ME text:', r3.text)
    except Exception as e:
        print('ME error:', e)

if __name__ == '__main__':
    main()
