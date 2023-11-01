import smtplib
def sendmail():
    gmail_user = 'palak2609s@gmail.com'
    gmail_app_password = 'palak0102mail'
    
    sent_from = gmail_user
    sent_to = ['tush2298@gmail.com',"palak2609s@gmail.com"]
    sent_subject = "Test Mail"
    sent_body = "MAIL"
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)


    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
sendmail()
