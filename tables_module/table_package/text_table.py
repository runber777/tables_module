def save_table(table, filename):
    """Сохраняет таблицу в текстовый файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        for col in table.keys():
            file.write(f"{col}: {', '.join(map(str, table[col]))}\n")