def is_perfect(n: int) -> bool:
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def perfect_in_range(start: int, end: int):
    result = []
    for i in range(start, end + 1):
        if is_perfect(i):
            result.append(i)
    return result

if __name__ == "__main__":
    start = int(input("Başlanğıc ədəd: "))
    end = int(input("Son ədəd: "))
    print("Perfect rəqəmləri:", perfect_in_range(start, end))
