def table(columns,data):#fonction qui permet de creer un tableau qui tient compte du nombre de colonne que nous lui donnont

	column_widths=[max(len(str(item)) for item in column) for column in zip (columns,*data)]

	header = '| '.join(header.ljust(width) for header, width in zip (columns,column_widths))

	separator = '+' .join(['-' * width for width in column_widths])

	table = []
	table.append(separator)
	table.append(header)
	table.append(separator)

	for row in data:

		row_date = '| '.join(str(item).ljust(width) for item,width in zip(row,column_widths))

		table.append(row_date)
		table.append(separator)

	return '\n' .join(table)

#Exemple d'utilisation de la fonction
"""

columns =['ID','Nom','Valeur']

av=[(1,'A',10),(2,'B',20),(3,'C',15),]

data=list(av)


table_generate= table(columns,data)
print(table_generate)
"""