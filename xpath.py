import pyodbc
import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome(r"C:\Users\sameer\Downloads\chromedriver_win32\chromedriver")
driver.implicitly_wait(10)

MeetingDate = datetime.datetime(2020, 5, 11)
delay = 3  # seconds

connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=192.168.1.232\SQLEXPRESS;'
                            'Database=meetingdatevalidator;'
                            'Trusted_Connection=yes;')

cursor = connection.cursor()
rows = cursor.execute(
    'SELECT * FROM [meetingdatevalidator].[dbo].[sameerrequest] where update_status is null ').fetchall()

for row in rows:
    # print(row[4])
    try:
        driver.get(row[4])
        agendaMeetingdateformat = MeetingDate.strftime(row[7])
        meeting = row[5].replace('*', agendaMeetingdateformat)
        # print(meeting)
        my_element = driver.find_element_by_xpath(meeting).text
        if my_element == agendaMeetingdateformat:
            # print('valid Meeting date')
            cursor.execute("UPDATE [meetingdatevalidator].[dbo].[sameerrequest] SET update_status=? WHERE fcid = ?",
                           'valid Meeting date',row[0])
            cursor.commit()
        else:
            # print('Invalid Meeting date')
            cursor.execute("UPDATE [meetingdatevalidator].[dbo].[sameerrequest] SET update_status=? WHERE fcid = ?",
                           'Invalid Meeting date',row[0])
            cursor.commit()

    except NoSuchElementException:  # spelling error making this code not work as expected
        print("bad page:")
        cursor.execute("UPDATE [meetingdatevalidator].[dbo].[sameerrequest] SET update_status=? WHERE fcid = ?",'Bad xpath',row[0])
        cursor.commit()
