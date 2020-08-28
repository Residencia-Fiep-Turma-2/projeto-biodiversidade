from opencage.geocoder import OpenCageGeocode
import Bio
import unicodedata

bio = Bio.Bio("../data/test.csv")

key = '3f1d63102a214341bc1a293171077d33'
geocoder = OpenCageGeocode(key)
for i in range(len(bio.data)):
    latitude = (bio.data[i][29])
    longitude = (bio.data[i][30])
    if(i > 0):
        results = geocoder.reverse_geocode(latitude, longitude)
        if('town' in results[0]['components']):
            
            cidade_coord = ''.join((c for c in unicodedata.normalize('NFD', (results[0]['components']['town'])) if unicodedata.category(c) != 'Mn'))
            if(bio.data[i][27] == cidade_coord):
                print("Igual")
            else:
                print("Localização geográfica não correspondente ao informado \n\n")
                print("Localização informada:" + bio.data[i][27] +"\n\n")
                print("Localização informada por coordenadas: "+ cidade_coord)