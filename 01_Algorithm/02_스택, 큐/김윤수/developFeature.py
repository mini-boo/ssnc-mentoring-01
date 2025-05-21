from collections import deque
import math

def solution(progresses, speeds):
    answer = []

    speedsQueue = deque(speeds)
    progressQueue = deque(progresses)
    days = 0

    while progressQueue:
        currentProgress = progressQueue[0] + speedsQueue[0] * days

        if currentProgress < 100:
            remainDays = 100 - currentProgress
            needDays = math.ceil(remainDays / speedsQueue[0])
            days += needDays

        count = 0
        while progressQueue and progressQueue[0] + speedsQueue[0] * days >= 100:
            progressQueue.popleft()
            speedsQueue.popleft()
            count += 1

        if count > 0:
            answer.append(count)

    return answer