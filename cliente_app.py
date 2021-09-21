import flask
import grpc
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2
import redis
import json
from google.protobuf.json_format import MessageToJson
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

class SearchClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = pb2_grpc.SearchStub(self.channel)

    def get_results(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)

@app.route('/inventory/search', methods=['GET'])
def busqueda():
    if 'q' in request.args:
        busqueda= request.args['q']

        r= redis.Redis(host='localhost', port=6379, db=0)
        resultado = (r.get(busqueda))

        if(resultado!=None):
            products= json.loads(resultado)
            return jsonify(products)

        else:
            client = SearchClient()
            result = client.get_results(busqueda)
            print(result.product[0].name + "*******")
            serialized = MessageToJson(result)
            r.set(busqueda, serialized)
            return serialized
    else:
        return "Error, porfavor especifique la busqueda a realizar"

app.run()