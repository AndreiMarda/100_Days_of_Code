##################### Extra Hard Starting Project ######################
import smtplib
import pandas
import datetime as dt
from random import choice

MY_EMAIL = "example@gmail.com"
MY_PASSWORD = "vexnarxlphojwuszh"

# 1. Update the birthdays.csv
csv_file = "birthdays.csv"
df = pandas.read_csv(csv_file)

mom_dict={
    "name": "Mom",
    "email": "Mom@gmail.com",
    "year": 1970,
    "month": 6,
    "day": 18,
}
dad_dict={
    "name": "Dad",
    "email": "Dad@gmail.com",
    "year": 1970,
    "month": 2,
    "day": 19,
}
another_dict = [mom_dict, dad_dict]
new_file = pandas.DataFrame(another_dict)
new_file.to_csv("new_folder.csv", index=False)

# 2. Check if today matches a birthday in the birthdays.csv
new_df = pandas.read_csv("new_folder.csv")
birthday_days=[new_df["day"]]
birthday_month=[new_df["month"]]

now = dt.datetime.now()

for index in range(len(birthday_days)):
    if now.day == new_df["day"][index] and now.month == new_df["month"][index] or True:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        for digit in range(1, 4):
            file_list=[f"letter_templates/letter_{digit}.txt"]
            random_letter = choice(file_list)
        with open(random_letter) as rand_letter:
            data = rand_letter.read()
            data = data.replace("[NAME]", new_df["name"][index])
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=new_df["email"][index],
                                msg=f"Subject: Happy Birthday\n\n{data}"
                                )



