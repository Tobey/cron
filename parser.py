import sys

import constants
from config import cron_config
from cli_args import current_time
from cron_parser import get_next_cron_time


def print_next_run(simulated_time, minute, hour, file_path):
    """
    This function is used to output the next time the cron will run,
    given the current time

    :param simulated_time: simulated "current time"
    :param minute: cron minutes args
    :param hour: cron hour args
    :param file: path to file
    :return:
    """
    output_template = '{}:{:02} {} - {}\n'

    cron_time = get_next_cron_time(simulated_time, cron_hour=hour, cron_minute=minute)
    output = output_template.format(
        cron_time.hour, cron_time.minute, constants.DAY_FORMATS[cron_time.day], file_path
    )
    sys.stdout.write(output)


if __name__ == '__main__':
    for config in cron_config:
        print_next_run(current_time, *config)
