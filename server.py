from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List
from uuid import uuid4

app= FastAPI()

class Musica(BaseModel):
    id: Optional[str] = None
    nome: str
    cantor: str
    estilo: str
    autor: str
    ano_lançamento: int


data : List[Musica] = []

@app.get('/')
async def root():
    return {"mensagem": "rodando"}

@app.get('/musicas')
def listar_musicas():
    return data


@app.get('/musicas/2/{musica_id}')
def obter_musica(musica_id: str):
    for musica in data:
        if musica.id == musica_id:
            return musica
    return{'mensagem': f'musica com id {musica_id} não encontrada'}

@app.post('/musicas')
def add_musica(musica : Musica):
    musica.id = str(uuid4())
    data.append(musica)
    return {'mensagem': f'{musica} adicionada com sucesso'}



@app.delete('/musicas/1/{musica_id}')
def deletar_musica(musica_id: str):
    posicao = -1
    # fazer a busca da posição da musica
    for index, musica in enumerate(data):
        if musica.id == musica_id:
            posicao = index
            break
    if posicao != -1:
            data.pop(posicao)
            return{'mensagem': f'{musica}\n com o id {musica_id} removida com sucesso'}
    else:
        return{'error': f'musica com o id {musica_id}'}
