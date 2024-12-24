from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta
app = Flask(__name__)
def get_exchange_rate(date):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json&date={date.strftime('%Y%m%d')}&valcode=USD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]["rate"]
    return None
@app.route("/currency", methods=["GET"])
def currency():
    param = request.args.get("param")
    today = datetime.today()
    if param == "today":
        rate = get_exchange_rate(today)
        if rate:
            return jsonify({"date": today.strftime('%Y-%m-%d'), "currency": "USD", "rate": rate})
        else:
            return jsonify({"error": "Не вдалося отримати курс для сьогоднішнього дня"}), 500
    elif param == "yesterday":
        yesterday = today - timedelta(days=1)
        rate = get_exchange_rate(yesterday)
        if rate:
            return jsonify({"date": yesterday.strftime('%Y-%m-%d'), "currency": "USD", "rate": rate})
        else:
            return jsonify({"error": "Не вдалося отримати курс для вчорашнього дня"}), 500
    else:
        return jsonify({"error": "Використовуйте 'today' або 'yesterday'."}), 400
if __name__ == '__main__':
    app.run(port=8000)