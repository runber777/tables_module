import csv
from table_package.table_data import create_table, add_column


def load_table(file_path: str):
    """Загружает таблицу из CSV файла."""
    table = create_table()
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key, value in row.items():
                if key not in table:
                    add_column(table, key, [])
                table[key].append(value)
    return table

def save_table(table, file_path: str) -> None:
    """Сохраняет таблицу в CSV файл."""
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=table.keys())
        writer.writeheader()
        rows = zip(*table.values())
        for row in rows:
            writer.writerow(dict(zip(table.keys(), row)))