loc_1, loc_2, loc_3, loc_4, = 1, 2, 3, 4
history = []
goal = 24
goal_c = goal-1+0.99999999999999
value_1 = int(input("enter value 1: "))
value_2 = int(input("enter value 2: "))
value_3 = int(input("enter value 3: "))
value_4 = int(input("enter value 4: "))
v2b = value_2
v1b = value_1
v3b = value_3
v4b = value_4

def solve(num, op, num_1):
    if op == 1:
        return num + num_1
    elif op == 2:
        return num - num_1
    elif op == 3:
        return num * num_1
    elif op == 4:
        return num / num_1

def place(value):
    if value == 1:
        return v1b
    elif value == 2:
        return v2b
    elif value == 3:
        return v3b
    elif value == 4:
        return v4b

def op_translate(op):
    if op == 1:
        return "+"
    elif op == 2:
        return "-"
    elif op == 3:
        return "*"
    elif op == 4:
        return "/"

def add_digit():
    global loc_1
    global loc_2
    global loc_3
    global loc_4
    loc_4 += 1
    if loc_4 > 4:
        loc_3 += 1
        loc_4 = 1
    if loc_3 > 4:
        loc_2 += 1
        loc_3 = 1
    if loc_2 > 4:
        loc_1 += 1
        loc_2 = 1
    if loc_1 != loc_2 and loc_1 != loc_3 and loc_1 != loc_4 and loc_2 != loc_3 and loc_2 != loc_4 and loc_3 != loc_4:
        pass
    else:
        add_digit()
    

op1, op2, op3 = 1, 1, 1

while op1 <= 4:
    #possible solutions
    try: 
        solution_1 = solve(solve(solve(value_1, op1, value_2), op2, value_3), op3, value_4)
    except ZeroDivisionError:
        solution_1 = "N/A"

    try: 
        solution_2 = solve(solve(value_1, op3, value_2), op1, solve(value_3, op2, value_4))
    except ZeroDivisionError:
        solution_2 = "N/A"
        
    try:
        solution_3 = solve(value_1, op3, solve(value_2, op2, solve(value_3, op1, value_4)))
    except ZeroDivisionError:
        solution_3 = "N/A"
    
                        

    #Add solution to history
        
    if solution_1 == goal or solution_1 == goal_c:
        if history.count(str(value_1)+str(op_translate(op1))+str(value_2)+str(op_translate(op2))+str(value_3)+str(op_translate(op3))+str(value_4)) !=1:
            history.append(str(value_1)+str(op_translate(op1))+str(value_2)+str(op_translate(op2))+str(value_3)+str(op_translate(op3))+str(value_4))

    if solution_2 == goal or solution_2 == goal_c:
        if history.count('('+str(value_1)+str(op_translate(op3))+str(value_2)+')'+str(op_translate(op1))+'('+str(value_3)+str(op_translate(op2))+str(value_4)+')') !=1:
            history.append('('+str(value_1)+str(op_translate(op3))+str(value_2)+')'+str(op_translate(op1))+'('+str(value_3)+str(op_translate(op2))+str(value_4)+')')
            
    if solution_3 == goal or solution_3 == goal_c:
        if history.count(str(value_1)+str(op_translate(op3))+'('+str(value_2)+str(op_translate(op2))+'('+str(value_3)+str(op_translate(op1))+str(value_4)+'))') != 1:              
            history.append(str(value_1)+str(op_translate(op3))+'('+str(value_2)+str(op_translate(op2))+'('+str(value_3)+str(op_translate(op1))+str(value_4)+'))')
    
    op3+=1
    if op3>4:
        op2+=1    
        op3=1
    if op2>4:
        op1+=1
        op2=1
        
    if op1 == 5:
        add_digit()
        value_1, value_2, value_3, value_4 = place(loc_1), place(loc_2), place(loc_3), place(loc_4)
        op1, op2, op3 = 1, 1, 1
                
    if loc_1 == 5:
        op1=5 #end count
        print("Solution(s): ")
        print("-------------------")
#if no solution
if len(history) == 0:
    print("No Solution(Ø)")

#print solutions
item_no = 1
for item in history:
    print(str(item_no)+'. '+item)
    item_no +=1
    
do_next=input(">")
