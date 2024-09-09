from flask import Flask, render_template, request
from .utils import calculate_shipping_cost
from .data import get_shipping_rates, get_location_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']
        package_weight = float(request.form['weight'])
        shipping_rates = get_shipping_rates()
        location_data = get_location_data()
        cost, delivery_estimate = calculate_shipping_cost(origin, destination, package_weight, shipping_rates, location_data)
        return render_template('results.html', cost=cost, delivery_estimate=delivery_estimate)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)