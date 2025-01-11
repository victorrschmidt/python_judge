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