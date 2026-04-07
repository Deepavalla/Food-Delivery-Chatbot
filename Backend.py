from fastapi import FastAPI, Request
from db_helper import *

app = FastAPI()

@app.post("/")
async def webhook(request: Request):
    data = await request.json()

    intent = data['queryResult']['intent']['displayName']
    parameters = data['queryResult']['parameters']

    if intent == "new.order":
        item = parameters.get("food-item")
        qty = int(parameters.get("number"))
        price = get_price(item)

        total = price * qty
        order_id = insert_order(item, qty, total)

        return {
            "fulfillmentText": f"Order placed! ID: {order_id}, Total: ₹{total}"
        }

    elif intent == "track.order":
        order_id = parameters.get("order_id")
        status = track_order(order_id)

        return {
            "fulfillmentText": f"Your order status is: {status}"
        }

    return {"fulfillmentText": "Sorry, I didn't understand."}
