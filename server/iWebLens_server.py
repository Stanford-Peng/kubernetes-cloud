# -*- coding: utf-8 -*-
"""
REST API
FLASK
"""
from flask import Flask
from flask import request
import json
from object_detection import object_detection

app = Flask(__name__)
#app.config["DEBUG"] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def hello():
    return "<h2>This is iWebLens_server script deisgned by Shubin Peng, student id: 30869048</h2>"

@app.route("/api/detect", methods=['POST'])
def detect_images():
    image = request.get_json()
    data = json.loads(image)
    #data['image']
#    nums_of_thread = 5
#    with concurrent.futures.ThreadPoolExecutor(nums_of_thread) as executor:
#        futures = []
#        for url in wiki_page_urls:
#            futures.append(executor.submit(detect_objects, wiki_page_url=url))
#        for future in concurrent.futures.as_completed(futures):
#            return future.result()
    return detect_objects(data)

def detect_objects(data):   
    result = object_detection.detect_image(data['image'])
    res = {'id':data['id'],
           'objects':result
            }
    return json.dumps(res)
        
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',threaded=True)