def solution(s):
    s = s.replace('zero','0')
    s = s.replace('one','1')
    s = s.replace('two','2')
    s = s.replace('three','3')
    s = s.replace('four','4')
    s = s.replace('five', '5')
    s = s.replace('six','6')
    s = s.replace('seven','7')
    s = s.replace('eight','8')
    s = s.replace('nine','9')
    answer = int(s)
    return answer

def main():
    ex_list = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]
    sol_list = [1478, 234567, 234567, 123]
    for idx in range(len(ex_list)):
        if solution(ex_list[idx]) == sol_list[idx]:
            print('correct')
        else:
            print('incorrect')

if __name__ == '__main__':
      main()