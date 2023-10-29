from elasticsearch import Elasticsearch

# https://qiita.com/satto_sann/items/8a63761bbfd6542bb9a2

# connect ElasticSearch
es = Elasticsearch("http://localhost:9200")

# confirm ES connection
print(es.info())

index_name = 'students'

def create_index():
    # not index => create index
    if es.indices.exists(index='students'):
        pass
    else:
        # Create index
        mapping = {
            "mappings": {
                "properties": {
                    "name": {"type": "text"},
                    "age": {"type": "long"},
                    "email": {"type": "text"}
                }
            }
        }
        es.indices.create(index=index_name, body=mapping)

def all_doc():
    # es = Elasticsearch("http://localhost:9200")
    # インデックス内の全ドキュメントを検索
    result = es.search(index=index_name, body={"query": {"match_all": {}}})

    # 検索結果のドキュメントを表示
    # for hit in result['hits']['hits']:
    #     print(f"ドキュメントID: {hit['_id']}")
    #     print(f"ドキュメント内容: {hit['_source']}")
    #     print()
    es.close()
    return result
