import psutil
import pygetwindow as gw
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os
import logging

# Configuration
EMAIL_FROM = 'bacs.anti.cheat@gmail.com'
EMAIL_PASSWORD = 'geey tugd lnzr dfuz'
EMAIL_TO = 'varil35414@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
LOG_FILE_PATH = 'browser_activity.log' #Logging file
CHECK_INTERVAL = 10  # in seconds   
BROWSER_TO_CLOSE = 'chrome.exe'

# Setup logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_browser_processes():
    browsers = ['chrome.exe', 'firefox.exe', 'msedge.exe']
    running_processes = [p.info['name'] for p in psutil.process_iter(['name'])]
    active_browsers = [browser for browser in browsers if browser in running_processes]
    return active_browsers

def get_open_browsers():
    browsers = ['Chrome', 'Firefox', 'Edge']
    open_browsers = []
    for window in gw.getWindowsWithTitle(''):
        if any(browser in window.title for browser in browsers):
            open_browsers.append(window.title)
    return open_browsers

def log_browser_activity():
    active_browsers = get_browser_processes()
    open_browser_windows = get_open_browsers()
    
    log_entries = []
    if active_browsers or open_browser_windows:
        log_entries.append(f"Active Browser Processes: {', '.join(active_browsers)}")
        log_entries.append(f"Open Browser Windows: {', '.join(open_browser_windows)}")
        log_entries.append("-" * 40)
    
    if log_entries:
        logging.info("\n".join(log_entries))
        return "\n".join(log_entries)
    return ""

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.send_message(msg)
        logging.info("Email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def close_browser(browser_name):
    for process in psutil.process_iter(['pid', 'name']):
        try:
            if browser_name.lower() in process.info['name'].lower():
                process.terminate()
                logging.info(f"Terminated {process.info['name']} with PID {process.info['pid']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            logging.error(f"Error: {e}")

def monitor_and_report():
    while True:
        log_content = log_browser_activity()
        
        if log_content:
            send_email('Browser Activity Report on PC_NO.:(Add PC number)', log_content) # Important Information Needed to identify specific computers
        
        active_browsers = get_browser_processes()
        if BROWSER_TO_CLOSE in active_browsers:
            close_browser(BROWSER_TO_CLOSE)
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    logging.info("Starting the monitoring service.")
    monitor_and_report()
