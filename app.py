from flask import Flask, jsonify
from RPi import GPIO
from threading import Timer

app = Flask(__name__)

@app.route('/on', methods=['POST'])
def door_on():
    def door_close():
        GPIO.output(7, GPIO.LOW)
        GPIO.cleanup()
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)
        GPIO.output(7, GPIO.HIGH)
        offLED = Timer(5, door_close)
        offLED.start()
        return jsonify(message= 'door has opened')
    except Exception as e:
        print(f'door_on: {e}')
        return jsonify(message= 'door has failed to open')

if __name__ == '__main__':
    try:
        app.run(debug=False, host='0.0.0.0')
    except Exception as e:
        print(f'main: {e}')