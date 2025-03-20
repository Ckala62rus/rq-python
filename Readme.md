#### Run worker with default queue
```bash
rq worker --config rq_conf 
```

#### Run worker with (high default low) queues
```bash
rq worker high default low --config rq_conf 
```

# Создание requirements.txt экспорта зависимостей без хэшей
poetry export --without-hashes -f requirements.txt --output requirements.txt  
