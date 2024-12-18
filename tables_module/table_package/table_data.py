def create_table():
    """Создает пустую таблицу в виде словаря."""
    return {}


def add_column(table, column_name, values):
    """Добавляет новый столбец в таблицу."""
    if column_name in table:
        raise ValueError(f"Столбец '{column_name}' уже существует.")
    table[column_name] = values


def get_rows_by_number(table, start, stop=None, copy_table=False):
    """Получение строк из таблицы по номеру."""
    if start < 0 or (stop is not None and stop < start):
        raise IndexError("Номер строки должен быть неотрицательным и stop не может быть меньше start.")

    rows = list(table.values())
    if stop is None:
        stop = start + 1

    selected_rows = {col: rows[col][start:stop] for col in table.keys()}

    if copy_table:
        return selected_rows.copy()
    else:
        return selected_rows  # Возвращаем новое представление


def get_rows_by_index(table, *vals, copy_table=False):
    """Получение строк по значениям в первом столбце."""
    if not vals:
        raise ValueError("Необходимо передать хотя бы одно значение для поиска.")

    first_column = list(table.values())[0]
    selected_rows = {col: [] for col in table.keys()}

    for val in vals:
        if val in first_column:
            index = first_column.index(val)
            for col in table.keys():
                selected_rows[col].append(table[col][index])

    if copy_table:
        return selected_rows.copy()
    else:
        return selected_rows  # Возвращаем новое представление


def get_column_types(table, by_number=True):
    """Получение типов значений в столбцах."""
    types_dict = {}
    for i, col in enumerate(table.keys()):
        if by_number:
            index = i
        else:
            index = col

        types_dict[index] = type(table[col][0]).__name__ if table[col] else 'None'

    return types_dict


def set_column_types(table, types_dict, by_number=True):
    """Задание типов значений в столбцах."""
    for key, value in types_dict.items():
        if by_number:
            col_name = list(table.keys())[key]
        else:
            col_name = key

        if col_name not in table:
            raise KeyError(f"Столбец '{col_name}' не существует.")

        # Преобразуем значения в соответствии с указанным типом
        for i in range(len(table[col_name])):
            if value == 'int':
                table[col_name][i] = int(table[col_name][i])
            elif value == 'float':
                table[col_name][i] = float(table[col_name][i])
            elif value == 'bool':
                table[col_name][i] = bool(table[col_name][i])
            elif value == 'str':
                table[col_name][i] = str(table[col_name][i])
            else:
                raise ValueError(f"Неизвестный тип '{value}' для столбца '{col_name}'.")


def get_values(table, column=0):
    """Получение списка значений из столбца."""
    if isinstance(column, int):
        col_name = list(table.keys())[column]
    else:
        col_name = column

    if col_name not in table:
        raise KeyError(f"Столбец '{col_name}' не существует.")

    return table[col_name]


def get_value(table, column=0):
    """Получение одного значения из столбца."""
    values = get_values(table, column)
    if not values:
        raise IndexError("Столбец пуст.")
    return values[0]


def set_values(table, values, column=0):
    """Задание списка значений для столбца."""
    if isinstance(column, int):
        col_name = list(table.keys())[column]
    else:
        col_name = column

    if col_name not in table:
        raise KeyError(f"Столбец '{col_name}' не существует.")

    if len(values) != len(table[col_name]):
        raise ValueError("Количество значений не совпадает с количеством строк в столбце.")

    table[col_name] = values


def set_value(table, value, column=0):
    """Установка одного значения в столбце."""
    values = get_values(table, column)
    if not values:
        raise IndexError("Столбец пуст.")
    values[0] = value
    set_values(table, values, column)


def print_table(table):
    """Печатает таблицу в удобочитаемом формате."""
    headers = list(table.keys())
    print(" | ".join(headers))
    rows = zip(*[table[header] for header in headers])
    for row in rows:
        print(" | ".join(map(str, row)))