from pathlib import Path

SOL_FILE = Path('io/expected.sol')
OUTPUT_FILE = Path('io/output.txt')

LANGUAGES = {
    'cpp': (
        f"cd submissions",
        f"g++ bee.cpp -o run",
        f"run.exe < ../io/input.in > ../io/output.txt"
    ),
    'py': (
        f"cd submissions",
        f"py bee.py < ../io/input.in > ../io/output.txt"
    )
}