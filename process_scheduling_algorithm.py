def findWaitingTime(n, bt, wt, quantum):
    rem_bt = bt[:]
    t = 0  # Current time

    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done:
            break

def findTurnAroundTime(n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findCompletionTime(n, bt, wt, completion_time):
    for i in range(n):
        completion_time[i] = wt[i] + bt[i]

def findavgTime(n, bt, quantum):
    wt, tat, completion_time = [0] * n, [0] * n, [0] * n

    findWaitingTime(n, bt, wt, quantum)
    findTurnAroundTime(n, bt, wt, tat)
    findCompletionTime(n, bt, wt, completion_time)

    print("P\tBT\tWT\tTAT\tCT")
    total_wt = total_tat = total_ct = 0

    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        total_ct += completion_time[i]
        print(f"{i + 1}\t{bt[i]}\t{wt[i]}\t{tat[i]}\t{completion_time[i]}")

    print(f"\nAverage waiting time = {total_wt / n:.5f}")
    print(f"Average turn around time = {total_tat / n:.5f}")
    print(f"Average completion time = {total_ct / n:.5f}")

if __name__ == "__main__":
    n = 3
    burst_time = [10, 5, 8]
    quantum = 2
    findavgTime(n, burst_time, quantum)
