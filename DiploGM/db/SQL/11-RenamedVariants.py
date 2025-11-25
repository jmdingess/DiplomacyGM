# Migration from 1.2.1 to 1.3.0
# 11-RenamedVariants.sql


to_rename = [
    ["helladip", "helladip.0.2"],
    ["impdip", "impdip.1.0"],
    ["impdip1.0", "impdip.1.1"],
    ["impdip_a1", "impdip.0.1"],
    ["impdipchaos", "impdip.1.4.chaos"],
    ["impdipchaos_sa", "impdip.1.2.chaos.sa"],
    ["impdipfow", "impdip.1.2.fow"],
    ["maddip", "maddip.0.2"],
    ["peloponnesian_war", "pelopondip.2.2"]
]

db_usages = [
    ["board", "data_file"],
]

SQL_txt = "BEGIN TRANSACTION;"

SQL_format = """
UPDATE {table_name}
SET {column_name} = '{replace}'
WHERE {column_name} = '{search}';
"""

for table, column in db_usages:
    for find, replace in to_rename:
        SQL_txt += SQL_format.format(table_name=table, column_name=column, replace=replace, search=find)

SQL_txt += "\nCOMMIT;\n"

with open("11-RenamedVariants.sql", 'w') as f:
    f.write(SQL_txt)