def num2eng(num):
    english_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                   'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                   'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
                   'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
                   'hundred', 'thousand']
    hundred = english_num[-2]
    thousand = 'one-' + english_num[-1]
    gap = 18

    if 0 <= num <= 19:
        return english_num[num]
    elif num in range(20, 100, 10):
        return english_num[num // 10 + gap]
    elif num == 100:
        return hundred
    elif num == 1000:
        return thousand

print "Please input numbers to test, -1 to end: "
while True:
    numStr = raw_input('input_num = ')
    input_num = int(numStr)
    if input_num == -1:
        break
    elif input_num < 0 or input_num > 1000:
        print "Wrong number input, should be in 0 to 1000"
        continue
    elif input_num == 1000:
        eng = num2eng(input_num)
    else:
        length = len(numStr)
        if length == 1:
            numStr = '00' + numStr
        elif length == 2:
            numStr = '0' + numStr
        i = int(numStr[0])
        j = int(numStr[1])
        k = int(numStr[2])
        if length == 3:
            if j == 0:
                eng = num2eng(i) + '-hundred-' + num2eng(k)
                if k == 0:
                    eng = eng[:len(eng) - 5]
            elif j == 1:
                newNum = j * 10 + k
                eng = num2eng(i) + '-hundred-' + num2eng(newNum)
            else:
                newNum = j * 10
                eng = num2eng(i) + '-' + 'hundred-' + num2eng(newNum) + '-' + num2eng(k)
                if k == 0:
                    eng = eng[:len(eng) - 5]
        elif length == 2:
            if j == 1:
                newNum = j * 10 + k
                eng = num2eng(newNum)
            else:
                newNum = j * 10
                eng = num2eng(newNum) + '-' + num2eng(k)
                if k == 0:
                    eng = eng[:len(eng) - 5]
    print eng
