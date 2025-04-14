### FastAPIの起動
``` sh
uvicorn backends.main:app --reload --host 0.0.0.0 --port 8000
```

#### リクエスト例
```
http://localhost:8000/api/compare?a=5&b=5
```
