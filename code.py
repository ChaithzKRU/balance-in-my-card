import datetime
import calendar

balance = int(input('Enter the balance available: '))
interest_rate = float(input('interest rate (yearly): ')) * .01
monthly_payment = int(input('Monthly Payment: '))

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1] #returns no. od days in the month
days_till_end_month = days_in_current_month - today.day

start_date = today + datetime.timedelta(days = days_till_end_month + 1)
end_date = start_date

while balance > 0:
    interest_charge = (interest_rate/12) * balance
    balance += interest_charge
    balance -= monthly_payment

    balance = round(balance, 2)
    if balance<0:
        balance = 0

    print('Date: ' + str(end_date) + " " + 'Remaining Balance: ' + str(balance))
    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1] #returns no. od days in the month
    end_date = end_date + datetime.timedelta(days = days_in_current_month)
