def buy(shopping_bag):
    print("[구입]")
    item = input("상품명? ")
    if item == "":
        return False  
    amount = int(input("수량은? "))
    
    if item in shopping_bag:
        shopping_bag[item] += amount  
    else:
        shopping_bag[item] = amount 

    print(f"장바구니에 {item} {amount}개가 담겼습니다.\n")
    return True

def show(shopping_bag):
    print(">>> 장바구니 보기:", shopping_bag)
    print()

def find(shopping_bag):
    print("[검색]")
    item = input("장바구니에서 확인하고자 하는 상품은? ")
    if item in shopping_bag:
        print(f"장바구니에 {item}(는) {shopping_bag[item]}개 담겨 있습니다.\n")
    else:
        print(f"장바구니에 {item}(는) 없습니다.\n")


shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break

show(shopping_bag)
find(shopping_bag)
