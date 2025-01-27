def solve_tightrope_stage1(s):
    left_tilt = 0
    right_tilt = 0
    for move in s:
        if move == 'L':
            if right_tilt > 0:
                right_tilt -= 1
            else:
                left_tilt += 1
        elif move == 'R':
            if left_tilt > 0:
                left_tilt -= 1
            else:
                right_tilt += 1

        if left_tilt > 3 or right_tilt > 3:
            return "YOU LOST"
    return "GOAL"
s = input()
result = solve_tightrope_stage1(s)
print(result)