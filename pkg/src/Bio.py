from opencage.geocoder import OpenCageGeocode
import unicodedata
from collections import Counter
import operator

class Bio:
    sep = ";"

    def __init__(self, path):
        self.path = path
        self.data = self.open_()

    def open_(self):
        f = open(self.path, "r")
        data = f.readlines()
        f.close()

        for i in range(len(data)):
            data[i] = data[i].replace("\n", "").split(";")

        return data
    
    #Funcionalidade 1
    def dicionario(self):
        p = self.open_()
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
        dic_lista = list(self.dicionario().values())
        colunas = []

        for item in dic_lista:
            colunas.append(item[1])
    
        faltantes_coluna = dict(Counter(colunas))    
        sorted_faltantes_coluna = dict(sorted(faltantes_coluna.items(), key=lambda x: x[1]) )
    
        return sorted_faltantes_coluna
    
    def media(self):
        num_col0 = self.open_()
        num_col1 = num_col0[0]
        numero_colunas = len(num_col1)
        
        faltantes = self.dados_faltantes()
        soma = 0
        for key in faltantes:
            soma += faltantes[key]
    
        media = soma/numero_colunas
        return media
    #Fim funcionalidade 1
    
    #Funcionalidade 2
    def checaNivelTaxonomico(self):
        #Percorre a lista criada com os dados do CSV e pega os valores da coluna 14 (posicao 13 da lista) para criar a lista com os niveis taxonomico
        #Começando da posicao 1 da lista, pois a primeira linha é o cabeçalho
        nivel_taxonomico = [x[13] for x in self.data[1:]]
        return nivel_taxonomico
    
    #Funcionalidade 3
    def select_columns(self, columns_list):
        if not isinstance(columns_list, list):
            raise TypeError("'columns_list' should be a list")

        col_idx = []
        [col_idx.append(self.data[0].index(col)) for col in columns_list]

        result = []
        for i in range(len(self.data)):
            result_i = []
            [result_i.append(self.data[i][j]) for j in col_idx]
            result.append(result_i)

        return result


    def filter_rows(self, column, value):
        col_idx = self.data[0].index(column)
        clean = self.data[1:]

        result = [[self.data[0]]]
        for i in range(len(clean)):
            if clean[i][col_idx] == value:
                result.append(clean[i])

        return result
    #Fim Funcionalide 3
    
    #Funcionalidade 4
    def verifica_lat_long(self):
        
        #chave necessária para acessar o pacote geocode 
        key = '3f1d63102a214341bc1a293171077d33'
        #inicia o pacote com a chave
        geocoder = OpenCageGeocode(key)

        #para cada linha dos dados teste
        for i in range(len(self.data)):
            #observa latitude e longitude informada
            latitude = (self.data[i][29])
            longitude = (self.data[i][30])
            #se não for o primeiro campo (informações sobre campos)
            if(i > 0):
                #Recebe informações sobre latitude e longitude
                results = geocoder.reverse_geocode(latitude, longitude)
                #Se dentre os resultados, ouver componentes carregados sobre localização
                if('town' in results[0]['components']):
                    
                    #retira pontuação para comparação com base de dados (base de dados sem pontuação)
                    cidade_coord = ''.join((c for c in unicodedata.normalize('NFD', (results[0]['components']['town'])) if unicodedata.category(c) != 'Mn'))
                    #Se cidade informada na base de dados for igual a cidade observada a partir de latitude e longitude
                    if(self.data[i][27] == cidade_coord):
                        print("Igual")
                    else:
                        print("Localização geográfica não correspondente ao informado \n\n")
                        print("Localização informada:" + self.data[i][27] +"\n\n")
                        print("Localização informada por coordenadas: "+ cidade_coord)
                        


###########Testes############
bio = Bio("../data/test.csv")

#Funcionalidade 1
    #print(bio.media())

#Funcionalidade 2
    #Executando a funcao checaNivelTaxonomico mostrando o número do registro
    #result = bio.checaNivelTaxonomico()
    #for i in range(1,len(result) - 1):
    #    print("Nível taxônomico registro " + str(i) + " - " + result[i])

    #Versão simples (printando a lista com os resultados)
    #print(bio.checaNivelTaxonomico())

#Funcionalidade 3 
    #columns_list = ["Responsavel pelo registro", "Data do evento"]
    #print(bio.select_columns(columns_list))

    #column = "Numero do registro no portal"
    #value = "262289"
    #print(bio.filter_rows(column, value))

#Funcionalidade 4
    #bio.verifica_lat_long()
    



