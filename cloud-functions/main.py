from flask import Flask
from flask import Request

from flask import request
from flask import abort

from google.cloud import firestore

import uuid

import json
import geojson
from geojson.geometry import Point
from geojson import Feature

app = Flask(__name__)
db = firestore.Client()

@app.route('/', methods=['POST'])
def main():
    return putPointFeatureEndpoint(request)

def putPointFeatureEndpoint( request:Request ):
    try:
        point_feature:Feature = geojson.loads(request.data.decode("utf-8"))
    except:
        abort(400, 'Couldn\'t parse JSON!!')
    
    persistToFeatureBase(point_feature)
    return "Gotty"

def persistToFeatureBase ( feature:Feature ) :
    feature_doc_ref = db.collection(u'poc_collection').document(str(uuid.uuid4()))
    feature_doc_ref.set(feature)
    return
