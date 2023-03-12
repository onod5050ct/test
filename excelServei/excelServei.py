import os
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from plyer import notification
import configparser

def send_email(body):
    from_addr = config['Email']['from_address']
    to_addr = config['Email']['to_address']
    password = config['Email']['from_password']
    smtp_server = config['Email']['smtp_server']
    smtp_port = config['Email']['smtp_port']

    msg = MIMEText(body)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Excel file update notification'
    msg['Date'] = formatdate()

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.close()
        print('Email sent successfully')
    except Exception as e:
        print('Something went wrong while sending email:', e)

def send_notification(body):
    notification.notify(
        title='Excel file update notification',
        message=body,
        app_name='Excel Update',
        timeout=10
    )
    
def check_file_updates():
    while True:
        for file_name in config['ExcelFiles']:
            if file_name.startswith('file'):
                excel_path = config['ExcelFiles'][file_name]
                if not os.path.isfile(excel_path):
                    print(f'Excel file not found: {excel_path}')
                    continue
                file_modified_time = os.path.getmtime(excel_path)
                if file_name not in file_modified_times:
                    file_modified_times[file_name] = file_modified_time
                    print(f'{file_name} was added to file_modified_times dictionary')
                    continue
                if file_modified_times[file_name] < file_modified_time:
                    file_modified_times[file_name] = file_modified_time
                    message_body = f'{file_name} has been updated!'
                    print(message_body)
                    notification_method = config['General']['notification_method']
                    if notification_method == 'email':
                        send_email(message_body)
                    elif notification_method == 'notification':
                        send_notification(message_body)
        time.sleep(int(config['General']['check_interval']))


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini', )
    file_modified_times = {}
    check_file_updates()
