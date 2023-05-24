class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.__x1=x1
        self.__y1=y1
        self.__x2=x2
        self.__y2=y2
    def show(self):
        print(f'좌측 사단 꼭지점이 ({self.__x1},{self.__y1})이고 우측 하단 꼭지점이 ({self.__x2},{self.__y2})인 사각형입니다.')
    def getWidth(self):
        return self.__x2-self.__x1
    def getHeight(self):
        return self.__y2-self.__y1
    #자기 자신의 함수 멤버를 부를 때도 self를 사용해야한다 
    #getheight라고 썼는데 씹혔다 이거 맞냐?..
    def getArea(self):
        return (r1.getHeight())*(r1.getWidth())
    def getPerimeter(self):
        return (r1.getHeight())*2+(r1.getWidth())*2
r1=Rectangle(5,5,20,10)
a=r1.getArea()
p=r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')