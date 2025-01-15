import os
import sys
from pathlib import Path
from lib.logger import logger
from lib.languages import LANGUAGES

SOLUTION_FILE = Path('io/expected.sol')
OUTPUT_FILE = Path('io/output.txt')

class judge:
    def __init__(self):
        self.running_lang = None
        self.output_only = False

    def validate_argv(self) -> int:
        argc = len(sys.argv)

        if argc < 2 or argc > 3:
            logger.error_argc()
            sys.exit(1)

        lang = sys.argv[1]

        if lang not in LANGUAGES:
            logger.error_submission_language(lang)
            sys.exit(1)

        self.running_lang = lang

        if argc == 2:
            return

        optional_argv = sys.argv[2]

        if optional_argv == '-o':
            self.output_only = True
        else:
            logger.error_unknown_command(optional_argv)
            sys.exit(1)

    def run_file(self) -> None:
        command_list = LANGUAGES[self.running_lang]
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

        logger.judge_accepted_answer()

    def print_output(self) -> None:
        logger.log(OUTPUT_FILE.read_text())

    def execute(self) -> None:
        self.validate_argv()
        self.run_file()

        if self.output_only:
            self.print_output()
        else:
            self.judge_solution()

if __name__ == '__main__':
    j = judge()
    j.execute()
