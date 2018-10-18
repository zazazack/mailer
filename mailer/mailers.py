from csv import DictReader
from dataclasses import dataclass, field
from email.message import EmailMessage
from email import message_from_string
from pathlib import Path
from smtplib import SMTP_SSL
from string import Template


@dataclass
class BulkMailer(EmailMessage):
    sender: str
    template_file: Template = 'tests/test_template.txt'
    database_file: str = 'tests/test_database.csv'
    host: str = field(default='localhost')
    port: int = field(default=25)
    credentials: dict = field(default={'username': None, 'password': None})
    database: DictReader = field(init=False)
    message: EmailMessage = field(init=False)
    template: Template = field(init=False)

    def __post_init__(self):
        self.template = Template(Path(self.template_file).read_text())
        self.database = DictReader(Path(self.database_file).open())

    def gen_messages(self):
        for row in self.database:
            s = self.template(f=self.sender, t=row['email'])
            yield message_from_string(s)

    def send(self):
        with SMTP_SSL(self.host) as server:
            if self.credentials:
                server.login(self.credentials)
            server.set_debuglevel(1)
            server.send_message(self.message)
