import argparse

from datetime import datetime

import constants

required_format = "{}:{}".format(
    constants.TIME_FORMATS['hours'], constants.TIME_FORMATS['minutes']
)


def valid_current_time(str_time):

    try:
        return datetime.strptime(str_time, required_format)
    except ValueError:
        msg = 'Not a valid time: "{}". required format  is "HH:MM"'.format(str_time)
        raise argparse.ArgumentTypeError(msg)


parser = argparse.ArgumentParser(description='A CLI tool for parsing cron job configs')
parser.add_argument('current_time', help='Current time in fromat HH:MM', type=valid_current_time)
args = parser.parse_args()

current_time = args.current_time
