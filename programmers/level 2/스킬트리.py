# 다른 사람 풀이 1
def solution(skill, skill_trees):
    answer = 0
    sd = {k:v for v, k in enumerate(skill)} # {skill : skill index} {C : 0} 스킬과 인덱스로 객체 만듦

    for skill_tree in skill_trees: # skill_trees를 돌려서
        status = [False] * (len(skill)+1) # skill의 길이보다 하나 큰 False 배열 생성
        answer_flag = True
        for ch in skill_tree: # skill_tree 하나하나의 스킬들(C, B, D...)을 순회하며
            if ch in skill: # 해당 스킬이 skill에 있으면
                for idx in range(sd[ch]): # 해당 스킬의 배워야하는 순서만큼 반복문을 돌려서
                    if not status[idx]: # 그 이전에 배워야하는 스킬을 안배웠으면, 이전에 배워야하는 스킬을 배웠으면 True가 되어서 여기를 통과하지 못함
                        answer_flag = False # answer_flag를 False로 바꾸고
                status[sd[ch]] = True # 해당 스킬은 배웠다고 True로 표시

        if answer_flag:
            answer += 1
    return answer

# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "CAD", "Z"])) # 3


# 다른 사람 풀이 2
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill) # skill을 리스트로 변환

        for s in skills: # skill_trees의 요소(skills)를 한글자씩 돌면서
            if s in skill: # 해당 스킬이 skill에 있으면
                if s != skill_list.pop(0): # 그 스킬이 skill_list의 첫번째 요소와 같지 않을 때는 불가능하다고 판단
                    break
        else:
            answer += 1 # 같으면 가능하다고 판단, for-else문은 break가 실행되면 else를 실행하지 않음

    return answer


# 다른 사람 풀이 3
def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i: # skill_tree의 요소를 한글자씩 돌면서
            if z in skill: # skill에 있으면
                skillist+=z # skillist에 글자를 추가, skill_tree 요소의 글자 순서대로 글자를 추가하므로 불가능한 건 skill과 다르게 순서가 뒤집힘
        if skillist==skill[0:len(skillist)]: # skillist와 그 길이만큼의 skill이 똑같으면 가능하다고 판단
            answer+=1
    return answer