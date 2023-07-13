# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

# starting time, duration, optional third day argument
print(add_time("08:30 AM", "1:02"))


# Run unit tests automatically
# main(module='test_module', exit=False)
