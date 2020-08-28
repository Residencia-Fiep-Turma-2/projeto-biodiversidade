from Bio import Bio

#Teste 1
def teste1():
    bio1 = Bio("../data/test2.csv")
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

#Teste 2
def teste2():
    bio2 = Bio("../data/test3.csv")
    #Funcionalidade 1
    print(bio2.media())
    #Funcionalidade 2
    print(bio2.checaNivelTaxonomico())
    #Funcionalidade 3 
    columns_list = ["Responsavel pelo registro", "Data do evento"]
    print(bio2.select_columns(columns_list))
    column = "Numero do registro no portal"
    value = "262289"
    print(bio2.filter_rows(column, value))
    #Funcionalidade 4
    bio2.verifica_lat_long()

#teste1()
teste2()