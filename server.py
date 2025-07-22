from flask import Flask, send_file
import psutil
import socket
import webbrowser

app = Flask(__name__)

@app.route('/')
def root():
	return send_file('static/index.html'), 200

@app.route('/landing')
def landing():
	hostname = socket.getfqdn()
	return 'Open in your phone\'s browser: ' + socket.gethostbyname(hostname) + ':8080'

# https://umeey.medium.com/system-monitoring-made-easy-with-pythons-psutil-library-4b9add95a443
@app.route('/memory')
def get_memory_info():
	return {
		"total_memory": psutil.virtual_memory().total / (1024.0 ** 3),
		"available_memory": psutil.virtual_memory().available / (1024.0 ** 3),
		"used_memory": psutil.virtual_memory().used / (1024.0 ** 3),
		"memory_percentage": psutil.virtual_memory().percent
	}

@app.route('/cpu')
def get_cpu_info():
	return {
		"physical_cores": psutil.cpu_count(logical=False),
		"total_cores": psutil.cpu_count(logical=True),
		"processor_speed": psutil.cpu_freq().current,
		"cpu_usage_per_core": dict(enumerate(psutil.cpu_percent(percpu=True, interval=1))),
		"total_cpu_usage": psutil.cpu_percent(interval=1)
	}

@app.route('/load')
def get_load_average():
	load_avg_1, load_avg_5, load_avg_15 = psutil.getloadavg()
	return {
		"load_average_1": load_avg_1,
		"load_average_5": load_avg_5,
		"load_average_15": load_avg_15
	}

if __name__ == '__main__':
	webbrowser.open('http://localhost:8080/landing')
	app.run(host='0.0.0.0', port=8080, debug=True)