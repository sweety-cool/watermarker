import base64
import json
import os
from flask import Flask, request
from google.cloud import storage
import logging
from PIL import Image, ImageDraw, ImageFont




app = Flask(__name__)
port = int(os.environ.get("PORT", 8080))


@app.route("/",methods=["POST"])
def main():
     logging.warning("hello world")
     return ""
     envelope = request.get_json()
     if not envelope:
        msg = "no Pub/Sub message received"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

     if not isinstance(envelope, dict) or "message" not in envelope:
        msg = "invalid Pub/Sub message format"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400
     
            # Decode the Pub/Sub message.

     pubsub_message = envelope["message"]
     if isinstance(pubsub_message, dict) and "data" in pubsub_message:
         try:
            data = json.loads(base64.b64decode(pubsub_message["data"]).decode())
            print("data",data)
            print("name", {data.name})
            print("bucket", {data.bucket})
         except Exception as e:
            msg = (
                "Invalid Pub/Sub message: "
                "data property is not valid base64 encoded JSON"
            )
            print(f"error: {e}")
            print("name", {data.name})
            print("bucket", {data.bucket})
            return f"Bad Request: {msg}", 400
         
    # Validate the message is a Cloud Storage event.
     if not data["name"] or not data["bucket"]:
            msg = (
                "Invalid Cloud Storage notification: "
                "expected name and bucket properties"
            )
            print(f"error: {msg}")
            print("name", {data.name})
            print("bucket", {data.bucket})
            return f"Bad Request: {msg}", 400
            
     try:
        im = Image.open(data)
        width, height = im.size
        draw = ImageDraw.Draw(im)
        text = "© Sweety"
        fontSize = round(min(width, height) * 0.1)
        font = ImageFont.truetype('font.ttf', fontSize)
        textwidth, textheight = draw.textsize(text, font)
        margin = 20
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x, y), text, font=font)
        im.save('watermark.jpg')

        return ("", 204)

     except Exception as e:
            print(f"error: {e}")
            return ("", 500)
     
    #  return ("", 500)

if __name__ == '__main__':
    app.run(debug=True, port=port, host="0.0.0.0")

