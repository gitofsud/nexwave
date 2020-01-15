import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('daddynexwave@gmail.com', '741258963qwerty')
server.sendmail('daddynexwave@gmail.com', 'daddynexwave@gmail.com', 'GEORGE')
server.close()
