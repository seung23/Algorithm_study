def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    stack = []
    for weight in people:
        print(stack)
        if stack and stack[-1] + weight <= limit:
            stack.pop()
            answer += 1
            print(answer)
            continue
        stack.append(weight)

    answer += len(stack)

    return answer