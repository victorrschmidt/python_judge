import sys
from lib.files import LANGUAGES
from lib.logger import logger

def validate_argv() -> None:
    argc = len(sys.argv)

    if argc != 2:
        logger.error_argc()
        sys.exit(1)

    suffix = sys.argv[1]

    if suffix not in LANGUAGES:
        logger.error_submission_extension(suffix)
        sys.exit(1)
