import logging
from argparse import ArgumentParser, FileType
from email import message_from_file
from email.utils import parseaddr

from __version__ import __version__


def main(sender: str,
         recipients: tuple,
         content: tuple,
         attachments: tuple = None):
    pass


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--version', const=__version__, action='store_const')
    parser.add_argument('-v', '--verbosity')

    # TODO: This must be mutually exclusive from any of the following arguments
    parser.add_argument(
        '-c', '--config', type=FileType('r'), default='server.cfg')

    parser.add_argument('sender', type=str)
    # TODO: 'to' and 'database' must be mutually exclusive
    parser.add_argument('to', type=str, nargs='+')
    parser.add_argument('-d', '--database', type=FileType('r'))

    # login information
    # TODO: argument group?
    parser.add_argument('-u', '--username', type=str, dest='login')
    parser.add_argument('-p', '--password', type=str, dest='login')

    # TODO: add subcommands for interactive shell
    args = parser.parse_args()

    main(*args)
