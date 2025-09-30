def is_armstrong(n: int) -> bool:
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

def armstrong_in_range(start: int, end: int):
    result = []
    for i in range(start, end + 1):
        if is_armstrong(i):
            result.append(i)
    return result

if __name__ == "__main__":
    start = int(input("Başlanğıc ədəd: "))
    end = int(input("Son ədəd: "))
    print("Armstrong rəqəmləri:", armstrong_in_range(start, end))
