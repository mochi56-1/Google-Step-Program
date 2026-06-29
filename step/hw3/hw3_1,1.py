#! /usr/bin/python3
#def read 数字や文字を読み込みtoken型を判断する

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index

def read_slash(line, index):
    token = {'type': 'SLASH'}
    return token, index + 1

def read_asterisk(line, index):
    token = {'type': 'ASTERISK'}
    return token, index + 1

def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1
#1+2*3
#tokens=[({'type':'NUMBER','number':1},0),({'type':'PLUS'},1),({'type':'NUMBER','number':2},2),
#({'type': 'ASTERISK'}, 3), ({'type': 'NUMBER', 'number': 3}, 4)]
def tokenize(line): #字句に分割　 入力 式の文字列　出力 字句を表すtokenのリスト}
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)#tokens[1] [1,+2] [1,+,2,*,3]
        elif line[index] == '+':
            (token, index) = read_plus(line, index)#tokens[1,+]
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '/':
            (token, index) = read_slash(line, index)
        elif line[index] == '*':
            (token, index) = read_asterisk(line, index)#[1,+,2,*]
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

tokens=[({'type':'NUMBER','number':1},0),({'type':'PLUS'},1),({'type':'NUMBER','number':2},2),({'type': 'ASTERISK'}, 3), ({'type': 'NUMBER', 'number': 3}, 4)]
def kakezann_warizan_evaluate(tokens):
    index=0
    while index < len(tokens):    
        if tokens[index]['type'] == 'ASTERISK': 
                num = tokens [index - 1] ['number' ] * tokens [index + 1] ['number' ]
                tokens [index - 1] = {'type': 'NUMBER', 'number': num}
                del tokens [index : index + 2]
                continue
        elif tokens [index] ['type'] == 'SLASH':
                divide = tokens [index + 1] ['number' ]
                if divide == 0:
                  print("Error")
                  exit(1)
                num = tokens [index - 1] ['number'] / divide
                tokens [index - 1] = {'type': 'NUMBER', 'number': num}
                del tokens [index : index + 2]
                continue
        index += 1
    return tokens
                

def evaluate(tokens): #字句の並びを計算　入力 字句を表すtokenのリスト　出力 計算結果
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':      
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer


def test(line):
    tokens = tokenize(line)
    tokens = kakezann_warizan_evaluate(tokens)
    actual_answer = evaluate(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
#テストケース
def run_test():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    test("3+2*6")
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input() #1行読む
    tokens = tokenize(line) #字句に分割
    kakezan_warizan_answer= kakezann_warizan_evaluate(tokens)
    answer = evaluate(tokens) #字句の並びを計算
    print("answer = %f\n" % answer)