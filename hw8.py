def buy(shopping_bag):
    print("[구입]")   
    name=input("상품명? ")
    if name=="":
        return False
    n=int(input("수량은? "))
    shopping_bag[name]=n
    print(f'장바구니에 {name} {n}개가 담겼습니다.')
    print()
def show(shopping_bag):
    print(f'>>> 장바구니 보기: {shopping_bag}')
def find(shopping_bag):
    print()
    print("[검색]")
    i=input("장바구니에서 확인하고자 하는 상품은?")
    if i in shopping_bag:
        print(f'{i}은(는) {shopping_bag[i]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {i}은(는) 없습니다.')

shopping_bag={}
while True:
    if buy(shopping_bag)==False:
        break
show(shopping_bag)
find(shopping_bag)

