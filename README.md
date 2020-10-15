# setup+logic exec

```
docker-compose up
```

# request

success pattern:  
http://localhost:9004/api/login?id=user1&password=user1

failed pattern:  
http://localhost:9004/api/login?id=user1&password=user2

(reference file)

app/server/api/login.py

# test exec

```
# Windows
run-pytest-watch.bat

# Linux
sh run-pytest.sh
sh run-pytest-watch.sh # watch
```

(reference file)

app/server/test/api/test_login.py
