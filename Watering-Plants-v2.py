def solution(flowers: list, cap1: int, cap2: int) -> int:
    can1 = cap1
    can2 = cap2
    refill = 2

    for i in range(len(flowers)//2):
        if can1 < flowers[i]:
            can1 = cap1
            refill += 1
        can1 -= flowers[i]

        if can2 < flowers[-(i+1)]:
            can2 = cap2
            refill += 1
        can2 -= flowers[-(i+1)]

    if len(flowers) % 2 == 1:
        if (can1 + can2) < flowers[len(flowers)//2]:
            refill += 1
    return refill