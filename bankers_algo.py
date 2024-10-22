def is_safe(n, m, alloc, max, avail):
    need = [[max[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    f, ans, ind = [0] * n, [0] * n, 0

    for _ in range(n):
        for i in range(n):
            if not f[i] and all(need[i][j] <= avail[j] for j in range(m)):
                ans[ind], ind = i, ind + 1
                avail = [avail[j] + alloc[i][j] for j in range(m)]
                f[i] = 1
                break
        else:
            break  # Break if no process can proceed

    if ind == n:
        print("SAFE Sequence: ", ' -> '.join(f"P{ans[i]}" for i in range(n)))
    else:
        print("No SAFE Sequence found.")

if __name__ == "__main__":
    n, m = 5, 3
    alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    max = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    avail = [3, 3, 2]
    
    is_safe(n, m, alloc, max, avail)
