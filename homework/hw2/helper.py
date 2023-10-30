for x in range(1, 8_000_000):
    power = 1
    while True:
        if power == 8 and (x * power) % 8_000_000 == 0:
            print(x)
            break
        if (x * power) % 8_000_000 == 0:
            break
        if power == 8:
            break
        power += 1
