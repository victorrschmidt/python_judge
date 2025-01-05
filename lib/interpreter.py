import sys
from pathlib import Path
from lib.files import *
from lib.logger import logger

def validate_argv() -> None:
    argc = len(sys.argv)

    if argc < 2:
        logger.error_argc_number()
        sys.exit(1)

    submission_file = Path(f"{SUBMISSION_FOLDER.name}/{sys.argv[1]}")

    if not submission_file.exists():
        logger.error_submission_file_missing(submission_file.name)
        sys.exit(1)

    if submission_file.suffix != '.cpp':
        logger.error_submission_file_invalid(submission_file.name)
        sys.exit(1)
