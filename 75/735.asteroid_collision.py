def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []

    for aster in asteroids:
        if aster > 0:
            stack.append(aster)
        else:
            while stack and stack[-1] > 0 and stack[-1] < -aster:
                stack.pop()

            if stack[-1] == -aster:
                stack.pop()
            elif stack[-1] < 0 or not stack:
                stack.append(aster)
            else:
                pass    
    return stack

def asteroidCollision2(asteroids: list[int]) -> list[int]:
    stack = []

    for aster in asteroids:
        
        while stack and aster < 0 < stack[-1]:
                if stack[-1] < -aster:
                    stack.pop()
                    continue
                elif stack[-1] == -aster:
                    stack.pop()
                    break
        else: 
            stack.append(aster)
          
    return stack

print(asteroidCollision([1, 2 ,8,-8, 5, 10,-5]))

