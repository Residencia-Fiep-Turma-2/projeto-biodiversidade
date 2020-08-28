from pkg.src.Bio import Bio


def select_columns(data, columns_list):
    if not isinstance(columns_list, list):
        raise TypeError("'columns_list' should be a list")

    col_idx = []
    [col_idx.append(data[0].index(col)) for col in columns_list]

    result = []
    for i in range(len(data)):
        result_i = []
        [result_i.append(data[i][j]) for j in col_idx]
        result.append(result_i)

    return result


def filter_rows(data, column, value):
    col_idx = data[0].index(column)
    clean = data[1:]

    result = [data[0]]
    for i in range(len(clean)):
        if clean[i][col_idx] == value:
            result.append(clean[i])

    return result


def filter_rows_pattern(data, column, pattern):
    import re

    col_idx = data[0].index(column)
    clean = data[1:]

    result = [data[0]]
    for i in range(len(clean)):
        if bool(re.search(pattern, clean[i][col_idx])):
            result.append(clean[i])

    return result
