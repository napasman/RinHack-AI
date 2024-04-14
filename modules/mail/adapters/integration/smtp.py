import smtplib

from email.mime.text import MIMEText
from email.header import Header
from modules.common.main.config import SMTPConfig
from modules.mail.application.common.ports import SMTPPort


class SMTP(SMTPPort):
    def __init__(self, smtp_config: SMTPConfig) -> None:
        self._smtp_config = smtp_config

    async def send_messages(self, *, recipient_mails: list[str], msg_text: str) -> None:

        msg = MIMEText(f"{msg_text}", "plain", "utf-8")
        msg["Subject"] = Header("Обнаружена угроза", "utf-8")
        msg["From"] = self._smtp_config.login
        msg["To"] = ", ".join(recipient_mails)

        s = smtplib.SMTP("smtp.yandex.ru", 587, timeout=10)

        try:
            s.starttls()
            s.login(self._smtp_config.login, self._smtp_config.password)
            s.sendmail(msg["From"], recipient_mails, msg.as_string())
        except Exception as ex:
            print(ex)
        finally:
            s.quit()
