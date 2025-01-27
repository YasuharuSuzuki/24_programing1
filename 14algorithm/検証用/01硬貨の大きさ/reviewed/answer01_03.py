okaneA, okaneB = map(int, input().split())
okaneA_ookisa = 0
okaneB_ookisa = 0

match okaneA:
    case 1:
        okaneA_ookisa = 20.0
    case 5:
        okaneA_ookisa = 22.0
    case 10:
        okaneA_ookisa = 23.5
    case 50:
        okaneA_ookisa = 21.0
    case 100:
        okaneA_ookisa = 22.3
    case 500:
        okaneA_ookisa = 26.5

match okaneB:
    case 1:
        okaneB_ookisa = 20.0
    case 5:
        okaneB_ookisa = 22.0
    case 10:
        okaneB_ookisa = 23.5
    case 50:
        okaneB_ookisa = 21.0
    case 100:
        okaneB_ookisa = 22.3
    case 500:
        okaneB_ookisa = 26.5

if okaneA_ookisa == okaneB_ookisa:
    print("同じ")
elif okaneA_ookisa > okaneB_ookisa:
    print("A")
else:
    print("B")
