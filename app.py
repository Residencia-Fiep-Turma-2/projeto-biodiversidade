from pkg_biodiversidade import Bio

#Teste 1
def teste():
    bio1 = Bio.Bio("pkg/data/test3.csv")

    #Funcionalidade 1
    print("Funcionalidade de média de dados faltantes por coluna\n")
    print(bio1.media())

    #Funcionalidade 2
    print("\n")
    print("Funcionalidade de identificação de nível taxonômico por ocorrência\n")
    print(bio1.checaNivelTaxonomico())

    #Funcionalidade 3 
    #filtrandos os valores das colunas "Responsavel pelo registro" e "Data do evento"
    columns_list = ["Responsavel pelo registro", "Data do evento"]
    bio1.select_columns(columns_list)
    #filtrando a linha de acordo com a coluna "Numero do registro no portal" com o valor de "262289"
    column = "Numero do registro no portal"
    value = "262289"
    bio1.filter_rows(column, value)
    #acessando os valores filtrados
    print("\n")
    print("csv filtrado por linhas e colunas \n")
    print(bio1.filtered_data)

    #Funcionalidade 4
    print("\n")
    print("Funcionalidade para checar a longitude e latitude corresponde com a localização\n")
    bio1.verifica_lat_long()

def main():
    teste()

if __name__ == "__main__":
    main() 