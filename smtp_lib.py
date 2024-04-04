import smtplib



# hostname = 'smtp.gmail.com'
# emial = 'nirnay99bhardwaj@gmail.com'
# password =

with smtplib.SMTP(host=hostname) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg=f'Subject : test python Email\n\n '
    )



