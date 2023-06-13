# Flask Rest

### Setup Environment

```
python3 -m venv .venv
source .venv/bin/activate
pip install flask
```

### Setup flask app

```
# app.py
from flask import Flask

app = Flask(__name__)

@app.get("/")
def greet():
    return { "message": "Hello World" }
```

```
# Makefile

run:
    flask run --debug
```

### Create API Specification

```
# oas.yaml
openapi: 3.0.3

info:
  title: FLASK REST API
  description: API to learn flask
  version: 1.0.0

paths:
  /stores:
    get:
      summary: Returns a list of store items
      responses:
        '200':
          description: A JSON array of stores
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListStoresSchema'
                
# ...
```

### Implement endpoints

```
@app.get("/stores")
def get_stores():
    return {"stores": stores}
```
