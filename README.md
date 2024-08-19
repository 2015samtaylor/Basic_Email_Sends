## Overview

This Python script sends an email notification about the PowerSchool connection status and logs the process. It initializes an email instance with specified parameters and sends the email. It also logs the outcome (success or failure) to a log file and records this information in a SQL database.

## Dependencies

- `config`: Imports `EMAIL_PASS` for email authentication.
- `logging`: Standard Python module for logging.
- `modules.logging_metadata`: Imports `JobLogger` for custom logging.
- `modules.email_sends`: Imports `EMAIL` class for sending emails.

## Setup

1. **Logging Configuration**
   - Logs are saved to `Logs/PS_Email.log`.
   - Log format includes timestamp and message.
   - The log file is created if it does not exist.

2. **Email Configuration**
   - Initializes the `EMAIL` class with the following parameters:
     - `EMAIL_PASS`: Email account password (imported from `config`).
     - `from_email`: Sender’s email address.
     - `to_email`: List of recipient email addresses.
     - `subject`: Subject of the email.
     - `content_string`: Body of the email.
     - `attachment_one_path` and `attachment_two_path`: Paths to email attachments.

3. **Email Sending**
   - Calls the `send` method of the `EMAIL` class to send the email.

4. **Main Function**
   - Attempts to send the email and logs success.
   - In case of failure, logs the failure.

## Usage

1. **Create the `Logs` Directory**
   - The directory is created if it does not exist using `os.makedirs('Logs', exist_ok=True)`.

2. **Send Email and Log Results**
   - The email is sent and results are logged using `logger` and `logging`.

## SMTP Email Account Setup

To use SMTP for sending emails, ensure the following:

1. **Enable SMTP Access**
   - Go to your email provider's settings (e.g., Gmail).
   - Enable "Less secure app access" or use an "App password" if using 2FA (Two-Factor Authentication).
   - https://www.youtube.com/watch?v=kTcmbZqNiGw 

2. **Update Email Settings in Script**
   - Ensure that `EMAIL_PASS` is correctly set with your email account's password or app-specific password.
   - Configure the email server settings if needed (not shown in this script but often necessary for different email providers).

3. **Check for Security Settings**
   - Verify that your email provider allows SMTP connections and that the IP address or application sending emails is not blocked.

## Example

```python
from config import EMAIL_PASS
import logging
import os
from modules.logging_metadata import JobLogger
from modules.email_sends import EMAIL

logger = JobLogger(process_name='PowerSchool Email Notification', 
                   job_name='PowerSchool Email Notification', 
                   job_type='python')

logging.basicConfig(filename='Logs/PS_Email.log', level=logging.INFO,
                   format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', force=True)
logging.info('\n\n-------------PS_Email new instance log')

os.makedirs('Logs', exist_ok=True)

# Initialize Email Class
email_one = EMAIL(
    EMAIL_PASS=EMAIL_PASS,
    from_email='2015samtaylor@gmail.com',
    to_email=['2015samtaylor@gmail.com', 'samuel.taylor@greendot.org'],
    subject='PowerSchool Email Notification',
    content_string='Email Notifying About PowerSchool Connection Status is....',
    attachment_one_path=r'C:\Users\samuel.taylor\Desktop\Python_Scripts\CIVICS_Illuminate_to_PS\Civics_Scores.log',
    attachment_two_path=r'C:\Users\samuel.taylor\Desktop\Python_Scripts\Whetstone\Whetstone_Tracker_2.log'
)
    
email_one.send()

def main():
    try:
        email_one.send()
        logger.log_job('Success')
        logging.info('Success')
        logger.send_frame_to_SQL()
    except:
        logger.log_job('Failure')
        logging.info('Process failed')
        logger.send_frame_to_SQL()

main()
```
