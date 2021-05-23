
def display(arrivedprocesses):
    print("Arrivedprocesses are-")
    for i in range(0, len(arrivedprocesses)):
        print(f"{arrivedprocesses[i].name}, {arrivedprocesses[i].rt}")


class Process:
    def __init__(self, name, at, bt):
        self.name = name
        self.at = at
        self.bt = bt
        self.rt = bt


if __name__ == "__main__":
    nameofp = ["P1", "P2", "P3", "P4"]
    at = [0, 1, 2, 4]
    bt = [5, 4, 2, 1]
    tq = 2  # timequantum
    n = len(nameofp)
    p = []
    for i in range(0, len(nameofp)):
        p.append(Process(nameofp[i], at[i], bt[i]))

    print("Processes" + " Burst time " +
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

    t = 0
    pcopy = p.copy()
    ganttchart = []
    timequeue = [0]
    arrivedprocesses = []  # readyqueue
    while(True):
        # arrive processes in ready queue
        i = 0
        while(i < len(pcopy)):
            if(t >= pcopy[i].at):
                arrivedprocesses.append(pcopy[i])
                pcopy.remove(pcopy[i])
                i = i-1
            i = i+1
        n = len(arrivedprocesses)
        if(arrivedprocesses == []):
            if(pcopy == []):
                break
            else:
                t = t+tq
                continue
        else:
            ganttchart.append(arrivedprocesses[0].name)
            if(arrivedprocesses[0].rt < tq):
                timequeue.append(arrivedprocesses[0].rt+timequeue[-1])
                arrivedprocesses[0].rt = 0
            else:
                timequeue.append(tq+timequeue[-1])
                arrivedprocesses[0].rt -= tq
            currentprocess = arrivedprocesses[0]
            arrivedprocesses.remove(arrivedprocesses[0])
            t = t+tq
            i = 0
            while(i < len(pcopy)):
                if(t >= pcopy[i].at):
                    arrivedprocesses.append(pcopy[i])
                    pcopy.remove(pcopy[i])
                    i = i-1
                i = i+1
            if(currentprocess.rt > 0):
                arrivedprocesses.append(currentprocess)

    print(ganttchart)
    print(timequeue)
    n = len(p)
    ct = [0]*n
    wt = [0]*n
    ftcpu = [0]*n
    tat = [0]*n
    for i in range(0, n):
        pname = p[i].name
        for j in range(0, len(ganttchart)):
            if(ganttchart[j] == p[i].name):
                ct[i] = timequeue[j+1]
        tat[i] = ct[i]-p[i].at
        wt[i] = tat[i]-p[i].bt

    print("Processes"+" Burst time " +
          " Arrival Time" + " Completion Time"+" Waiting Time"+" TurnAround Time")
    for i in range(n):
        print(" " + str(p[i].name) + "\t\t" +
              str(p[i].bt) + "\t\t" +
              str(p[i].at) + "\t "+str(ct[i]) + "\t\t" +
              str(wt[i]) + "\t\t" +
              str(tat[i]) + "\t ")
