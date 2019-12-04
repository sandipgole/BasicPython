try:
    age=int(input("age"))
    print(age)
    income=2000
    tax=income/age
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("age cannot be zero")
# single line comments
'''
multiline comments
'''