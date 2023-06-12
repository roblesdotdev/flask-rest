from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "Chair",
                "price": 33.20
            }
        ]
    }
]


@app.get("/store")
def get_store():
    return {"stores": stores}

