weight=int(input("weight plz"))
unit=input("kg or gram")
if unit.upper() == "KG":
    converted = weight*1000
    print(f"weight in gram {converted}")
else:
    converted=weight/1000
    print(f"weight in kg {converted}")


