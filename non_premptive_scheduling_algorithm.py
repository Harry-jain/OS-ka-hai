totalprocess = 5
proc = []

def get_times(wt, tat):
    service = [0] * totalprocess
    wt[0] = 0
    for i in range(1, totalprocess):
        service[i] = proc[i - 1][1] + service[i - 1]
        wt[i] = max(service[i] - proc[i][0] + 1, 0)
    for i in range(totalprocess):
        tat[i] = proc[i][1] + wt[i]

def findgc():
    wt, tat = [0] * totalprocess, [0] * totalprocess
    get_times(wt, tat)
    stime, ctime = [1], [tat[0] + 1]
    for i in range(1, totalprocess):
        stime.append(ctime[i - 1])
        ctime.append(stime[i] + tat[i] - wt[i])

    wavg = sum(wt) / totalprocess
    tavg = sum(tat) / totalprocess
    print("Process\tStart\tComplete\tTAT\tWT")
    for i in range(totalprocess):
        print(f"{proc[i][3]}\t{stime[i]}\t{ctime[i]}\t{tat[i]}\t{wt[i]}")
    print(f"Avg waiting time: {wavg:.2f}, Avg TAT: {tavg:.2f}")

if __name__ == "__main__":
    for i in range(totalprocess):
        arrival = int(input(f"Process {i+1} Arrival Time: "))
        burst = int(input(f"Process {i+1} Burst Time: "))
        pri = int(input(f"Process {i+1} Priority: "))
        proc.append([arrival, burst, pri, i + 1])

    proc.sort(key=lambda x: (x[2], x[0]))  # Sort by priority and arrival
    findgc()
