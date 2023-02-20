""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation
    """
    list_of_log=[]
    print(logfile,"fffffffffffffffffffffff")
    with open('logfile') as f:
        lines = [line.rstrip('\n') for line in f]
        for i in lines:
            if 'Shutdown' in i:
                list_of_log.append(i)
    return list_of_log



# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
