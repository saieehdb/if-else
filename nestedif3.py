e_date=int(input("enter expected date"))
e_month=int(input("enter expected month"))
e_year=int(input("enter expected year"))
r_date=int(input("enter return date"))
r_month=int(input("enter return month"))
r_year=int(input("enter return year"))
if e_month==r_month and e_year==r_year:
    if e_date>r_date:
        print("no charge")  
    elif e_date<r_date:
        fine="number of days late*15"
        print(fine)