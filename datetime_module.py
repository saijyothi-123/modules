import datetime
# print(datetime.datetime.today())
# present_date=datetime.datetime.now()
# print(present_date)
# formatted_date=present_date.strftime("%A/%B/%y")
# print(formatted_date)
# print(type(formatted_date))
# print(datetime.date.today()
def timeConversion(s):
    from datetime import datetime
    return datetime.strftime(datetime.strptime(s, "%I:%M:%S%p"), "%H:%M:%S")




# import datetime
# now=datetime.datetime.now()
# other=datetime.datetime(2020,7,20,22,56)
# print(now-other)



# future_date=present_date+timedelta(days=1095)
# print(type(future_date))
# print("future_date_3years:",str(future_date))
# print(future_date-present_date)


