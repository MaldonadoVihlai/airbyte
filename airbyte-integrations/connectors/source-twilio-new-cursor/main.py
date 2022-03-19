#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_twilio_new_cursor import SourceTwilioNewCursor

if __name__ == "__main__":
    source = SourceTwilioNewCursor()
    launch(source, sys.argv[1:])
