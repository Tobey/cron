from datetime import datetime
from datetime import timedelta

from cli_args import required_format

import constants


def _get_next_cron_time(current_time, cron_time, fixed_hour, fixed_min):
    """helper to calculate the next possible time"""
    current_day = cron_time

    cron_delta = cron_time - current_time
    if cron_delta.total_seconds() >= 0:
        return cron_time

    max_hour = cron_time.hour + 1 if fixed_hour else constants.MAX_HOUR + 1
    max_minute = cron_time.minute + 1 if fixed_min else constants.MAX_MINUTE + 1

    min_hour = cron_time.hour

    time_format = '%d:' + required_format
    new_cron_time = None
    check_next_time = True

    while check_next_time:
        # Attempt to sequentially check next cron time depending on input

        for hour in range(min_hour, max_hour):

            impossible_time_frame = current_day.day == current_time.day and hour < current_time.hour
            # no need to check every minute if the hour is behind the current time
            if not impossible_time_frame:

                min_minute = cron_time.minute if fixed_min else 0

                for minute in range(min_minute, max_minute):
                    cron_time_str = '{:02}:{:02}:{:02}'.format(current_day.day, hour, minute)
                    new_cron_time = datetime.strptime(cron_time_str, time_format)
                    cron_delta = new_cron_time - current_time
                    if cron_delta.total_seconds() >= 0:
                        check_next_time = False
                        break
                else:
                    min_minute = cron_time.minute if fixed_min else 0
                    continue
                break

        min_hour = cron_time.hour if fixed_hour else 0
        current_day = current_time + timedelta(days=1)

    return new_cron_time


def get_next_cron_time(current_time, cron_hour='*', cron_minute='*'):
    fixed_hour, fixed_min = True, True
    if cron_hour == constants.RELATIVE_TIME:
        cron_hour = current_time - timedelta(hours=current_time.hour)
        fixed_hour = False

    if cron_minute == constants.RELATIVE_TIME:
        cron_minute = current_time - timedelta(minutes=current_time.minute)
        fixed_min = False

    cron_time_str = '{}:{}'.format(
        cron_hour.strftime(constants.TIME_FORMATS['hours']),
        cron_minute.strftime(constants.TIME_FORMATS['minutes'])
    )
    cron_time = datetime.strptime(cron_time_str, required_format)

    cron_time = _get_next_cron_time(current_time, cron_time, fixed_hour, fixed_min)

    return cron_time
