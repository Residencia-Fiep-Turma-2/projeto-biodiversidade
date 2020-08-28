from Bio import Bio

def checaNivelTaxonomico():
    bio = Bio("../data/test.csv")
    #Percorre a lista criada com os dados do CSV e pega os valores da coluna 14 (posicao 13 da lista) para criar a lista com os niveis taxonomico
    #Começando da posicao 1 da lista, pois a primeira linha é o cabeçalho
    nivel_taxonomico = [x[13] for x in bio.data[1:]]
    return nivel_taxonomico

#Executando a funcao checaNivelTaxonomico mostrando o número do registro
result = checaNivelTaxonomico()
for i in range(1,len(result) - 1):
    print("Nível taxônomico registro " + str(i) + " - " + result[i])

#Versão simples (printando a lista com os resultados)
print(checaNivelTaxonomico())