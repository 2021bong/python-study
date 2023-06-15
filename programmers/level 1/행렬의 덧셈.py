def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j] + arr2[i][j])

    return answer
# print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
# print(solution([[1], [2]], [[3], [4]]))


# 다른 사람 풀이 -> zip을 써도 됐을 듯하다
def sumMatrix(A, B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    return answer
