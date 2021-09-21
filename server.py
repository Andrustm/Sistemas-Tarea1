import grpc
from concurrent import futures
import time
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2
import json

#tambien muere si no existe, creo

class SearchService(pb2_grpc.SearchServicer):

    def __init__(self, *args, **kwargs):
        pass

    def readfile(nombre): #esta wea caga si el string dado es mas largo que el nombre de los productos, supongo
        resultados=[]
        largo=len(nombre)
        with open('productos.json') as products:
            productos= json.load(products)

        for prod in productos["products"]:
            if(prod["name"][:largo] == nombre):
                resultados.append(prod)

        return resultados


    def GetServerResponse(self, request, context):
        message = request.message       # string con el nombre
        print(message)
        result = SearchService.readfile(message)
        print(result)
        search_res = {'product': result} #esta wea se banca una lista creo, no se la bancó, si se la bancó solo soy aweonao

        return pb2.SearchResults(**search_res)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
pb2_grpc.add_SearchServicer_to_server(SearchService(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
