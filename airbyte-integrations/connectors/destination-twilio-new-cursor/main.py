#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import sys

from destination_twilio_new_cursor import DestinationTwilioNewCursor

if __name__ == "__main__":
    DestinationTwilioNewCursor().run(sys.argv[1:])
