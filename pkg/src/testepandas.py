from Bio import Bio

def testePandas():

    bio = Bio("../data/test3.csv", "pandas")
    columns_list = ["Nivel taxonomico"]
    bio.select_columns_pandas(columns_list)
    print(bio.filtered_data)

testePandas()