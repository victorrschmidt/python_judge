class logger:
    text_line = '-' * 56

    @staticmethod
    def log_error(message: str) -> None:
        print(f"{logger.text_line}\nERRO: {message}\n{logger.text_line}")

    @staticmethod
    def log_judge(message: str) -> None:
        print(f"{logger.text_line}\nJudge: {message}\n{logger.text_line}")

    @staticmethod
    def error_argc_number() -> None:
        message = f"Número de argumentos insuficiente.\n\n" \
                  f"py main.py\n" \
                  f"{' ' * 11}^"
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
        message = f"O arquivo de submissão precisa ser um arquivo C++.\n\n" \
                  f"py main.py {file_name}\n" \
                  f"{' ' * (12 + file_name_suffix_len)}^"
        logger.log_error(message)

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
