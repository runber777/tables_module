import pickle
from table_package.table_data import create_table

def load_table(file_path: str):
    """Загружает таблицу из Pickle файла."""
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
        table = create_table()
        table.update(data)
        return table

def save_table(table, file_path: str) -> None:
    """Сохраняет таблицу в Pickle файл."""
    with open(file_path, 'wb') as file:
        pickle.dump(table, file)