#!/usr/bin/python

from flask import render_template, Flask,  jsonify, request
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

app = Flask(__name__)

@app.route('/write/<int:pin_no>')
def write(pin_no):
        state = request.args.get('write', 0, type=str)
        if state == 'HIGH':
		GPIO.setup(pin_no,GPIO.OUT)
                GPIO.output(pin_no,GPIO.HIGH)
        else:
                GPIO.output(pin_no,GPIO.LOW)
		GPIO.setup(pin_no,GPIO.IN)
	written = 'SUCCESS'
	return jsonify(result=written)

@app.route('/read/<int:pin_no>')
def read(pin_no):
	GPIO.setup(pin_no,GPIO.IN)
	if GPIO.input(pin_no) == 1:
		read = 'HIGH'
	else:
		read = 'LOW'
	return jsonify(result=read)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3396)
