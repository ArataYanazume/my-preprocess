### テスト実行
```
docker compose build
docker compose up -d
docker compose exec my-preprocess pytest functions/char/tests/
 --log-cli-level=DEBUG
```
### 環境設定の更新
```
docker compose exec my-preprocess pip freeze > requirements.txt
```
