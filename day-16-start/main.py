from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name",["pikachu","squirtle"])
table.add_column("Pokemon type",["electric","water"])
table.align = "l"

print(table)
