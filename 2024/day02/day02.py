# Generated on 02-12-2024 18:42
# --- Day 2: Red-Nosed Reports ---

def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip().split(" ") for line in f.readlines()]
    return values

def allowed_value_check(x: int, y: int):
    n_max =max(x,y)
    n_min = min(x,y)
    for i in range(1, 4):
        if n_min + i == n_max:
            return True
    return False

def is_safe_increase(report):
    is_safe = False
    i = 1
    total = len(report)
    print(total)
    for x in range(0, total):
        print(x)
        if x + 1 == total:
            break
        if report[x] < report[x + 1] and allowed_value_check(report[x], report[x + 1]):
            i += 1
            continue
        else:
            break
    print(i)
    if i == total:
        is_safe = True
    return is_safe

def is_safe_decrease(report):
    is_safe = False
    i = 1
    total = len(report)
    print(total)
    for x in range(0, total):
        print(x)
        if x + 1 == total:
            break
        if report[x] > report[x + 1] and allowed_value_check(report[x], report[x + 1]):
            i += 1
            continue
        else:
            break
    print(i)
    if i == total:
        is_safe = True
    return is_safe


def is_safe(report) -> bool:
    return is_safe_increase(report) or is_safe_decrease(report)


def part_one(file: str):
    total_safe_reports = 0
    raw_data = get_raw_data(file)
    reports_solution = {}

    print(raw_data)
    for i, reports in enumerate(raw_data, 1):
        print(f"Report {i}")
        report = []
        for level in reports:
            report.append(int(level))

        reports_solution[i] = {"list": report,
                               "is_safe": is_safe(report)}

    print(reports_solution)
    for k, v in reports_solution.items():
        if v["is_safe"]:
            total_safe_reports += 1

    print(f"How many reports are safe? {total_safe_reports}")

def part_two(file: str):
    raw_data = get_raw_data(file)

    for value in raw_data:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")