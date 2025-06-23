import psutil
import sys
import os
from datetime import datetime
import smtplib
from email.message import EmailMessage

def log_processes(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, "process_log.txt")
    with open(filename, 'w') as f:
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            f.write(f"Name: {proc.info['name']}, PID: {proc.info['pid']}, User: {proc.info['username']}\n")
    return filename

def send_email(log_file, recipient_email):
    try:
        msg = EmailMessage()
        msg['Subject'] = 'Process Log File'
        msg['From'] = "sakshipatil8996@gmail.com"
        msg['To'] = recipient_email

        with open(log_file, 'rb') as f:
            content = f.read()
            msg.set_content("Attached is the log file of running processes.")
            msg.add_attachment(content, maintype='text', subtype='plain', filename=os.path.basename(log_file))

        # SMTP setup (e.g., Gmail requires app password)
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login("sakshipatil8996@gmail.com", "Gmail")
            smtp.send_message(msg)
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python ProcInfoLog.py <directory> <email>")
        return

    directory = sys.argv[1]
    email = sys.argv[2]

    log_file = log_processes(directory)
    send_email(log_file, email)

if __name__ == "__main__":
    main()