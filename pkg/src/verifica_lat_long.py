#Importa o pacote geocoder que recebe coordenadas e devolve informações correspondentes
from opencage.geocoder import OpenCageGeocode
#Importa a classe base bio
import Bio
#Importa pacote para lidar com acentuação em português 
import unicodedata

#Instância a classe bio com a base de dados de teste
bio = Bio.Bio("../data/test.csv")

#chave necessária para acessar o pacote geocode 
key = '3f1d63102a214341bc1a293171077d33'
#inicia o pacote com a chave
geocoder = OpenCageGeocode(key)

#para cada linha dos dados teste
for i in range(len(bio.data)):
    #observa latitude e longitude informada
    latitude = (bio.data[i][29])
    longitude = (bio.data[i][30])
    #se não for o primeiro campo (informações sobre campos)
    if(i > 0):
        #Recebe informações sobre latitude e longitude
        results = geocoder.reverse_geocode(latitude, longitude)
        #Se dentre os resultados, ouver componentes carregados sobre localização
        if('town' in results[0]['components']):
            
            #retira pontuação para comparação com base de dados (base de dados sem pontuação)
            cidade_coord = ''.join((c for c in unicodedata.normalize('NFD', (results[0]['components']['town'])) if unicodedata.category(c) != 'Mn'))
            #Se cidade informada na base de dados for igual a cidade observada a partir de latitude e longitude
            if(bio.data[i][27] == cidade_coord):
                print("Igual")
            else:
                print("Localização geográfica não correspondente ao informado \n\n")
                print("Localização informada:" + bio.data[i][27] +"\n\n")
                print("Localização informada por coordenadas: "+ cidade_coord)
