import smtplib
import email.message
import os

import seagate_firecuda_hdd_4tb
import price_check_check

checks = [
    seagate_firecuda_hdd_4tb.price_check,
    price_check_check.price_check_check,
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
            msg['Subject'] = check.__module__ + "." + check.__name__
            msg['From'] = os.environ['EMAIL_FROM']
            msg['To'] = os.environ['EMAIL_TO']
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(result)

            if os.environ.get("DRY_RUN") == "true":
                print("DRY_RUN: Not sending email")
            else:
                s = smtplib.SMTP(os.environ['EMAIL_HOST'], os.environ['EMAIL_PORT'])
                s.starttls()
                s.login(msg['From'], os.environ['EMAIL_PASSWORD'])
                s.sendmail(msg['From'], [msg['To']], msg.as_string())
                s.quit()

            print("SUBJECT: " + msg['Subject'])
            print("BODY: " + result)
            print("Email sent successfully")

if __name__ == "__main__":
    """
    Supply the following environment variables:
    EMAIL_FROM, EMAIL_TO, EMAIL_PASSWORD, EMAIL_HOST, EMAIL_PORT
    """
    main()
