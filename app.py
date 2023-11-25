from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
PORT = 3000

API_KEY = 'E4pgENVQYRuznkJovtWDz6ydAiK42F1U'  # API key to use
EXCHANGE_RATE_API = 'https://api.apilayer.com/exchangerates_data/latest'


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = request.args.get('amount')

    try:
        url = f'{EXCHANGE_RATE_API}?base={from_currency}&symbols={to_currency}'
        headers = {
            'apikey': API_KEY
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        if not data['success']:
            return jsonify({'error': 'Exchange rate server error'}), 500

        if not data['rates'].get(to_currency):
            return jsonify({'error': 'Invalid currency'}), 400

        conversion_rate = data['rates'][to_currency]
        converted_amount = float(amount) * conversion_rate

        return jsonify({'result': round(converted_amount, 6)})

    except Exception as e:
        print(e)
        return jsonify({'error': 'Server error'}), 500


# Start the server
if __name__ == '__main__':
    app.run(port=PORT, debug=True)
