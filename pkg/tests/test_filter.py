import pytest
import pandas as pd
from pkg.src import utils
from pkg.src.Bio import Bio
from pkg.src.filters import *


@pytest.fixture
def data():
    data = Bio("./pkg/data/test.csv").data
    pd_data = pd.read_csv("./pkg/data/test.csv", sep=";")
    return data, pd_data


class TestSelectColumns:
    def test_single_column(self, data):
        columns_list = ["Responsavel pelo registro"]
        assert select_columns(data[0], columns_list) == utils.select_columns(
            data[1], columns_list)

    def test_multiple_columns(self, data):
        columns_list = ["Responsavel pelo registro", "Data do evento"]
        assert select_columns(data[0], columns_list) == utils.select_columns(
            data[1], columns_list)

    def test_non_match_one_column(self, data):
        columns_list = ["x"]
        with pytest.raises(ValueError):
            select_columns(data[0], columns_list)

    def test_non_match_two_columns(self, data):
        columns_list = ["x", "y"]
        with pytest.raises(ValueError):
            select_columns(data[0], columns_list)

    def test_non_match_one_of_columns(self, data):
        columns_list = ["Responsavel pelo registro", "y"]
        with pytest.raises(ValueError):
            select_columns(data[0], columns_list)

    def test_type_of_input_is_not_list(self, data):
        columns_list = "Responsavel pelo registro"
        with pytest.raises(TypeError):
            select_columns(data[0], columns_list)


class TestFilterRows:
    def test_single_return(self, data):
        column = "Numero do registro no portal"
        value = "262289"
        assert filter_rows(data[0], column, value) == utils.filter_rows(
            data[1], column, value)

    def test_multiples_return(self, data):
        column = "Nome da base de dados"
        value = "Sistema de Autorização e Informação em Biodiversidade."
        assert filter_rows(data[0], column, value) == utils.filter_rows(
            data[1], column, value)

    def test_no_match_return(self, data):
        column = "Nome da base de dados"
        value = "x"
        assert filter_rows(data[0], column, value) == utils.filter_rows(
            data[1], column, value)

    def test_non_match_column(self, data):
        with pytest.raises(ValueError):
            filter_rows(data, "non_exist", "1245")
