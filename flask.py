from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sensor', methods=['POST'])
def sensor_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        temperature = data.get('temperature')
        humidity = data.get('humidity')

        if temperature is None or humidity is None:
            return jsonify({"error": "Invalid data. Make sure temperature and humidity are provided."}), 400

        app.logger.info(f"Received temperature: {temperature}, humidity: {humidity}")
        response = {
            "status": "success",
            "temperature": temperature,
            "humidity": humidity
        }
        return jsonify(response), 200

    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000)