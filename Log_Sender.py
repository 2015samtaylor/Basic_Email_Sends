from config import EMAIL_PASS
import logging
from modules.logging_metadata import *
from modules.email_sends import *

logger = JobLogger(process_name='PowerSchool Email Notification', 
                   job_name='PowerSchool Email Notification', 
                   job_type='python')

logging.basicConfig(filename='Logs/PS_Email.log', level=logging.INFO,
                   format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',force=True)
logging.info('\n\n-------------PS_Email new instance log')

os.makedirs('Logs', exist_ok=True)

#Initialize Email Class
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