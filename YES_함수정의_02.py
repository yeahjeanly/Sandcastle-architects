def favorate_color(name, color, amount) :

    if (amount == 1) :
        print('%s 님은 %s을 좋아하지 않습니다.' % (name, color))
    elif (amount == 2) :
        print('%s 님은 %s을 조금 좋아합니다.' % (name, color))
    else :
        print('%s 님은 %s을 매우 좋아합니다.' % (name, color))

favorate_color('이미나', '빨강', 1)
favorate_color('조충범', '노랑', 2)
favorate_color('이예영', '파랑', 3)
