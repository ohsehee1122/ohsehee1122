def rep_char(c,n):
    print(c*n)

def draw_line_string(prompt):
    word1=f'Hello {prompt},'
    word2=('Welcome to Seoul.')
    nstr = len(word1) if (len(word1) > len(word2)) else len(word2)
    rep_char('-',nstr+1)
    print(word1)
    print(word2)
    rep_char('-',nstr+1)

name=input('Input his/her name:')
draw_line_string(name)
