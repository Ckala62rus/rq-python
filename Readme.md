#### Run worker with default queue
```bash
rq worker --config rq_conf 
```

#### Run worker with (high default low) queues
```bash
rq worker high default low --config rq_conf 
```

#### Create requirements.txt dependences without hashes
```bash
poetry export --without-hashes -f requirements.txt --output requirements.txt  
```


#### Download all packages for local install
```bash
pip download -d vendor -r requirements.txt
```

#### Install all packages localhost from folder
```bash
pip install --no-index --find-links /vendor -r requirements.txt
```
