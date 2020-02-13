# define
headers = {
    'Access-Control-Allow-Origin': '*'
}

# pytest용 클라이언트
from settings.settings import app
client = app.test_client()
