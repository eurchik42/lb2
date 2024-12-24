from flask import Flask, request
app = Flask(__name__)
@app.route("/currency", methods=["GET"])
def get_currency():
    today = request.args.get("today")
    key = request.args.get("key")
    exchange_rate = "USD - 42"
    return f"Курс валют: {exchange_rate}, Параметри: today={today}, key={key}"

# Запуск сервера на порту 8000
if __name__ == '__main__':
    app.run(port=8000)