def main():
    counts = {}

    try:
        while True:
            item = input().strip()
            if item == False:
                continue
            item = item.lower()

            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
    except EOFError:
        pass
    for x in sorted(counts.keys()):
        print(f"{counts[x]} {x.upper()}")
main()
