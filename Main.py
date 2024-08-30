#combining the features into appliction
from features import transaction,sort,add_date,delete_date,sum_amount
transactions=[{"date":"2001-08-28",
            "amount": 500,
             "desc" : "fruit"},{"date":"2001-08-25",
            "amount": 400,
             "desc" : "birds"},{"date":"2001-08-27",
            "amount": 300,
             "desc" : "animal"},{"date":"2001-08-23",
            "amount": 600,
             "desc" : "apple"},{"date":"2001-08-29",
            "amount": 200,
             "desc" : "books"}]


flag =True
while flag:
  print("Expense Tracker App:\n 1.Adding\n 2.Searching\n 3.Sorting\n 4.Deleting\n 5.display\n 6.Stop Application\n 7.sum amount\n")
  choice=int(input("Choose feature: "))
  if choice==1:
    print("-"*50)
    print("adding data")
    print("-"*50)
    print(add_date(transactions))
    print("-"*50)
  elif choice==2:
    print("-"*50)
    print("Searching Data")
    print("-"*50)
    print(transaction(transactions))
    print("-"*50)
  elif choice==3:
    print("-"*50)
    print("Sorting data")
    print("-"*50)
    print(sort(transactions))
    print("-"*50)
  elif choice==4:
    print("-"*50)
    print("deleting data")
    print("-"*50)
    print(delete_date(transactions))
    print("-"*50)
  elif choice==5:
    print("-"*50)
    print(transactions)
    print("-"*50)
  elif choice==6:
    print("-"*50)
    print("Application Stopped")
    flag=False
    print("-"*50)
  elif choice==7:
    print("-"*50)
    print("sum of amount of a given year")
    print(sum_amount(transactions))
    print("-"*50)
  else:
    print("-"*50)
    print("Please enter correct feature")
    print("-"*50)


