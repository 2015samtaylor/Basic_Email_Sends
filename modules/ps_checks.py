from .sql_query_module import *
from .email_sends import *

def did_PS_fail():

    p_log = SQL_query.SQL_query_90('''
    SELECT TOP 3 *
    FROM SSIS_Logging.dbo.process_log
    WHERE process_name = 'PowerSchool'
    ORDER BY end_time DESC;
    ''')

    p_log_fails = p_log[p_log['success_failure'].str.contains('Failure|Failed|Fail', case=False, na=False)]

    if p_log_fails.empty:
        return(False)
    else:
        p_log_fails.to_csv('powerschool_log_fails.csv', index=False)
        return(True)


def determination(which_email_instance):

    #If output == False the PS processes did not fail, if True they did Fail. 
    output = which_email_instance.did_PS_fail()

    if output == True:
        logging.info(f'PS processes have failed. Sending email out to {which_email_instance.to_email}')
        try:
            which_email_instance.send()
        except Exception as e:
            logging.error(f'Unable to send email due to error {e}')
    else:
        pass
        logging.info('Powerschool processes were a success. No need to send email')