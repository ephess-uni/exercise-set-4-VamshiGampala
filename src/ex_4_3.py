""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    list1 = get_shutdown_events(logfile)
    start_time= logstamp_to_datetime(list1[0].split(' ')[1])
    end_time= logstamp_to_datetime(list1[-1].split(' ')[1])
    diff = end_time - start_time
    diff_in_hours = diff.total_seconds() / 36
    return diff_in_hours


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
