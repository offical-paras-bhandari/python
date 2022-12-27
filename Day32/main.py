# connection = SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,
#                     to_adders="bhandariparash75@gmail.com",
#                     msg="Hello Happy Birthday"
#                     )
# connection.close()

import datetime as dt
import random
import smtplib
from smtplib import SMTP

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    with open("quotes.txt") as file:
        list_quotes = file.readlines()
        random_quotes = list_quotes[random.randint(0, len(list_quotes))]
        my_email = "testingpurpose994@gmail.com"
        password = "testingpurpose994@123"
        with smtplib.SMTP("stmp.google.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="bhandariparash75@gmail.com",
                                msg=f"Hello Happy Birthday\n\n {random_quotes}"
                                )

