import sys
from pathlib import Path
from lib.files import *
from lib.logger import logger

class interpreter:
    @staticmethod
    def create_submission(file_name: str) -> None:
        file = Path(f"{SUBMISSION_FOLDER}/{file_name}.py")

        if file.exists():
            logger.error_argv_create_submission_exists(file_name)
            sys.exit(1)

        file.touch()

    @staticmethod
    def clear_submissions() -> None:
        for file in SUBMISSION_FOLDER.iterdir():
            file.unlink()

    @staticmethod
    def clear_tests() -> None:
        for file in IO_FOLDER.iterdir():
            file.unlink()

    @staticmethod
    def create_tests(n: int) -> None:
        interpreter.clear_tests()

        for file_number in range(1, n+1):
            for file_suffix in ('in', 'sol'):
                file = Path(f"{IO_FOLDER.name}/{file_number}.{file_suffix}")
                file.touch()

    @staticmethod
    def validate_argv() -> None:
        argc = len(sys.argv)

        if argc < 2:
            logger.error_argv_number()
            sys.exit(1)

        match sys.argv[1]:
            case 'help':
                logger.help()
                sys.exit(1)

            case 'create_submission':
                if argc < 3:
                    logger.error_argv_create_submission_name()
                    sys.exit(1)
                interpreter.create_submission(sys.argv[2])
                sys.exit(1)

            case 'create_tests':
                if argc < 3:
                    logger.error_argv_create_tests()
                    sys.exit(1)
                interpreter.create_tests(int(sys.argv[2]))
                sys.exit(1)

            case 'clear_tests':
                interpreter.clear_tests()
                sys.exit(1)

            case 'clear_submissions':
                interpreter.clear_submissions()
                sys.exit(1)

        submission_file = Path(f"{SUBMISSION_FOLDER.name}/{sys.argv[1]}")

        if not submission_file.exists():
            logger.error_submission_file_missing(submission_file.name)
            sys.exit(1)

        if submission_file.suffix != '.py':
            logger.error_submission_file_invalid(submission_file.name)
            sys.exit(1)
