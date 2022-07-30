#编写者:彭子涵
#编写时间:2022/4/29 14:58
# 更相减损法,求最大公约数
def gcf(a, b):
    # 减少倍数
    reduction = 1
    while True:
        # 可半者半之
        if a % 2 == 0 and b % 2 == 0:
            a //= 2
            b //= 2
            reduction *= 2
        else:
            # 不可半者
            break

    while True:
        # 副置分母、子之数，以少减多，更相减损，求其等也
        big = max(a, b)
        small = min(a, b)
        if small * 2 == big:
            return small * reduction
        else:
            a, b = small, big - small

a = gcf(1000, 200)
print(a)