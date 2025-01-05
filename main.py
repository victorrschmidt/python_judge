import os
import sys
from lib.files import *
from lib.interpreter import validate_argv
from lib.logger import logger

class judge:
    def run_file(self) -> None:
        if GCC_PATH not in os.environ['PATH'].split(os.pathsep):
            os.environ['PATH'] += f"{os.pathsep}{GCC_PATH}"

        command_list = (
            'cd submissions',
            'g++ bee.cpp -o run',
            f"run.exe < ../io/input.in > ../io/output.txt"
        )

        os.system(' && '.join(command_list))

    def judge_solution(self) -> None:
        output_lines = OUTPUT_FILE.read_text().split('\n')
        sol_lines = SOL_FILE.read_text().split('\n')

        if len(output_lines) != len(sol_lines):
            logger.judge_output_lines_number(len(output_lines), len(sol_lines))
            sys.exit(1)

        for i in range(len(output_lines)):
            if output_lines[i] != sol_lines[i]:
                logger.judge_wrong_answer(output_lines[i], sol_lines[i])
                sys.exit(1)

    def execute(self) -> None:
        self.run_file()
        self.judge_solution()
        logger.judge_accepted_answer()

if __name__ == '__main__':
    validate_argv()
    j = judge()
    j.execute()
