#importação
import json
import os

#Json
arquivo = 'denuncias.json'

def ler_dados():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f)
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_dados(dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=2)

def gerar_novo_id(denuncias):
    if not denuncias:
        return "1"
    ids = [int(d['id']) for d in denuncias]
    return str(max(ids) + 1)

#criar denuncia
def criar_denuncia():
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data = input("Data: ")
    local = input("Local: ")

    denuncias = ler_dados()
    novo_id = gerar_novo_id(denuncias)

    nova = {
        "id": novo_id,
        "titulo": titulo,
        "descricao": descricao,
        "data": data,
        "local": local,
        "status": "aberta"
    }
    denuncias.append(nova)
    salvar_dados(denuncias)
    print("Denúncia criada com ID:", novo_id)

#Lista de denuncias
def lista_denuncias():
    denuncias = ler_dados()
    if not denuncias:
        print("Nenhuma denúncia registrada")
        return
    for d in denuncias:
        print(f"[{d['id']}] {d['titulo']} - {d['status']}")

#Ver denuncia especifica
def ver_denuncia():
    id = input("ID da denúncia: ")
    denuncias = ler_dados()
    for d in denuncias:
        if d["id"] == id:
            print(json.dumps(d, indent=2, ensure_ascii=False))
            return
    print("Denúncia não encontrada")
