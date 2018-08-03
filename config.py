import sys

from datetime import datetime

import constants


class ConfigFileException(Exception):
    pass


def validate_line_length(current_line, config_input):
    if len(config_input) != 3:
        raise ConfigFileException(
            'Error on line {}. '
            'Entry must be in format "MM HH file_path"'.format(current_line)
        )


def validate_time(str_time, format, current_line, field_type='time'):
    try:
        return datetime.strptime(str_time, format)
    except ValueError:
        raise ConfigFileException('Error on line {}. Invalid minute "{}"'.format(current_line, field_type))


def validate_line_content(current_line, minute, hour, file_path):

    if minute != constants.RELATIVE_TIME:
        minute = validate_time(minute, constants.TIME_FORMATS['minutes'], current_line, field_type='minute')

    if hour != constants.RELATIVE_TIME:
        hour = validate_time(hour, constants.TIME_FORMATS['hours'], current_line, field_type='hour')

    return minute, hour, file_path


def validate_config_input(configs):
    validated_config = []
    for line, config in enumerate(configs):
        config = config.strip().split()
        validate_line_length(line, config)
        config = validate_line_content(line, *config)
        validated_config.append(config)

    return validated_config


_cron_config = sys.stdin.readlines()
cron_config = validate_config_input(_cron_config)
