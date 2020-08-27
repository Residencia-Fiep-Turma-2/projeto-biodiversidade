from Bio import Bio

def checaNivelTaxonomico():
    bio = Bio("../data/test.csv")
    nivel_taxonomico = [x[13] for x in bio.data[1:]]
    return nivel_taxonomico

#Executando a funcao checaNivelTaxonomico mostrando o número do registro
result = checaNivelTaxonomico()
for i in range(1,len(result) - 1):
    print("Nível taxônomico registro " + str(i) + " - " + result[i])

#Versão simples (printando a lista com os resultados)
print(checaNivelTaxonomico())