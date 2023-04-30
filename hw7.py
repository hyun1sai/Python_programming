fruit={}
print("구입")
name=0
while True:    
    name=input("상품명? ")
    if name=="":
        break
    n=int(input("수량은? "))
    fruit[name]=n
    print(f'장바구니에 {name} {n}개가 담겼습니다.')
    print()
print(f'>>> 장바구니 보기:{fruit}')
print()
print("[검색]")
i=input("장바구니에서 확인하고자 하는 상품은?")
if i in fruit:
    print(f'{i}은(는) {fruit[i]}개 담겨 있습니다.')


