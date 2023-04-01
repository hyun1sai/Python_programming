def draw_line_string(name):
    msg1="hello "+name+","
    msg2="Welcom to Seoul."
    nstr=0
    if len(msg1)>len(msg2):
        nstr=len(msg1)
    else:
        nstr=len(msg2)
    print((nstr*"-")+"--")
    print(f' {msg1:s}')
    print(f' {msg2:s}')
    print((nstr*"-")+"--")
name=input("Input his/her name: ")
draw_line_string(name)
