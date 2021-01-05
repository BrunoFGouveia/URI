def normaliza_palavras(lista):
  normaliza = []
  for palavra in lista:
    if palavra.isalpha():
      normaliza.append(palavra.lower())
  return normaliza

def construir_palavra(palavra):
  fatias = []

  for i in range(len(palavra) + 1):
    fatias.append((palavra[:i], palavra[i:]))

  palavras = inserir_letras(fatias)
  palavras += deletando_caracter(fatias)
  palavras += troca_letra(fatias)
  palavras += inverte_letra(fatias)

  return palavras


def inserir_letras(fatias):
  novas_palavras = []

  letras = 'abcdefghijklmnopqrstuvwxyzáâàãéêèẽíîìĩóôõòúûùũç'
  for E, D in fatias:
    for letra in letras:
      novas_palavras.append(E + letra + D)
  return novas_palavras



def corretor(palavra):

  if palavra in palavras_dic:
    return print(palavra.title())
  else:
    candidatos = []

    palavras_geradas = construir_palavra(palavra)

    for i in palavras_geradas:
      if i in palavras_dic:
        candidatos.append(i)

    return candidatos

def deletando_caracter(fatias):
  novas_palavras = []
  for E, D in fatias:
    novas_palavras.append(E + D[1:])
  return novas_palavras


def troca_letra(fatias):
  novas_palavras = []

  letras = 'abcdefghijklmnopqrstuvwxyzáâàãéêèẽíîìĩóôõòúûùũç'

  for E, D in fatias:
    for i in letras:
      novas_palavras.append(E + i + D[1:])

  return novas_palavras


def inverte_letra(fatias):
  novas_palavras = []

  for E, D in fatias:
    if len(D) > 1:
      novas_palavras.append(E + D[1] + D[0] + D[2:])

  return novas_palavras


# define empty list
palavras_dic = []

# open file and read the content in a list
with open('palavras.txt', 'r') as filehandle:
    palavras_dic = [current_place.rstrip() for current_place in filehandle.readlines()]


palavras_dic = normaliza_palavras(palavras_dic)

artigos_sep = set(palavras_dic)



while 1:
  palavra_user = input("Digite uma palavra >> ")
  if palavra_user == '*':
    break
  print(corretor(palavra_user))