## Start Server

```
python3 restServer.py
```

## Curl Commands

### GET

```
curl -X GET  http://localhost:4242/status/976
```

### PUT

```
curl -X PUT --form-string 'body={ "boo": "foo"}' -F 'audio=@/home/path/filename.wav' http://127.0.0.1:4242/order
```