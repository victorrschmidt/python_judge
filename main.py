import sys
import subprocess
from pathlib import Path
from lib.logger import logger

SUBMISSION_FOLDER = Path('submissions')
IO_FOLDER = Path('io')
OUTPUT_FILE = Path('output.txt')
TIME_LIMIT = 2

class Judge:
    def __init__(self) -> None:
        """
        Construtor da classe; Define o caminho do arquivo de submissão e
        verifica 3 coisas:

        - Verifica se foi especificado um arquivo de submissão no argv.
        - Verifica se o arquivo especificado no argv existe.
        - Verifica se o arquivo especificado no argv é um arquivo Python.
        """

        try:
            self.submission_file_path = f"{SUBMISSION_FOLDER.name}/{sys.argv[1]}"
        except IndexError:
            logger.argv()
            sys.exit(1)

        submission_file = Path(self.submission_file_path)

        if not submission_file.exists():
            logger.file_not_found(submission_file.name)
            sys.exit(1)

        if submission_file.suffix != '.py':
            logger.invalid_submission_file(submission_file.name)
            sys.exit(1)

    def check_io_files(self) -> None:
        """
        Função para verificar e definir os arquivos de entrada e saída. Cada
        par .in e .sol forma um caso de teste para ser julgado. A função
        verifica 3 coisas:

        - Verifica se todos os arquivos contidos no folder 'io' são .in ou .sol.
        - Verifica se cada arquivo .in possui um arquivo .sol de mesmo nome.
        - Verifica se pelo existe menos um par de arquivos .in e .sol no folder 'io'.
        """

        self.io_file_list = []
        file_dict = {'.in': set(), '.sol': set()}

        for file in IO_FOLDER.iterdir():
            if file.suffix not in file_dict:
                logger.invalid_io_file(file.name)
                sys.exit(1)
            file_dict[file.suffix].add(file.stem)

        for file_stem in file_dict['.in']:
            if file_stem not in file_dict['.sol']:
                logger.missing_sol_file(f"{file_stem}.in")
                sys.exit(1)
            self.io_file_list.append(file_stem)

        if len(self.io_file_list) == 0:
            logger.no_in_files()
            sys.exit(1)

    def judge_solution(self, sol_file: Path) -> None:
        """
        Função para verificar se o arquivo output.txt produziu a mesma saída
        definida pelo arquivo .sol. As linhas são verificadas uma a uma, e em
        caso de descrepância, a execução do Judge é encerrada e é mostrado
        o erro correspondente. A função verifica 2 coisas:

        - Verifica se o arquivo output.txt possui o mesmo número de linhas que
        o arquivo .sol correspondente.
        - Verifica se a i-ésima linha do arquivo output.txt é igual a i-ésima
        linha do arquivo .sol correspondente.
        """

        output_lines = OUTPUT_FILE.read_text().split('\n')
        sol_lines = sol_file.read_text().split('\n')

        if len(output_lines) != len(sol_lines):
            logger.len_output_lines(len(output_lines), len(sol_lines))
            sys.exit(1)

        for i in range(len(output_lines)):
            if output_lines[i] != sol_lines[i]:
                logger.wrong_answer(output_lines[i], sol_lines[i])
                sys.exit(1)

    def run_test_case(self, test_case_name: str) -> None:
        """

        """
        in_file = Path(f"{IO_FOLDER.name}/{test_case_name}.in")
        sol_file = Path(f"{IO_FOLDER.name}/{test_case_name}.sol")

        with OUTPUT_FILE.open(mode='w') as output_file, \
            in_file.open(mode='r') as in_file:

            try:
                process = subprocess.run(
                    ['py', self.submission_file_path],
                    stdin=in_file,
                    stdout=output_file,
                    timeout=TIME_LIMIT
                )
            except subprocess.TimeoutExpired:
                logger.time_limit_exceeded(TIME_LIMIT)
                sys.exit(1)

            if process.returncode == 1:
                sys.exit(1)

            self.judge_solution(sol_file)

    def execute(self) -> None:
        """

        """
        self.check_io_files()

        for test_case_name in self.io_file_list:
            self.run_test_case(test_case_name)

        logger.accepted_answer()

if __name__ == '__main__':
    judge = Judge()
    judge.execute()
