from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Variable to store the last received data
last_received_data = None

@app.route('/')
def home():
    return render_template('index.html', data=last_received_data)  # Pass data to the template

@app.route('/send_data', methods=['POST'])
def receive_data():
    global last_received_data  # Use the global variable to store the latest data
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data received'}), 400

        pi_id = data.get('pi_id')
        product_count = data.get('product_count')
        not_ok_count = data.get('not_ok_count')
        shift = data.get('shift')

        # Store received data in the global variable
        last_received_data = {
            'pi_id': pi_id,
            'product_count': product_count,
            'not_ok_count': not_ok_count,
            'shift': shift
        }

        print(f'Received data from {pi_id}: Product Count: {product_count}, Not OK Count: {not_ok_count}, Shift: {shift}')
        return jsonify({'status': 'success', 'message': 'Data received successfully'}), 200

    except Exception as e:
        print("Error processing data:", e)
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
