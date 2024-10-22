def main():
    n = int(input("Enter number of processes: "))
    processes = [[i + 1, int(input(f"P{i+1} Burst Time: ")), 0, 0] for i in range(n)]
    
    # Sort by Burst Time (BT)
    processes.sort(key=lambda x: x[1])
    
    total_wt = 0
    for i in range(1, n):
        processes[i][2] = processes[i-1][2] + processes[i-1][1]  # Waiting time
        total_wt += processes[i][2]
    
    avg_wt = total_wt / n
    
    total_tat = 0
    for i in range(n):
        processes[i][3] = processes[i][1] + processes[i][2]  # Turnaround time
        total_tat += processes[i][3]
    
    avg_tat = total_tat / n

    print("P\tBT\tWT\tTAT")
    for p in processes:
        print(f"P{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}")
    
    print(f"Average Waiting Time= {avg_wt}")
    print(f"Average Turnaround Time= {avg_tat}")

if __name__ == "__main__":
    main()
