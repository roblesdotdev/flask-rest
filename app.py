import uuid

from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "id": uuid.uuid4(),
        "name": "My store",
        "items": [
            {
                "id": uuid.uuid4(),
                "name": "Chair",
                "price": 33.20
            }
        ]
    }
]


@app.get("/store")
def get_store():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"id": uuid.uuid4(),"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<uuid:store_id>/item")
def create_item(store_id):
    request_data = request.get_json()
    for store in stores:
        if store["id"] == store_id:
            new_item = {"id": uuid.uuid4(),"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


@app.get("/store/<uuid:store_id>")
def get_store(store_id):
    for store in stores:
        if store["id"] == store_id:
            return {"store": store}
    return {"message": "Store not found"}, 404


@app.get("/store/<uuid:store_id>/items")
def get_items(store_id):
    for store in stores:
        if store["id"] == store_id:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404
