while True:
  dígito,valor=map(str,input().split())

  if dígito == "0" and valor == "0":
    break
  aux = 0
  valor = list(valor)
  lista_final = []
  lista=[]
  
  for i in range(len(valor)):
    if dígito != valor[i]:
      lista.append(int(valor[i]))
      

  for i in lista:
    if aux == 0:
      if i != 0:
        lista_final.append(i)
        aux+= 1
    else:
      lista_final.append(i)
      aux+= 1
      
  soma = 0
  for i in range(len(lista)):
    soma+= lista[i]
  if soma == 0:
    print("0")
  else:
    for i in lista_final:
      print(i,end= "".strip())
    print()