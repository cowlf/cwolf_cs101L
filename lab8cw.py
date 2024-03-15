tasklist = []
#Function that allows the addition of tasks
def addtask():
    print('enter the task:')
    newtask = input()
    tasklist.append({'taskdesc':newtask,'Complete':'false','Priority':None})
    return tasklist
#This function allows user to select a task to mark as complete
def markcomplete():
    print(f"To- Do list:\n")
    if not tasklist:
        print('No tasks to display.')
    else:
        for t in tasklist:
            print(f"{tasklist.index(t)}. {tasklist[tasklist.index(t)]['taskdesc']}")
        mcheck = 0
        while mcheck != 1:
            markc = int(input('Enter index of task to mark as complete:\n'))
            try:
                tasklist[markc]['Complete'] = 'true'
                print('Task marked as complete.')
                return tasklist
                mcheck = 1
            except:
                print('Please enter a valid index.')
#Prints a list of all tasks, along with relevant information about them
def viewlist():
    print(f"To- Do list:\n")
    if not tasklist:
        print('No tasks to display.')
    for t in tasklist:
        print(f"{tasklist.index(t)}. {tasklist[tasklist.index(t)]['taskdesc']}", end = '')
        if t['Complete'] == 'false':
            print(f"- Pending", end = '')
        else:
            print(f"- Complete", end = '')
        if t['Priority'] != None:
            print(f"- {tasklist[tasklist.index(t)]['Priority']}")
        else:
            print()
#Allows user to change task priority
def prioritize():
    print(f"To- Do list:\n")
    for t in tasklist:
        print(f"{tasklist.index(t)}. {tasklist[tasklist.index(t)]['taskdesc']}", end = '')
        if t['Complete'] == 'false':
            print(f"- Pending", end = '')
        else:
            print(f"- Complete", end = '')
        if t['Priority'] != None:
            print(f"- {tasklist[tasklist.index(t)]['Priority']}")
        else:
            print()
    pindexcheck = 0
    while pindexcheck != 1:
        targettask = int(input('Enter index of task to prioritize:\n'))
        try:
            pcheck = 0
            while pcheck != 1:
                print(f"Selected task: {tasklist[targettask]['taskdesc']}")
                newpriority = input('Enter new priority level(high, medium, low):\n')
                newlower = newpriority.lower()
                if newlower == 'high':
                    tasklist[targettask]['Priority'] = newpriority
                    print('Task priority updated.')
                    return tasklist
                    pcheck = 1
                elif newlower == 'medium':
                    tasklist[targettask]['Priority'] = newpriority
                    print('Task priority updated.')
                    return tasklist
                    pcheck = 1
                elif newlower == 'low':
                    tasklist[targettask]['Priority'] = newpriority
                    print('Task priority updated.')
                    return tasklist
                    pcheck = 1
                else:
                    print('Please enter high, medium, or low.')
        except:
            print('Please enter a valid index.')
#This function removes completed tasks
def removetask():
    print('Tasks to remove:')
    for t in tasklist:
        if t['Complete'] == 'true':
            print(f"{tasklist.index(t)}. {tasklist[tasklist.index(t)]['taskdesc']} - Removed")
            del tasklist[tasklist.index(t)]
    print('No completed tasks in list.')
    return tasklist

def mainmenu():
    selection = 0
    while selection != '6':
        print(f"Menu:\n"
              f"1. Add Task\n"
              f"2. Mark Task as Completed\n"
              f"3. View To- Do List\n"
              f"4. Prioritize Task\n"
              f"5. Remove Complete Tasks\n"
              f"6. Exit")
        selection = input('Please Enter your selection(1-6): ')
        if selection == '1':
            addtask()
        elif selection == '2':
            markcomplete()
        elif selection == '3':
            viewlist()
        elif selection == '4':
            prioritize()
        elif selection == '5':
            removetask()
        elif selection == '6':
            break
        else:
            print('Please enter a value 1-6.')
    print('Have a nice day.')

mainmenu()
