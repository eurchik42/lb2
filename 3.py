from flask import Flask, request, jsonify
import dicttoxml

app = Flask(__name__)

@app.route("/currency", methods=["GET"])
def get_currency():
    content_type = request.headers.get("Content-Type")
    exchange_rate = {"currency": "USD", "rate": 42}
    if content_type == "application/json":
        return jsonify(exchange_rate)
    elif content_type == "application/xml":
        xml_data = dicttoxml.dicttoxml(exchange_rate)
        return xml_data, 200, {'Content-Type': 'application/xml'}

    else:
        return "Курс валют: USD "
if __name__ == '__main__':
    app.run(port=8000)