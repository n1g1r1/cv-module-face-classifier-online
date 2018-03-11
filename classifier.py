# IMPORTS.
import requests		# sending requests.
import json 		# json data actions.
import numpy as np  # checking data type.

class NumPyArangeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist() # or map(int, obj)
        return json.JSONEncoder.default(self, obj)

def classify(recognition_server_api_url, image_np):

    data = {}
    data["image"]= json.dumps(image_np.tolist())
    data["mode"]= "predict"
    response = requests.post(recognition_server_api_url, json = data)
    return response.json()["label"], float(response.json()["probability"])
