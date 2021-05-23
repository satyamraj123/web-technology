
struct process
{
    int pid, at;
    struct process *next;
} * current;
void add_process(int p, int a)
{
    struct process New = (struct process)malloc(sizeof(struct process));
    struct process *temp = current;
    New->pid = p;
    New->at = a;
    New->next = NULL;
    if (current == NULL)
    {
        current = New;
    }
    else
    {
        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = New;
    }
}
void remove_process(int p)
{
    struct process *temp = current;
    struct process *prev = current;
    int found = 0;
    while (temp != NULL)
    {
        if (temp->pid == p)
        {
            found = 1;
            if (temp == current)
            {
                current = current->next;
                free(temp);
                temp = current;
            }
            else
            {
                prev->next = temp->next;

                free(temp);
                temp = prev;
            }
        }
        prev = temp;
        temp = temp->next;
    }
    if (found == 0)
    {
        printf("Element not found\n");
    }
}
void display()
{
    struct process *temp = current;
    printf("PID\tArrival Time\n");
    while (temp != NULL)
    {
        printf("%d\t%d\n", temp->pid, temp->at);
        temp = temp->next;
    }
}
void fcfs()
{
    struct process *temp = current;
    struct process *t, *soonest;
    int tp, ta;
    while (temp != NULL)
    {
        t = temp;
        soonest = temp;
        while (t != NULL)
        {
            if ((t->at) < (soonest->at))
            {
                soonest = t;
            }
            t = t->next;
        }
        tp = temp->pid;
        ta = temp->at;
        temp->pid = soonest->pid;
        temp->at = soonest->at;
        soonest->pid = tp;
        soonest->at = ta;
        temp = temp->next;
    }
    while (current != NULL) //removes processes one-by-one, completing fcfs
    {
        printf("Process #%d is executing\n", current->pid);
        temp = current;
        current = current->next;
        free(temp);
    }
}

int main()
{
    int choice = 1, p, a;
    while (choice != 0)
    {
printf("Enter:\n\t1 to add a process to the list\n\t2 to remove a process from the

list\n\t3 to display process list\n\t4 to start FCFS schedule\n\t0 to EXIT\n");

scanf("%d",&choice);
switch(choice)
{
        case 1:
            printf("Enter PID : ");
            scanf("%d", &p);
            printf("\nEnter Arrival Time : ");
            scanf("%d", &a);
            printf("\n");
            add_process(p, a);
            break;
        case 2:
            printf("Enter PID : ");
            scanf("%d", &p);
            printf("\n");
            remove_process(p);
            break;
        case 3:
            printf("Current process list is:\n");
            display();
            break;
        case 4:
            printf("Starting FCFS :\n");
            fcfs();
            break;
        case 0:
            printf("EXITING\n");
            break;
        default:
            printf("Invalid Choice\n");

}
    }
    return 0;
}