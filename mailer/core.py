from csv import DictReader
from email import message_from_file
from email.message import EmailMessage
from email.utils import parseaddr
from pathlib import Path
from smtplib import SMTP_SSL
from string import Template


def load_data(file: str, fields: tuple = None) -> DictReader:
    """Load file into csv.DictReader and yield rows from it."""
    reader = DictReader(Path(file).open())
    return reader


def parse_data(reader: DictReader, fields: tuple = None):
    for row in reader:
        yield row


def load_template(file: str) -> Template:
    with open(file) as f:
        s = Template(f.read())
    return s


def load_message(file: str):
    with open(file) as f:
        msg = message_from_file(f)
    return msg


def send(host: str, credentials: tuple = None, msg: EmailMessage = None):
    server = SMTP_SSL(host)
    server.login(*credentials)

    return NotImplemented
