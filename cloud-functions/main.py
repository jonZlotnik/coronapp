from flask import Flask
from flask import Request, Response

from flask import request
from flask import abort

from google.cloud import firestore

import uuid

import json
import geojson
from geojson.geometry import Point
from geojson import Feature, FeatureCollection

app = Flask(__name__)
db = firestore.Client()

@app.route('/', methods=['POST'])
def main():
    return putPointFeatureEndpoint(request)

@app.route('/getData', methods=['GET'])
def getData():
    return getPersistedPoints(request)

def putPointFeatureEndpoint( request:Request ):
    print(request.get_data())
    try:
        point_feature:Feature = geojson.loads(request.data.decode("utf-8"))
    except:
        print(request.data.decode("utf-8"))
        abort(400, 'Couldn\'t parse JSON!!')
    
    persistToFeatureBase(point_feature)
    return "Gotty"

def persistToFeatureBase ( feature:Feature ) :
    feature_doc_ref = db.collection(u'poc_collection').document(str(uuid.uuid4()))
    feature_doc_ref.set(feature)
    return


def getPersistedPoints( request:Request ):
    feature_list = []
    docs = db.collection(u'poc_collection').stream()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
        feature_list.append(doc.to_dict())
    feature_collection = FeatureCollection(feature_list)
    print(feature_collection)
    response_body = geojson.dumps(feature_collection)
    resp = Response(response_body)
    resp.headers['content-type'] = 'application/geo+json'
    return resp