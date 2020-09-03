from pkg_biodiversidade import Bio

#Teste 1
def teste():
    bio1 = Bio.Bio("pkg/data/test.csv")

    #Funcionalidade 1
    print(bio1.media())
    #Funcionalidade 2
    print(bio1.checaNivelTaxonomico())
    #Funcionalidade 3 
    columns_list = ["Responsavel pelo registro", "Data do evento"]
    print(bio1.select_columns(columns_list))
    column = "Numero do registro no portal"
    value = "262289"
    print(bio1.filter_rows(column, value))
    #Funcionalidade 4
    bio1.verifica_lat_long()

def main():
    teste()

if __name__ == "__main__":
    main() 