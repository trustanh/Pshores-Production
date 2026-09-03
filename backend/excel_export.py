from openpyxl import Workbook
2
 
3
def create_production_sheet(orders, summaries):
4
 
5
wb = Workbook()
6
 
7
ws = wb.active
8
 
9
ws.title = "Production Sheet"
10
 
11
ws["A1"] = "Dining Production Sheet"
12
 
13
filename = "ProductionSheet.xlsx"
14
 
15
wb.save(filename)
16
 
17
return filename
