import os
import hashlib
import time
import smtplib
import shutil
from email.message import EmailMessage
from datetime import datetime
import sys

def generate_checksum(file_path):
    """Generate MD5 checksum for a file"""
    h = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def find_and_delete_duplicates(directory):
    """Find and delete duplicate files based on checksum"""
    checksums = {}
    deleted_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            checksum = generate_checksum(path)

            if checksum in checksums:
                os.remove(path)
                deleted_files.append(path)
            else:
                checksums[checksum] = path

    return deleted_files

def create_log_file(deleted_files):
    """Create log file with deleted file names"""
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_dir = "Marvellous"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"log_{now}.txt")

    with open(log_file, 'w') as f:
        f.write(f"Log created at: {datetime.now()}\n")
        f.write("Deleted duplicate files:\n")
        for file in deleted_files:
            f.write(file + "\n")

    return log_file

def send_email(log_file, recipient_email):
    """Send the log file as attachment"""
    msg = EmailMessage()
    msg['Subject'] = 'Duplicate File Removal Log'
    msg['From'] = 'sakshipatil8996@gmail.com'
    msg['To'] = recipient_email

    with open(log_file, 'rb') as f:
        data = f.read()
        msg.add_attachment(data, maintype='text', subtype='plain', filename=os.path.basename(log_file))

    # Gmail requires an App Password
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('sakshipatil8996@gmail.com', 'gmail')
        smtp.send_message(msg)

def main():
    if len(sys.argv) != 4:
        print("Usage: DuplicateFileRemoval.py <directory> <interval_minutes> <email>")
        return

    directory = sys.argv[1]
    interval_minutes = int(sys.argv[2])
    email = sys.argv[3]

    print(f"Waiting for {interval_minutes} minutes before deleting duplicates...")
    time.sleep(interval_minutes * 60)

    start_time = time.time()
    deleted_files = find_and_delete_duplicates(directory)
    log_file = create_log_file(deleted_files)
    send_email(log_file, email)
    end_time = time.time()

    print(f"{len(deleted_files)} duplicate files deleted.")
    print(f"Log saved to {log_file}")
    print(f"Operation took {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()