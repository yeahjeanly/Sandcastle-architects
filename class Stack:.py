class Stack:
    def __init__(self):
        self.items = []
         
    
# 스택이 비어있는지 확인하는 메서드
    # 내 답안
    # def is_empty(self):
    #     return(len(self.items) == 0 )
    
    #  정답안
    def is_empty(self):
        return len(self.items) == 0 
    
# 추가하는 메서드 (PUSH)
    # 내 답안
    # def push(self):
    #     return self.append(items)
    
    # 정답안
    def push(self, item):
        self.items.append(item)
    
# 가장 최근 것을 삭제하는 메서드 (POP)
    # 내 답안
    # def pop(self):
    #     return self.pop()
    
    # 정답안
    def pop(self):
        if self.is_empty():
           return None
        return self.items.pop()

# 가장 최근 것을 확인하는 메서드 (PEEK)
    # 내 답안
    # def peek(self):
    #     return(self.items[-1])
    
    # 정답안
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]