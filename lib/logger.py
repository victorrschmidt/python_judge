class logger:
    line = '-' * 56

    @staticmethod
    def log_error(message: str) -> None:
        print(f"{logger.line}\nERRO: {message}\n{logger.line}")

    @staticmethod
    def log_answer(message: str) -> None:
        print(f"{logger.line}\nJudge: {message}\n{logger.line}")

    @staticmethod
    def argv() -> None:
        message = f"Especifique um arquivo de submissão.\n\n" \
                  f"py main.py\n" \
                  f"{' ' * 11}^"
        logger.log_error(message)

    @staticmethod
    def file_not_found(file_name: str) -> None:
        message = f"O arquivo '{file_name}' não foi encontrado.\n\n" \
                  f"py main.py {file_name}\n" \
                  f"{' ' * 11}^\n" \
                  f"Certifique-se de que o arquivo está no diretório\n" \
                  f"submissions/ e possui o mesmo nome especificado."
        logger.log_error(message)

    @staticmethod
    def invalid_submission_file(file_name: str) -> None:
        file_name_suffix_len = len(file_name[0: file_name.index('.')])
        message = f"O arquivo de submissão precisa ser um arquivo\n" \
                  f"python.\n\n" \
                  f"py main.py {file_name}\n" \
                  f"{' ' * (12 + file_name_suffix_len)}^"
        logger.log_error(message)

    @staticmethod
    def invalid_io_file(file_name: str) -> None:
        message = f"O arquivo '{file_name}' é inválido.\n\n" \
                  f"Os arquivos de entrada e saída devem ser,\n" \
                  f"respectivamente, arquivos .in e .sol."
        logger.log_error(message)

    @staticmethod
    def missing_sol_file(file_name: str) -> None:
        message = f"O arquivo '{file_name}' não possui um arquivo .sol \n" \
                  f"correspondente.\n\n" \
                  f"Verifique se cada arquivo de entrada possui um\n" \
                  f"arquivo de saída correspondente."
        logger.log_error(message)

    @staticmethod
    def no_in_files() -> None:
        message = f"Nenhum arquivo .in foi encontrado.\n\n" \
                  f"Certifique-se de que os arquivos .in e .sol estão no \n" \
                  f"diretório correto."
        logger.log_error(message)

    @staticmethod
    def time_limit_exceeded(time_limit: int) -> None:
        message = f"Time limit exceeded ({time_limit * 1000} ms)."
        logger.log_answer(message)

    @staticmethod
    def len_output_lines(output_lines: int, sol_lines: int) -> None:
        message = f"Wrong answer.\n\n" \
                  f"O número de linhas produzidas difere.\n\n" \
                  f"Linhas produzidas: {output_lines}\n" \
                  f"Linhas esperadas: {sol_lines}"
        logger.log_answer(message)

    @staticmethod
    def wrong_answer(output_line: str, sol_line: str) -> None:
        message = f"Wrong answer.\n\n" \
                  f"Linha produzida x linha esperada:\n\n" \
                  f"{output_line}\n" \
                  f"{sol_line}"
        logger.log_answer(message)

    @staticmethod
    def accepted_answer() -> None:
        message = f"ACCEPTED!"
        logger.log_answer(message)
