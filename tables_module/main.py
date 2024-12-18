from table_package import (
    create_table,
    add_column,
    load_csv_table,
    save_csv_table,
    load_pickle_table,
    save_pickle_table,
    save_text_table,
    print_table
)


def main():
    table = create_table()
    add_column(table, "Имя", ["gosha", "yana", "Roman", "Alabai"])
    add_column(table, "Возраст", [14, 18, 35, 34])

    print("Текущая таблица:")
    print_table(table)

    save_csv_table(table, "table.csv")

    loaded_table = load_csv_table("table.csv")
    print("\nЗагруженная таблица из CSV:")
    print_table(loaded_table)

    save_pickle_table(table, "table.pkl")

    loaded_pickle_table = load_pickle_table("table.pkl")
    print("\nЗагруженная таблица из Pickle:")
    print_table(loaded_pickle_table)

    save_text_table(table, "table.txt")


if __name__ == "__main__":
    main()