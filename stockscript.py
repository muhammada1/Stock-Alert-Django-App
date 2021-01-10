import os



def main():
    from django.db import models
    from main.models import WatchList, Stock
    from django.contrib.auth.models import User

    import yfinance as yf
    import datetime as dt
    from pandas_datareader import data as pdr
    import time
    yf.pdr_override()


    import smtplib
    import imghdr
    from email.message import EmailMessage

    EMAIL_ADDRESS = ''
    EMAIL_PASSWORD = ''

    msg = EmailMessage()

    start = dt.datetime(2020, 12, 29)
    now = dt.datetime.now()

    for ls in WatchList.objects.all():
        for itm in ls.stock_set.all():
            df = pdr.get_data_yahoo(str(itm), start, now)
            currentClose = df["Adj Close"][-1]
            watchlistid = itm.watchlist_id
            userid = WatchList.objects.get(id=watchlistid).user_id
            usermail = User.objects.get(id=userid).email
            print(usermail)
            
            msg['Subject'] = 'Alert on '+ str(itm) +'!'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = str(usermail)
            
            message = str(itm) + " has hit the price of " + str(currentClose)
            msg.set_content(message)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            
            del msg['Subject']
            del msg['From']
            del msg['To']
            
            


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockalert.settings')
    import django
    django.setup()
    main()

