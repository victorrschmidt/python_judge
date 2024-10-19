import sys
import subprocess
from pathlib import Path
from lib.files import *
from lib.interpreter import interpreter
from lib.logger import logger

TIME_LIMIT = 2

class judge:
    def __init__(self) -> None:
        """
        Construtor da classe; define o caminho do arquivo de submissão.
        """

        self.submission_file_path = f"{SUBMISSION_FOLDER.name}/{sys.argv[1]}"

    def check_io_files(self) -> None:
        """
        Função para verificar e definir os casos de teste. Cada par .in e .sol
        forma um caso de teste para ser julgado. A função verifica 3 coisas:

        - Verifica se todos os arquivos contidos no folder 'io' são .in ou .sol.
        - Verifica se cada arquivo .in possui um arquivo .sol de mesmo nome.
        - Verifica se existe pelo menos um par de arquivos .in e .sol no folder 'io'.
        """

        self.io_file_list = []
        file_dict = {'.in': set(), '.sol': set()}

        for file in IO_FOLDER.iterdir():
            if file.suffix not in file_dict:
                logger.error_io_file_invalid(file.name)
                sys.exit(1)
            file_dict[file.suffix].add(file.stem)

        for file_stem in file_dict['.in']:
            if file_stem not in file_dict['.sol']:
                logger.error_sol_file_missing(file_stem)
                sys.exit(1)
            self.io_file_list.append(file_stem)

        if len(self.io_file_list) == 0:
            logger.error_in_file_missing()
            sys.exit(1)

    def judge_solution(self, sol_file: Path) -> None:
        """
        Função para verificar se o arquivo output.txt produziu a mesma saída
        definida pelo arquivo .sol do caso de teste. As linhas são verificadas
        uma a uma, e em caso de descrepância, a execução do Judge é encerrada e
        é mostrado o erro encontrado. A função verifica 2 coisas:

        - Verifica se o arquivo output.txt possui o mesmo número de linhas que
        o arquivo .sol correspondente.
        - Verifica se a i-ésima linha do arquivo output.txt é igual a i-ésima
        linha do arquivo .sol correspondente.
        """

        output_lines = OUTPUT_FILE.read_text().split('\n')
        sol_lines = sol_file.read_text().split('\n')

        if len(output_lines) != len(sol_lines):
            logger.judge_output_lines_number(len(output_lines), len(sol_lines))
            sys.exit(1)

        for i in range(len(output_lines)):
            if output_lines[i] != sol_lines[i]:
                logger.judge_wrong_answer(output_lines[i], sol_lines[i])
                sys.exit(1)

    def run_test_case(self, test_case_name: str) -> None:
        """
        Função para executar o arquivo de submissão com o arquivo .in do caso
        de teste, e em seguida chamar a função para comparar a saída com o
        conteúdo do arquivo .sol correspondente. São verificadas 2 coisas:

        - Verifica se a submissão excedeu o tempo limite de execução.
        - Verifica se a submissão não apresentou nenhum erro de execução.
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
                logger.judge_time_limit_exceeded(TIME_LIMIT)
                sys.exit(1)

            if process.returncode == 1:
                sys.exit(1)

            self.judge_solution(sol_file)

    def execute(self) -> None:
        """
        Função principal do Judge, responsável por chamar as funções de
        verificação de arquivos de .in e .sol e de execução dos casos de teste.
        Caso todos os casos de teste estejam corretos, é mostrada a mensagem
        de "Accepted".
        """

        self.check_io_files()

        for test_case_name in self.io_file_list:
            self.run_test_case(test_case_name)

        logger.judge_accepted_answer()

if __name__ == '__main__':
    interpreter.validate_argv()
    j = judge()
    j.execute()
