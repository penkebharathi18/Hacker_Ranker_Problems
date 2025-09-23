def can_stack(blocks):
    l, r = 0, len(blocks) - 1
    top = float('inf')

    while l <= r:
        if blocks[l] >= blocks[r]:
            chosen = blocks[l]
            l += 1
        else:
            chosen = blocks[r]
            r -= 1

        if chosen <= top:
            top = chosen
        else:
            return "No"
    return "Yes"

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    blocks = list(map(int, input().split()))
    print(can_stack(blocks))
