# gamify discrete math textbook
# 1 chapter is (12 Chapters total)
# add up sections to compute potential levels
# 1 problem is progress


#sections
# Ch 01 - 3 
# Ch 02 - 5
# Ch 03 - 4
# Ch 04 - 8
# Ch 05 - 9
# Ch 06 - 4
# Ch 07 - 4
# Ch 08 - 5
# Ch 09 - 9
# Ch 10 - 7
# Ch 11 - 5
# Ch 12 - 3

print("Hello World")
print("The number of chapters is", 12)
print("The number of sections is", 3+5+4+8+9+4+4+5+9+7+5+3)
print("The number of problems is", )
print("The levels are generated by section :) ")

print("A table of the sections by level is shown below")

from prettytable import PrettyTable 
 
# Specify the Column Names while initializing the Table 
myTable = PrettyTable(["Chapter", "Section", "Sum"]) 
 
# Add rows 
myTable.add_row(["Chapter 01", "03 sections", "03"]) 
myTable.add_row(["Chapter 02", "05 sections", "08"]) 
myTable.add_row(["Chapter 03", "04 sections", "12"]) 
myTable.add_row(["Chapter 04", "08 sections", "20"]) 
myTable.add_row(["Chapter 05", "09 sections", "29"]) 
myTable.add_row(["Chapter 06", "04 sections", "33"]) 
myTable.add_row(["Chapter 07", "04 sections", "37"]) 
myTable.add_row(["Chapter 08", "05 sections", "42"]) 
myTable.add_row(["Chapter 09", "09 sections", "51"]) 
myTable.add_row(["Chapter 10", "07 sections", "58"]) 
myTable.add_row(["Chapter 11", "05 sections", "63"]) 
myTable.add_row(["Chapter 12", "03 sections", "66"]) 
 
print(myTable)
lvl = int(12)
star = int(66)
pt = int(193)
print("My current progress is level",lvl,"with",star,"stars and",pt,"points!")