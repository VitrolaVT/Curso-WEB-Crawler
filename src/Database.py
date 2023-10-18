from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from bson import ObjectId

class Database:

    def __init__(self):
        load_dotenv()
        self.Noticiasrecentes = self.connect()

    def connect(self):
        client = MongoClient(os.getenv("DB_URI"))
        db = client["Cursoweb"]
        return db.Noticiasrecentes

#Função de inserção no DB
    def insert(self, data: dict):

        query = {"Title": data["Title"]}
        result = self.Noticiasrecentes.find_one(query, sort=[("Date", -1)])

        if result is None:
            print("Inserção feita com sucesso")
            return self.Noticiasrecentes.insert_one(data)
        else:
            print("Conteúdo já inserido")
            return None

#Função de busca no DB
    def search_id(self, news_id):

        query = {'_id': ObjectId(news_id)}
        result = self.Noticiasrecentes.find_one(query)

        if result is None:
            print("Conteúdo não encontrado")
        else:
            print("Conteúdo encontrado")
            print(result)

if __name__ == "__main__":
    db = Database()

#Para pesquisar uma Notícia específica
    #news_id = ObjectId('Id da noticia')
    #db.search_id(news_id)

