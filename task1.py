from pathlib import Path

def total_salary(path: str) -> tuple[str, str] | None:
    p = Path(path)
    if not p.exists():
        print('Path does not exist')
        return None

    if p.is_dir():
        print('Path is not a file')
        return None

    total = 0;
    lines = 0;
    with open(path, 'r') as fh:
        while True:
            line = fh.readline()
            if not line:
                break

            raw = line.split(',')[1]
            try:
                salary = float(raw)
                total += salary
                lines += 1
            except ValueError:
                salary = 0

    fh.close()

    return (f"{total:.2f}", f"{total / lines:.2f}") if lines else None

print(total_salary('salary.txt'))
