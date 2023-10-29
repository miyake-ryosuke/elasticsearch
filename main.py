from fastapi import FastAPI
from elasticsearch import Elasticsearch
import glob

from src import elastic

app = FastAPI()
es = Elasticsearch("http://localhost:9200")
# es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# es.indices.create(index='sample_files')

@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.get("/list")
async def list():
    result = elastic.all_doc()
    return result

# @app.get("/query")
# async def query_info():
#     res = es.cat.indices()
#     return res

@app.get("/insert")
async def insert_info():
    txt_paths = glob.glob('./dummy/**.txt', recursive=True)
    return {'message': 'insert success'}

# @app.get("/close")
# async def query_info():
#     res = es.cat.indices()
#     return res
