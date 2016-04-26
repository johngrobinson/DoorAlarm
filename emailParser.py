#!/usr/bin/evn python


####################### EMAIL CREATION SECTION START ##############################
# This code is used to email out a notification if the magnetic door sensor has   #
# been triggered.                                                                 #
# Begin mail setup, this code is written for GMAIL but you could easily re-write  #
# the current code by changing the GMAIL setup properties with Hotmail or what    #
# ever smtp mail service.                                                         #
###################################################################################

def emailalert():
    import smtplib
    from time_convert import door_timestamp
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # GMAIL user setup #
    gmail_sender = 'johngrobinson@gmail.com'
    gmail_passwd = 'Monkeybutt2'
    you = "jrotton@hotmail.com"
    # , Sjcarrillo2@gmail.com
    # GMAIL SMTP Server connect
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP( smtp_host, smtp_port )
    server.ehlo( )
    server.starttls( )
    server.login( gmail_sender, gmail_passwd )

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart( 'alternative' )
    msg['Subject'] = 'TEST TEST - Do you know where you daughter is? - TEST TEST'
    msg['From'] = gmail_sender
    msg['To'] = you

    b1 = '<html><head></head><body><p><br><br>Do you know where you daughter is?<br><br>Your front door was opened at: '
    b2 = door_timestamp( 0 )
    b3 = ' </p><BR><BR><BR>The Alarm!<br><br>John Robinson</body></html>'

    # Create the body of the message (a plain-text and an HTML version).
    text = (
        "Do you know where you daughter is? \n Your front door was opened at: ", door_timestamp( 0 ), "\n\n The Alarm")
    html = (b1 + b2 + b3)

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText( text, 'plain' )
    part2 = MIMEText( html, 'html' )

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach( part1 )
    msg.attach( part2 )
    # Send the message via gmail SMTP server.
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    server.sendmail( gmail_sender, [you], msg.as_string( ) )
    server.quit( )



    ####################### EMAIL CREATION SECTION END ###############################
