from opencage.geocoder import OpenCageGeocode
import unicodedata
from collections import Counter
import operator
import re
class Bio:
    sep = ";"

    def __init__(self, path):
        self.path = path
        self.data = self.open_()
        self.filtered_data = self.data

    def open_(self):
        f = open(self.path, "r")
        data = f.readlines()
        f.close()

        for i in range(len(data)):
            data[i] = data[i].replace("\n", "").split(";")

        return data
    
    #Funcionalidade 1
    
    # dicionario(): gera um dicionário. A chave do dicionário numera cada um dos dados faltantes.
    # Os valores do dicionário são uma lista de dois elementos que corresponde aos índices do elemento faltante na matriz data.
    # O índice '0' corresponde à linha da matriz "data" em que o dado faltante se encontra.
    # O índice '1' corresponde à coluna da matriz "data" em que o dado faltante se encontra.
    
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
    
    # dados_faltantes(): converte os valores do dicionário definido previamente em uma lista (dic_lista)
    # Cada elemento da lista representa as coordenas matriciais dos elementos faltantes
    # O indice [1] de cada sub-elemento da lista representa as colunas
    # Para calcular o número de elementos faltantes por coluna, são contabilizadas as ocorrencias de cada coluna.
    # Exemplo: dic_lista = [[1, 0], [1, 2], [4, 0], [6, 0], [6, 1], [7, 0]]
    # A coluna 0 teve 3 ocorrências, a columa 2 teve 1 ocorrência, e a coluna 1 teve 1 ocorrência, organizando a 
    # saída em um dicionário, obtém-se:
    #          sorted_faltantes_coluna = {2: 1, 1: 1, 0: 4}
    # em que a chave representa o número da coluna e o valor a quantidade de dados faltantes na mesma.
    
    def dados_faltantes(self):
        dic_lista = list(self.dicionario().values())
        colunas = []

        for item in dic_lista:
            colunas.append(item[1])
    
        faltantes_coluna = dict(Counter(colunas))    
        sorted_faltantes_coluna = dict(sorted(faltantes_coluna.items(), key=lambda x: x[1]) )
    
        return sorted_faltantes_coluna
    
    # media(): pega os valores do dicionário definido anteriormente (sorted_faltantes_coluna)
    # cada valor do dicionário representa a quantidade de dados faltantes por coluna
    # soma o total de dodos faltantes por coluna e divide pela quantidade de colunas 
    
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
        ''' Retorna as colunas selecionadas para o conjunto de dados importado
        '''
        # Verifica se o parâmetro columns_list é uma lista, caso contrário
        # exibe erro
        if not isinstance(columns_list, list):
            raise TypeError("'columns_list' should be a list")

        # Obtém de forma iterativa a posição das colunas de interesse
        col_idx = []
        [col_idx.append(self.data[0].index(col)) for col in columns_list]

        # Obtém de forma iterativa os valores das linhas das colunas de
        # interesse mantendo a estrutura padrão dos dados
        result = []
        for i in range(len(self.data)):
            result_i = []
            [result_i.append(self.data[i][j]) for j in col_idx]
            result.append(result_i)

        self.filtered_data = result

    def filter_rows(self, column, value):
        ''' Retorna as linhas que respeitem uma condição conforme coluna==valor
        '''
        # Obtém posição da coluna que está sendo comparada a algum valor
        col_idx = self.data[0].index(column)

        # Remove o cabeçalho
        clean = self.data[1:]

        # Para cada linha verifica se a coluna de interesse é igual ao valor
        # informado, caso positivo captura a linha
        result = [[self.data[0]]]
        for i in range(len(clean)):
            if clean[i][col_idx] == value:
                result.append(clean[i])

        self.filtered_data = result

    def filter_rows_pattern(self, column, pattern):
        ''' Retorna as linhas que respeitem uma condição de expressão regular
        '''
        if not isinstance(column, str):
            raise TypeError("'Column' should be a str type")

        col_idx = self.data[0].index(column)
        clean = self.data[1:]

        result = [self.data[0]]
        for i in range(len(clean)):
            if bool(re.search(pattern, clean[i][col_idx])):
                result.append(clean[i])

        self.filted_data = result
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

    def to_csv(self):
        ''' Transforma os dados do formato matricial para csv
        '''
        data_row = []
        for i in range(len(self.filtered_data)):
            data_row.append(self.sep.join(self.filtered_data[i]))

        result = "\n".join(data_row) + "\n"
        return result

    def write_csv(self, path):
        ''' Exporta o conjunto de dados no formato csv para o caminho informado
        '''
        f = open(path, "w")
        f.write(self.to_csv())
        f.close()
        print("Arquivo exportado")

    def reset_filtered_data(self):
        ''' Remove os filtros aplicados, isto é, filtered_data = data
        '''
        self.filtered_data = self.data

###########Testes############
if __name__ == "__main__":
    bio = Bio(".../data/test.csv")

    #Funcionalidade 1
    print(bio.media())

    #Funcionalidade 2
    #Executando a funcao checaNivelTaxonomico mostrando o número do registro
    result = bio.checaNivelTaxonomico()
    for i in range(1,len(result) - 1):
       print("Nível taxônomico registro " + str(i) + " - " + result[i])

    #Versão simples (printando a lista com os resultados)
    print(bio.checaNivelTaxonomico())

    #Funcionalidade 3 
    columns_list = ["Responsavel pelo registro", "Data do evento"]
    print(bio.select_columns(columns_list))

    column = "Numero do registro no portal"
    value = "262289"
    print(bio.filter_rows(column, value))

    #Funcionalidade 4
    bio.verifica_lat_long()
