def __screen_shot(self):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Subject'] = subject

    text = "Send current screenshot."
    msg.attach(MIMEText(text))

    shot = take_screenshot()
    img_data = open(shot, 'rb').read()
    msg.attach(MIMEImage(img_data, name = os.path.basename(shot)))

    # for f in files or []:
    #     with open(f, "rb") as fil:
    #         part = MIMEApplication(
    #             fil.read(),
    #             Name=basename(f)
    #         )
    #     # After the file is closed
    #     part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
    #     msg.attach(part)


    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()