# 1<= E <=15 15
# 1<= S <=28 28
# 1<= M <=19 19


earth, sun, moon = map(int, input().split())
total = 0
earth_num = 0
sun_num = 0
moon_num = 0
while True:
    if earth == earth_num and sun == sun_num and moon == moon_num:
        print(total)
        break

    else:
        earth_num += 1
        sun_num += 1
        moon_num += 1
        total += 1

        if earth_num == 16:
            earth_num = 1
        if sun_num == 29:
            sun_num = 1
        if moon_num == 20:
            moon_num = 1
