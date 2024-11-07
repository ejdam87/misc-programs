import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


Mail = str

# Works with Gmail bots
PORT = 587
SMTP_SERVER = "smtp.gmail.com"

SENDER = "your.mail@xxx.com"
PASSWORD = "yourAppPassword"    # Setup in gmail account settings


def attach_sign(message: str, is_html: bool) -> str:
    
    if is_html:

        paragraph = """<footer> <p> ------------------- </p>
                                <p> <i> This message was sent with Dzadam's bot! </i> </p>
                        </footer>
                    """

        content = message.split("</html>")[0]
        content += paragraph + "\n"
        content += "</html>"

    else:

        content = message + "\n" + "-------------------"
        content += "This message was sent with Dzadam's bot!"

    return content


def send_mail(receiver: Mail,
              message: str,
              subject: str = "Bot message",
              is_html: bool = False) -> None:

    container = MIMEMultipart('alternative')
    container['Subject'] = subject
    container['From'] = SENDER
    container['To'] = receiver

    message = attach_sign(message, is_html)

    if is_html:
        content = MIMEText(message, 'html')
    else:
        content = MIMEText(message, 'plain')

    container.attach(content)
    context = ssl.create_default_context()

    with smtplib.SMTP(SMTP_SERVER, PORT) as server:

        server.starttls(context=context) # Secure connection
        server.login(SENDER, PASSWORD)
        server.sendmail(SENDER, receiver, container.as_string())
        server.quit()
