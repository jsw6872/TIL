def solution(new_id):
    allow_list = ['-', '_', '.']
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2
    for char in new_id:
        if char.isalpha() or char.isalnum() or char in allow_list:
            answer += char
    # 3
    while '..' in answer:
        answer = answer.replace('..','.')
    #4 빈 문자열일 때 슬라이싱이 안 된다
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5
    if answer == '':
        answer = answer.replace('','a')
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer

def main():
    ex_list = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]
    sol_list = ["bat.y.abcdefghi", "z--", "aaa", "123_.def", "abcdefghijklmn"]

    for id in range(len(ex_list)):
      if solution(ex_list[id]) == sol_list[id]:
        print('Correct')
      else:
        print('Incorrect')
      
if __name__ == '__main__' :
    main()