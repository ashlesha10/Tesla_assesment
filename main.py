from flask import json
from flask import Response
from flask_cors import CORS
from flask_api import FlaskAPI
APP = FlaskAPI(__name__)
CORS(APP)
@APP.route("https://reqres.in/api/<products>", methods=['GET'])
def get_json_response(products):
    labels_dict = {}
    response_dict = {}
    try:
        with open(filename, 'r') as labels:
            labels_dict = json.load(labels)
        response_dict[STATUS] = "true
        response_dict["labels_mapping"] = labels_dict
        js_dump = json.dumps(response_dict)
        resp = Response(js_dump,status=200,
                        mimetype='application/json')
    except FileNotFoundError as err:
        response_dict = {'error': 'file not found in server'}
        js_dump = json.dumps(response_dict)
        resp = Response(js_dump,status=500,
                        mimetype='application/json')
    except RuntimeError as err:
        response_dict = {'error': 'error occured on server side.
                          Please try again'}
        js_dump = json.dumps(response_dict)
        resp = Response(js_dump, status=500,
                        mimetype='application/json')
    return resp
if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=3001)
