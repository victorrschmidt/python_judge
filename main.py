import os
import sys
from pathlib import Path
from lib.logger import logger
from lib.languages import LANGUAGES

SOLUTION_FILE = Path('io/expected.sol')
OUTPUT_FILE = Path('io/output.txt')

class judge:
    def validate_argv(self) -> None:
        argc = len(sys.argv)

        if argc != 2:
            logger.error_argc()
            sys.exit(1)

        suffix = sys.argv[1]

        if suffix not in LANGUAGES:
            logger.error_submission_extension(suffix)
            sys.exit(1)

    def run_file(self) -> None:
        suffix = sys.argv[1]
        command_list = LANGUAGES[suffix]
        exit_status = os.system(' && '.join(command_list))

        if exit_status == 1:
            sys.exit(1)

    def judge_solution(self) -> None:
        output_lines = OUTPUT_FILE.read_text().split('\n')
        solution_lines = SOLUTION_FILE.read_text().split('\n')
        output_lines_number = len(output_lines)
        solution_lines_number = len(solution_lines)

        if output_lines_number != solution_lines_number:
            logger.judge_output_lines_number(output_lines_number, solution_lines_number)
            sys.exit(1)

        for i in range(output_lines_number):
            if output_lines[i] != solution_lines[i]:
                logger.judge_wrong_answer(output_lines[i], solution_lines[i])
                sys.exit(1)

    def execute(self) -> None:
        self.validate_argv()
        self.run_file()
        self.judge_solution()
        logger.judge_accepted_answer()

if __name__ == '__main__':
    j = judge()
    j.execute()
