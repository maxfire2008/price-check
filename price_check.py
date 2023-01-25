import smtplib
import email.message
import os

import seagate_firecuda_hdd_4tb

checks = [
    seagate_firecuda_hdd_4tb.price_check
]

def main():
    for check in checks:
        result = check()
        if result:
            # subject example: "Check returned: + seagate_firecuda_hdd_4tb.price_check"
            # body: result
            # send result to email with values from github actions secrets
            # SECRETS: EMAIL_FROM, EMAIL_TO, EMAIL_PASSWORD
            msg = email.message.Message()
            msg['Subject'] = "Check returned: " + check.__name__
            msg['From'] = os.environ['EMAIL_FROM']
            msg['To'] = os.environ['EMAIL_TO']
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(result)

            s = smtplib.SMTP(os.environ['EMAIL_HOST'], os.environ['EMAIL_PORT'])
            s.starttls()
            s.login(msg['From'], os.environ['EMAIL_PASSWORD'])
            s.sendmail(msg['From'], [msg['To']], msg.as_string())
            s.quit()

if __name__ == "__main__":
    """
    Supply the following environment variables:
    EMAIL_FROM, EMAIL_TO, EMAIL_PASSWORD, EMAIL_HOST, EMAIL_PORT
    """
    main()
