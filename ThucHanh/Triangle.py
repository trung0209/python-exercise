N=5

def ve_tam_giac_can(N: int):
    for i in range(N):
        count = 2 * (N - i - 1)
        count_star =  2 * i + 1
        space_str = str(" "*count)
        star_str = str( "*" *count_star)
        print(space_str + star_str)

ve_tam_giac_can(8)