

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metric = PrometheusMetrics(app)
metric.info('app_info', 'Application info', version='1.0.3')




@app.route('/')
def index():
    return "Hello World"

@app.route('/monitor-flask')
def monitor_app():
    return "Monitoring Flask"


    
    
    



