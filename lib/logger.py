class logger:
    text_line = '-' * 56

    @staticmethod
    def log(text: str) -> None:
        print(f"{logger.text_line}\n{text}\n{logger.text_line}")

    @staticmethod
    def log_error(message: str) -> None:
        print(f"{logger.text_line}\nErro: {message}\n{logger.text_line}")

    @staticmethod
    def log_judge(message: str) -> None:
        print(f"{logger.text_line}\nJudge: {message}\n{logger.text_line}")

    @staticmethod
    def error_argc() -> None:
        message = f"Número de argumentos inválido."
        logger.log_error(message)

    @staticmethod
    def error_unknown_command(command: str) -> None:
        message = f"Comando '{command}' inválido."
        logger.log_error(message)

    @staticmethod
    def error_submission_extension(suffix: str) -> None:
        message = f"Extensão de arquivo inválida."
        logger.log_error(message)

    @staticmethod
    def judge_output_lines_number(output_lines: int, solution_lines: int) -> None:
        message = f"Wrong answer.\n\n" \
                  f"O número de linhas produzidas difere.\n\n" \
                  f"Linhas produzidas: {output_lines}\n" \
                  f"Linhas esperadas: {solution_lines}"
        logger.log_judge(message)

    @staticmethod
    def judge_wrong_answer(output_line: str, solution_line: str) -> None:
        message = f"Wrong answer.\n\n" \
                  f"Linha produzida x linha esperada:\n\n" \
                  f"{output_line}\n{'^' * len(output_line)}\n\n" \
                  f"{solution_line}\n{'^' * len(solution_line)}"
        logger.log_judge(message)

    @staticmethod
    def judge_accepted_answer() -> None:
        message = f"ACCEPTED!"
        logger.log_judge(message)
