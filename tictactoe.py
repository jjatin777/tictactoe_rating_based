import copy

def calc_rating(turn,board)->int:
    r={}
    if turn == 'o': oturn ='x'
    if turn == 'x': oturn ='o'
    r[turn]=5
    r[oturn]=3
    r['e']=2
    val=[1,1,1,1,1,1,1,1]
    for i in range(3):
        val[0]=val[0]*r[board[i]]
        val[1]=val[1]*r[board[i+3]]
        val[2]=val[2]*r[board[i+6]]
        
        val[3]=val[3]*r[board[i*3]]
        val[4]=val[4]*r[board[i*3 +1]]
        val[5]=val[5]*r[board[i*3 +2]]
        
        val[6]=val[6]*r[board[i*4]]
        val[7]=val[7]*r[board[i*2+2]]
        
    # check if turn wins with this move
#     if r[turn]*r[turn]*r[turn] in val:
#         return 1000
  
#     # if other wins with this
#     if r[oturn]*r[oturn]*r[oturn] in val:
#         return -1000
    
#     #other win in next move
#     if r[oturn]*r[oturn]*2 in val:
#         return -800
        
#     # you win in next move provided other is not wining
#     if r[turn]*r[turn]*2 in val:
#         return 800
    
    # check if turn wins with this move
    if r[turn]*r[turn]*r[turn] in val:
        j=0
        for x in val:
            if r[turn]*r[turn]*r[turn] == x:
                j=j+1
        return j*1000
  
    # if other wins with this
    if r[oturn]*r[oturn]*r[oturn] in val:
        j=0
        for x in val:
            if r[oturn]*r[oturn]*r[oturn] == x:
                j=j+1
        return j*(-1000)
    
    #other win in next move
    if r[oturn]*r[oturn]*2 in val:
        j=0 
        for x in val:
            if r[oturn]*r[oturn]*2 == x:
                j=j+1
        return j*(-800)
        
    # you win in next move provided other is not wining
    if r[turn]*r[turn]*2 in val:
        j=0
        for x in val:
            if r[turn]*r[turn]*2 == x:
                j=j+1      
        return j*800
        
    return 0

def minimax(board,level,rating):
    
    if(level>2):
        return rating
    
    max_rating =-9999
    min_rating =9999
    pos=-1
    
    for i in range(9):
        
        if board[i]=='e':
            new_board=copy.deepcopy(board)
            
            if level%2==0:#even
                
                new_board[i]='o'
                il = calc_rating('o',new_board)
                r=minimax(new_board,level+1,rating-boardr[i]-il)
                
                if r < min_rating:
                    min_rating =r
                    pos=i
            else:
                new_board[i]='x'
                il = calc_rating('x',new_board)  
                r=minimax(new_board,level+1,rating+boardr[i]+il)
                if level%2==1 and r>max_rating:
                    pos=i
                    max_rating=r
    
    board[pos]='x'
    if level%2==0: rating = min_rating 
    else : rating = max_rating
    return rating

boardr =[30,20,30,20,50,20,30,20,30]
board =['e', 'e', 'e', 
 'e', 'e', 'e', 
 'e', 'e', 'e']
while(1):
    while(1):
        print('Enter your choice 1-9')
        s= int(input())
        if(board[s-1]=='e'):
            board[s-1]='o'
            
            if s==1:
                if board[1]=='e':boardr[1]=40
                else:boardr[3]=40
            if s==3:
                if board[1]=='e':boardr[1]=40
                else:boardr[5]=40
            if s==7:
                if board[7]=='e':boardr[7]=40
                else:boardr[3]=40
            if s==9:
                if board[5]=='e':boardr[5]=40
                else:boardr[7]=40            
            break
        else:
            print("Enter valid Choice")
     
    minimax(board,1,0)
    
    for i in range(3):
        for j in range(3):
            if board[i*3 + j]=='e':
                print('_',end=' ')
            else:
                print(board[i*3 + j],end=' ')
        print('\n')
        
    zee=calc_rating('x',board)
    if zee>=1000 and zee%1000==0:
        print('Comp wins')
        break
    
    zee=calc_rating('o',board)
    if zee>=1000 and zee%1000==0:
        print('YOu win')
        break
        
    if 'e' not in board:
        print('Its a draw')
        break