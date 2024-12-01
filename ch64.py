def tower(n, source, auxiliary, target):
    if n == 1:
        move_disk(source, target)
        print_towers()
        return 1
    else:
        count1 = tower(n-1, source, target, auxiliary)
        move_disk(source, target)
        print_towers()  
        count2 = tower(n-1, auxiliary, source, target)
        return count1 + count2 + 1

def move_disk(source, target):
    disk = source.pop()
    target.append(disk)

def print_towers():
    print('|  |  |')
    for i in range(n - 1, -1, -1):
        count=0
        for tower in [source, auxiliary, target]:
            if i < len(tower):
                if count==3:
                    print(tower[i], end='')
                    # count+=1
                else:
                    count+=1
                    if count==3:
                        print(tower[i], end='')
                    else:
                        print(tower[i], end='  ')
                    
            else:
                count+=1
                if count==3:
                    print('|', end='')
                else:
                    print('|', end='  ')
                
            
        print()
    if len(toprint)!=0:
        for i in range(len(toprint)):
            print(toprint[0])
            toprint.pop(0)
            break

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print_move(source, target, n)
        return 1
    else:
        count1 = tower_of_hanoi(n-1, source, target, auxiliary)
        print_move(source, target, n)
        count2 = tower_of_hanoi(n-1, auxiliary, source, target)
        return count1 + count2 + 1

def print_move(source, target, disk):
    toprint.append(f"move {disk} from  {source} to {target}")

print(' *** Tower of Hanoi ***')
n = int(input("Enter Input : "))
source = [i for i in range(n, 0, -1)]
auxiliary = []
target = []
toprint=[]
count=0
total_moves = tower_of_hanoi(n, 'A', 'B', 'C')
print_towers()
tower(n, source, auxiliary, target)
print(f"Total moves = {total_moves}")