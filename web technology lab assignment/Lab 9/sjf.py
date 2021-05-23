
def findWaitingTime(processes, wt):
    wt[0] = 0
    for i in range(1, len(processes)):
        if(processes[i-1].bt + processes[i-1].at < processes[i].at):
            wt[i] = 0
        else:
            wt[i] = processes[i-1].at + processes[i-1].bt + \
                wt[i - 1] - processes[i].at


def findTurnAroundTime(processes, wt, tat):
    for i in range(len(processes)):
        tat[i] = processes[i].bt + wt[i]


def findavgTime(processes):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    findWaitingTime(processes, wt)
    findTurnAroundTime(processes, wt, tat)
    print("Processes Burst time " +
          " Arrival Time"
          " Waiting time " +
          " Turn around time")
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(processes[i].name) + "\t\t" +
              str(processes[i].bt) + "\t\t" +
              str(processes[i].at) + "\t " +

              str(wt[i]) + "\t\t " +
              str(tat[i]))
    print("Average waiting time = " +
          str(total_wt / n))
    print("Average turn around time = " +
          str(total_tat / n))


class Process:
    def __init__(self, name, at, bt):
        self.name = name
        self.at = at
        self.bt = bt


if __name__ == "__main__":
    nameofp = [1, 2, 3]
    at = [5, 5, 9]
    bt = [5, 2, 8]
    n = len(nameofp)
    p = []
    for i in range(0, len(nameofp)):
        p.append(Process(nameofp[i], at[i], bt[i]))
        print(p[i].at)
    print("Processes Burst time " +
          " Arrival Time")
    for i in range(n):
        print(" " + str(p[i].name) + "\t\t" +
              str(p[i].bt) + "\t\t" +
              str(p[i].at) + "\t ")
    # sort
    for i in range(0, n):
        for j in range(0, n-i-1):
            if(p[j].at > p[j+1].at):
                temp = p[j]
                p[j] = p[j+1]
                p[j+1] = temp
            elif(p[j].at == p[j+1].at):
                if(p[j].bt > p[j+1].bt):
                    temp = p[j]
                    p[j] = p[j+1]
                    p[j+1] = temp
    findavgTime(p)
