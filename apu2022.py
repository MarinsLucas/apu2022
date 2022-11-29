from urllib import request
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

def pltGraph(candidato, porcentagem):
    plt.barh (candidato, porcentagem, color = 'red')
    plt.ylabel("porcentagem dos votos")
    plt.xlabel("candidatos")
    plt.title("apuração votos válidos")
    plt.show()

def relacaoVotosValidos(votos, n_ele, ben):
    n_ele - ben
    return (sum(votos)/n_ele)*100

def porcReal(q_votos, votos):
    return votos*100/q_votos
    

#adicionar o link para o arquivo json das eleições aqui
data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
json_data =  json.loads(data.content)

candidato = []
partido =  []
votos = []
porcentagem = []
porcentagem_real = []
n_v = int(json_data['vvc'])
abs = int(json_data['a'])
n_ele = int(json_data['e'])
v_brancos = int(json_data['vb'])
v_nulos = int(json_data['vn'])
votoscomunistas = 0

for informacoes in json_data['cand']:
    candidato.append(informacoes['nm'])
    print(informacoes['nm'])
    print(porcReal(n_ele-(abs+v_brancos+v_nulos), int(informacoes['vap'])))
    votos.append(int(informacoes['vap']))
    porcentagem_real = str(porcReal(n_ele-(abs+v_brancos+v_nulos), int(informacoes['vap'])))
    aux = informacoes['pvap']
    porcentagem.append(float(aux.replace(",", ".")))

    if informacoes['nm'] == 'SOFIA MANZANO' or informacoes['nm'] == "LÉO PÉRICLES":
        votoscomunistas += int(informacoes['vap'])

df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns = ['Candidato', 'Nº Votos', 'Porcentagem'])
print(df_eleicao)

print("Votos audidatos:" + str(n_v))
print("Brancos e Nulos: " + str(v_brancos+v_nulos+abs))
print("Votos válidos: " + str(relacaoVotosValidos(votos, n_ele, v_brancos + v_nulos)))

print("Votos em Candidaturas Comunistas (21 e 80): " +  str(votoscomunistas))
pltGraph(candidato, porcentagem)
