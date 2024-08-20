from config import EMAIL_PASS
import logging
from modules.logging_metadata import *
from modules.email_sends import *
from modules.ps_checks import *

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
    subject='PowerSchool Email Notification Status',
    content_string='Email Notifying About PowerSchool Connection Status is Failing',
    attachment_one_path=r'powerschool_log_fails.csv', #file written out during did_PS_fail func
)
    

#Test this
def main(which_email_instance):
    try:
        determination(which_email_instance)
        logging.info('Success')
        logger.log_job('Success')
        logger.send_frame_to_SQL()
    except Exception as e:
        logging.info(f'Process failed due to {e}')
        logger.log_job('Failure')
        logger.send_frame_to_SQL()

main(email_one)