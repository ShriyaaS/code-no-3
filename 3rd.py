from collections import deque

def bfs(n, m, num):
    
    q = deque()
    q.append(num)
    
    result = []
    
    
    while q:
        step_num = q.popleft()
        
        
        if n <= step_num <= m:
            result.append(step_num)
        
        
        if step_num == 0 or step_num > m:
            continue
        
        
        last_digit = step_num % 10
        
        
        step_num_a = step_num * 10 + (last_digit - 1)
        step_num_b = step_num * 10 + (last_digit + 1)
        
        
        if last_digit > 0:
            q.append(step_num_a)
        if last_digit < 9:
            q.append(step_num_b)
    
    return result

def findSteppingNumbers(n, m):
    result = []
    
    
    for i in range(10):
        result.extend(bfs(n, m, i))
    
    
    result.sort()
    return result


n = 100
m = 500


stepping_numbers = findSteppingNumbers(n, m)

if stepping_numbers:
    print("Stepping Numbers:", " ".join(map(str, stepping_numbers)))
else:
    print("No stepping numbers found in the range.")
