class logger:
    line = '-' * 56

    @staticmethod
    def help() -> None:
        message = f"Lista de comandos:\n\n" \
                  f"help -> Acessa a lista de comandos.\n" \
                  f"create_submission nome -> Cria um arquivo de submissão.\n" \
                  f"create_tests n -> Cria N casos de teste.\n" \
                  f"clear_tests -> Remove todos os casos de teste.\n" \
                  f"clear_submissions -> Remove os arquivos de submissão."
        print(f"{logger.line}\n{message}\n{logger.line}")

    @staticmethod
    def log_error(message: str) -> None:
        print(f"{logger.line}\nERRO: {message}\n{logger.line}")

    @staticmethod
    def log_judge(message: str) -> None:
        print(f"{logger.line}\nJudge: {message}\n{logger.line}")

    @staticmethod
    def error_argv_number() -> None:
        message = f"Número de argumentos insuficiente.\n\n" \
                  f"py main.py\n" \
                  f"{' ' * 11}^\n\n" \
                  f"Especifique um arquivo de submissão ou digite\n" \
                  f"'help' para visualizar os comandos disponíveis."
        logger.log_error(message)

    @staticmethod
    def error_argv_create_submission_name() -> None:
        message = f"Número de argumentos insuficiente.\n\n" \
                  f"py main.py create_submission\n" \
                  f"{' ' * 29}^\n\n" \
                  f"Especifique um nome para o arquivo de submissão."
        logger.log_error(message)

    @staticmethod
    def error_argv_create_submission_exists(file_name: str) -> None:
        message = f"O arquivo '{file_name}.py' já existe.\n\n" \
                  f"py main.py create_submission {file_name}\n" \
                  f"{' ' * 29}^"
        logger.log_error(message)

    @staticmethod
    def error_argv_create_tests() -> None:
        message = f"Número de argumentos insuficiente.\n\n" \
                  f"py main.py create_tests\n" \
                  f"{' ' * 24}^\n\n" \
                  f"Especifique o número de testes a serem criados."
        logger.log_error(message)

    @staticmethod
    def error_submission_file_missing(file_name: str) -> None:
        message = f"O arquivo '{file_name}' não foi encontrado.\n\n" \
                  f"py main.py {file_name}\n" \
                  f"{' ' * 11}^\n\n" \
                  f"Certifique-se de que o arquivo está no diretório\n" \
                  f"submissions/ e se possui o mesmo nome especificado."
        logger.log_error(message)

    @staticmethod
    def error_submission_file_invalid(file_name: str) -> None:
        file_name_suffix_len = len(file_name[0: file_name.index('.')])
        message = f"O arquivo de submissão precisa ser um arquivo\n" \
                  f"Python.\n\n" \
                  f"py main.py {file_name}\n" \
                  f"{' ' * (12 + file_name_suffix_len)}^\n\n" \
                  f"Digite o comando 'py main.py create_submission nome'\n" \
                  f"para criar um arquivo de submissão, ou adicione um\n" \
                  f"manualmente."
        logger.log_error(message)

    @staticmethod
    def error_io_file_invalid(file_name: str) -> None:
        message = f"O arquivo '{file_name}' não é valido como um arquivo\n" \
                  f"de entrada/saída.\n\n" \
                  f"Os arquivos de entrada e saída devem possuir extensão\n" \
                  f".in e .sol, respectivamente."
        logger.log_error(message)

    @staticmethod
    def error_sol_file_missing(file_name: str) -> None:
        message = f"O arquivo de entrada '{file_name}.in' não possui um\n" \
                  f"arquivo de saída (.sol) correspondente.\n\n" \
                  f"Verifique se cada arquivo de entrada possui um\n" \
                  f"arquivo de saída correspondente."
        logger.log_error(message)

    @staticmethod
    def error_in_file_missing() -> None:
        message = f"Nenhum arquivo de entrada (.in) foi encontrado.\n\n" \
                  f"Certifique-se de criar os arquivos de entrada e saída e\n" \
                  f"colocá-los no diretório 'io'.\n\n" \
                  f"Você pode utilizar o comando 'py main.py create_tests N'\n" \
                  f"para gerar N pares de arquivos de entrada e saída."
        logger.log_error(message)

    @staticmethod
    def judge_time_limit_exceeded(time_limit: int) -> None:
        message = f"Time limit exceeded ({time_limit * 1000} ms)."
        logger.log_judge(message)

    @staticmethod
    def judge_output_lines_number(output_lines: int, sol_lines: int) -> None:
        message = f"Wrong answer.\n\n" \
                  f"O número de linhas produzidas difere.\n\n" \
                  f"Linhas produzidas: {output_lines}\n" \
                  f"Linhas esperadas: {sol_lines}"
        logger.log_judge(message)

    @staticmethod
    def judge_wrong_answer(output_line: str, sol_line: str) -> None:
        message = f"Wrong answer.\n\n" \
                  f"Linha produzida x linha esperada:\n\n" \
                  f"{output_line}\n{'^' * len(output_line)}\n\n" \
                  f"{sol_line}\n{'^' * len(sol_line)}"
        logger.log_judge(message)

    @staticmethod
    def judge_accepted_answer() -> None:
        message = f"ACCEPTED!"
        logger.log_judge(message)
