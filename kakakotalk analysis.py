filename = "카카오톡.txt"  # 카톡 내용 불러오기
kt_file = open(filename, 'r', encoding='utf8')
kt_file_content = kt_file.readlines()
kt_file.close()

dict1 = dict()                             # 딕셔너리 만들기 -> key 값이 이름, value가 대화 내용
kt_file_content = kt_file_content[4:]      # 첫 4줄 -> 불필요

name = ''                                  # 한 개의 카카오톡 채팅 내에 줄바꿈을 한 경우
for line in kt_file_content:               
    if line.count('-') == 30:              # 불필요한 요소들 삭제
        continue
    if '님이 나갔습니다.' in line:
        continue
    if '님을 초대하였습니다.' in line:
        continue
    if '[' in line:                         # 구조가 이미 한 줄 띄어쓰기간 된 상태라 스트립으로 줄 간격 줄여주고
        line = line.strip('\n').split('] ') # '] '을 기준으로 나눠주기
        name = line[0][1:]                  # 이름은 첫 번째가 이름이고, 1인 이유 -> [ 땜에
        data = "] ".join(line[2:])          # 혹시라도 '] ' 가 포함된 채팅이 있을 경우 대비
        if name in dict1:                   # 이름이 딕셔너리에 있는 경우  
            dict1[name].append(data)        # 대화 내용에 추가
        else:                          
            dict1[name]=[data]              # 딕셔너리에 공간을 넣는다
    else:
        dict1[name][-1] += line.strip('\n') # 이 경우 리스트 마지막에 추가하고, 줄바꿈을 없애주기

#제시어 리스트
swearlist = ['ㅅㅂ', 'ㅆㅂ', '시발', '씨발', '시이발', 'ㅅ발', 'ㅂㅅ', 'ㅈㄹ','존나','ㅈㄴ']  
laughlist = ['ㅋ', 'ㅋㅎ', 'ㅎㅋ' 'ㅎㅎ']
crylist = ['ㅜ' , 'ㅠ', 'ㅜ.ㅜ']

# 시작!
while True:                             # 계속해서 반복해서 쓰기 위해서 while 사용
    start = input('검색할 단어: ')       # 처음에 입력할 단어 

    if start == '\swear':               # 입력한 단어가 \swear 일때
        for i in dict1:                 # 키값(이름)이 딕셔너리에 있을때
            swearcount = 0             
            for l in swearlist:         # l(욕설)이 리스트에 있는 경우
                for text in dict1[i]:   # 누군가의 채팅 기록이 텍스트
                    if l in text:       # 욕설이 텍스트에 있으면
                        swearcount += 1 # 개수 +1
            print(i, swearcount)        # 욕설 개수 총 프린트 해주기

    elif start == '\laugh':
        for i in dict1:
            laughcount = 0
            for l in laughlist:
                for text in dict1[i]:
                    if l in text:
                        laughcount += 1
            print(i, laughcount)
            
    elif start == '\cry':
        for i in dict1:
            crycount = 0
            for l in crylist:
                for text in dict1[i]:
                    if l in text:
                        crycount += 1
            print(i, crycount)

    elif start == '\\talk':            # \t로 쓰는 경우 escape sequence로 처리되서 \\t로
        for i in dict1:                # 이하는 위와 동일
            talkcount = 0
            for l in dict1[i]:
                talkcount += 1
            print(i, talkcount)

    elif start == '\stop':            # 종료를 원하는 경우 \stop을 입력하면 종료
        print('종료합니다!')
        break

    else:                             # 단어를 입력 -> 개수
        for i in dict1:
            wordcount = 0
            for l in dict1[i]:
                if start in l:
                        wordcount += 1
            print(i, wordcount)
            