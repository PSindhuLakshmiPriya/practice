def dfs(board,start,end,die_inputs):
    stack=[(start,0,0,0)]
    visited=set()
    while stack:
        position,snakes,ladders,moves=stack.pop()
        if position==end:
            return f"Possible {snakes} {ladders}"
        if position not in visited:
            visited.add(position)
            for die in die_inputs:
                new_position=position+die
                if new_position <= end:
                    if board[new_position]=='S':
                        stack.append((int(board[new_position+1]),snakes+1,ladders,moves+1))
                    elif board[new_position]=='L':
                        stack.append((int(board[new_position+1]),snakes,ladders+1,moves+1))
                    else:
                        stack.append((new_position,snakes,ladders,moves+1))
    return f"Not possible {snakes} {ladders}"                   
board=[input().split() for _ in range(10)]
board=[square if square!='S(Start)' else 'Start' for row in board for square in row]
start=board.index('Start')
end=board.index('End')
die_inputs=list(map(int,input().split()))
result=dfs(board,start,end,die_inputs)
print(result)