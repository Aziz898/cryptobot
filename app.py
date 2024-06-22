from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Список криптовалют по умолчанию
cryptocurrencies = ['bitcoin', 'the-open-network']

def get_crypto_price(crypto):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[crypto]['usd']

@app.route('/')
def index():
    return render_template('index.html', cryptocurrencies=cryptocurrencies)

@app.route('/add', methods=['POST'])
def add_crypto():
    crypto = request.form['crypto'].lower()
    if crypto not in cryptocurrencies:
        cryptocurrencies.append(crypto)
    return jsonify(cryptocurrencies)

@app.route('/price/<crypto>', methods=['GET'])
def price(crypto):
    try:
        price = get_crypto_price(crypto)
        return jsonify({'crypto': crypto, 'price': price})
    except KeyError:
        return jsonify({'error': 'Invalid cryptocurrency name'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
