from collections import Counter
import operator

class Bio:
    sep = ";"

    def __init__(self, path):
        self.path = path
        self.data = self.open()

    def open(self):
        f = open(self.path, "r")
        data = f.readlines()
        f.close()

        for i in range(len(data)):
            data[i] = data[i].replace("\n", "").split(";")
        return data

    def dicionario(self):
        p = x.open()
        cont_linha = -1
        cont_coluna = -1
        cont_faltante = 0
        dicionario = dict()
    
        for linha in p:
            cont_linha += 1
            for coluna in linha:
                cont_coluna += 1
                if coluna == 'Sem Informações':
                    cont_faltante += 1
                    dicionario[cont_faltante] = [cont_linha,cont_coluna]
            cont_coluna = -1
        return dicionario   
    
    def dados_faltantes(self):
        dic_lista = list(x.dicionario().values())
        colunas = []

        for item in dic_lista:
            colunas.append(item[1])
    
        faltantes_coluna = dict(Counter(colunas))    
        sorted_faltantes_coluna = dict(sorted(faltantes_coluna.items(), key=lambda x: x[1]) )
    
        return sorted_faltantes_coluna
    
    def media(self):
        num_col0 = x.open()
        num_col1 = num_col0[0]
        numero_colunas = len(num_col1)
        
        faltantes = x.dados_faltantes()
        soma = 0
        for key in faltantes:
            soma += faltantes[key]
    
        media = soma/numero_colunas
        return media
    
x = Bio('test.csv')

#x.dicionario()
#x.dados_faltantes()
#x.media()



