class Table:
    def __init__(self, field_names, rows):
        self.field_names = field_names
        self._rows = rows

def create_table():
    field_names = ["Name", "Age", "City"]
    rows = [
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "Chicago"]
    ]
    return Table(field_names, rows)

def display_table_with_loops(table):
    # Get the field names and rows
    field_names = table.field_names
    rows = table._rows

    # Print the field names
    for field in field_names:
        print(f"{field}\t", end="")
    print()

    # Print a separator
    for _ in field_names:
        print("--------", end="")
    print()

    # Print the rows
    for row in rows:
        for item in row:
            print(f"{item}\t", end="")
        print()

# Create and display the table
table = create_table()
display_table_with_loops(table)