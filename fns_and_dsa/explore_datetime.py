import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current Date and Time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))

    def calculate_future_date(days):
        number_of_days = int(input("Enter a number of days: "))
        future_date = current_date + datetime.timedelta(days=number_of_days)
        return future_date
        print("Future Date: ", future_date.strftime("%Y-%m-%d %H:%M:%S"))

   
