
from flask import send_file,make_response,Flask, request, jsonify
import os, json, yaml
from datetime import datetime,timedelta
from functools import wraps, update_wrapper
app = Flask(__name__)
 
def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
        
    return update_wrapper(no_cache, view)

@app.route('/')
#@cachecontrols
@nocache

def checking():
    #yaml_config=open("/home/amogh/Desktop/dash/Viveks/1F/config/calendar_configuration.yaml",'r')
    yaml_config_1=open(loads("/home/amogh/Desktop/dash/Viveks/1F/config/calendar_configuration.yaml",'r'))


    #a = yaml_config.read()
    #b= yaml.load(a)
    c= yaml_config_1
    print c
    return make_response(jsonify({'data_tables':c}))

@app.route('/register')
def register():
    return send_file('static/lib/templates/smartbuildingsRegistration.html')


@app.route('/table_data', methods=['POST'])
def tabledata():   
    data=json.loads(request.data)
    print data
    return make_response(jsonify({'data_tables':data}))


@app.route('/dropdown', methods=['POST'])
def dropdown_data():
    data=json.loads(request.data)
    print data
    return make_response(jsonify({'result':data}))  

def checking():
      config_json = open(os.path.join("/home/amogh/Desktop/dash/Viveks/1F/config", "data", "calendar_configuration.yaml"), "r")
      print config_json



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)



