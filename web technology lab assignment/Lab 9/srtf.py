
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
    nameofp = ["P1", "P2", "P3", "P4", "P5", "P6"]
    at = [0, 1, 2, 3, 4, 5]
    bt = [8, 4, 2, 1, 3, 2]
    n = len(nameofp)
    p = []
    for i in range(0, len(nameofp)):
        p.append(Process(nameofp[i], at[i], bt[i]))

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

    t = 0
    pcopy = p.copy()
    ganttchart = []
    arrivedprocesses = []
    while(True):
        i = 0
        while(i < len(pcopy)):
            if(t >= pcopy[i].at):
                arrivedprocesses.append(pcopy[i])
                pcopy.remove(pcopy[i])
                i = i-1
            i = i+1

        n = len(arrivedprocesses)
        for i in range(0, n):
            for j in range(0, n-i-1):
                if(arrivedprocesses[j].rt > arrivedprocesses[j+1].rt):
                    temp = arrivedprocesses[j]
                    arrivedprocesses[j] = arrivedprocesses[j+1]
                    arrivedprocesses[j+1] = temp

        if(arrivedprocesses == []):
            if(pcopy == []):
                break
            else:
                t = t+1
                continue
        else:
            ganttchart.append(arrivedprocesses[0].name)
            arrivedprocesses[0].rt -= 1
            if(arrivedprocesses[0].rt == 0):
                arrivedprocesses.remove(arrivedprocesses[0])
            t = t+1

    print(ganttchart)
    n = len(p)
    ct = [0]*n
    wt = [0]*n
    ftcpu = [0]*n
    tat = [0]*n
    for i in range(0, n):
        pname = p[i].name
        for j in range(0, len(ganttchart)):
            if(ganttchart[j] == p[i].name):
                ct[i] = j+1
        wt[i] = ct[i]-p[i].at
        for j in range(0, len(ganttchart)):
            if(ganttchart[j] == p[i].name):
                ftcpu[i] = j
                break
        tat[i] = ct[i]-ftcpu[i]

    print("Processes Burst time " +
          " Arrival Time" + " Completion Time"+" Waiting Time"+" TurnAround Time")
    for i in range(n):
        print(" " + str(p[i].name) + "\t\t" +
              str(p[i].bt) + "\t\t" +
              str(p[i].at) + "\t "+str(ct[i]) + "\t\t" +
              str(wt[i]) + "\t\t" +
              str(tat[i]) + "\t ")
