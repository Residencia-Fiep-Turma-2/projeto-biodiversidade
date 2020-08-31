import pytest
from pkg.src.Bio import Bio


@pytest.fixture
def data():
    path = "./pkg/data/test.csv"

    f = open(path, "r")
    csv_data = f.read()
    f.close()

    return path, csv_data


class TestToCsv:
    def test_with_data(self, data):
        bio = Bio(data[0])
        assert bio.to_csv() == data[1]
