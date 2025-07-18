# balance : 초기 잔액을 설정하는 변수를 초기화해주세요.
# 금액은 여러분 마음대로 설정해주세요

# 사용자로부터 atm 기계에 사용 목적에 맞는 기능을 선택할 수 있도록
# 기능 입력을 받는 기능을 구현해주세요.

balance = 10000
# 사용하기 위해 미리 만드는것, 초기화 특정값을 넣어 만들거나, 빈 값을 넣어서 만듭니다.
receipts = []

while True:
    num = input("사용하실 기능의 번호를 입력해주세요. (1.입금, 2.출금, 3.영수증 보기, 4.종료) : ")

    if num == '4': # 4번은 종료 기능
        break # while문 탈출
    
    if num == '1': #입금 기능 구현 -> feat/deposit 브랜치에서 작업
       deposit_amount = int(input('입금할 금액을 입력해주세요: ')) #str:5000 -> int:5000
       balance += deposit_amount # balance = balance + deposit_amount
       print(f'입금하신 금액은{deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.')    
       # 보안 문제
       receipts.append(('입금', deposit_amount, balance))

    if num == '2':
        withdraw_amount = int(input('출금할 금액을 입력해주세요:'))
        withdraw_amount = min(balance,withdraw_amount)
        balance -= withdraw_amount # balance = balance - deposit_amount
        print(f'출금하신 금액은{withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.')
        receipts.append(('출금', withdraw_amount, balance))
    
    if num == '3':
        if receipts:
            for i in receipts:
            # i = ('입금'. 3000. 13000)
            # i[0] ==> '입금"
                print(f'{i[0]}: {i[1]}원 | 잔액: {i[2]}')
        else:
            print('영수증 내역이 없습니다.')    
print(f'서비스를 종료합니다. 햔재 잔액은 {balance}원 입니다.'4