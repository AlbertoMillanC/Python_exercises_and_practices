from datetime import date

today = date(2022, 10, 5)
print (f"Name Month", today.strftime("%B"))
print (f"name Month reduce", today.strftime("%b"))