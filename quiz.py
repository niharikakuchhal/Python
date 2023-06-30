from pyfiglet import Figlet
from colorama import Fore,Style
import time

def render_title(text):
    f = Figlet(font='slant',justify='width=40')
    print(Fore.WHITE + f.renderText(text.center(50, ' ')) + Style.RESET_ALL)

def render_menu():
    print("Menu".center(50, '-'))
    print(f"{Fore.WHITE}For the previous question, press 'p'")
    print(f"For the next question, press 'n'")
    print(f"For quitting, press 'q'")
    print(Style.RESET_ALL)

def intro():
    print('\n' * 100)
    render_title("Welcome to Python Quiz")
    print('\n')
    render_menu()
    input("Press any key to start the game ------>")
    print('\n' * 100)


def questions():
    ques = {1:'In Python 3, the maximum value for an integer is 263 - 1:',
            2:'How would you express the hexadecimal value a5 as a base-16 integer constant in Python?',
            3:'How would you express the constant floating-point value 3.2 × 10-12 in Python:',
            4:'Write an expression for a string literal consisting of the following ASCII characters:\nHorizontal Tab character\nNewline (ASCII Linefeed) character\nThe character with hexadecimal value 7E',
            5: 'print(r\'foo\\bar\nbaz\')',
            6:'Which of the following is not a Python built-in function:'}
    
    opt = {1:['True','False'],
           2:['0xa5', 'a5', 'A5', '0xA5'],
           3:['3.2e-12', '3.2 × 10^-12', '3.2e12', '3.2 x 10^-12'],
           4:[],
           5:[],
            6:['round()','diff()','repr()','isinstance()','map()']
           }
    ans ={1:'False',
          2:'0xa5',
          3:'3.2e-12',
          4:["\\t\\n\\x7E",],
          5:['foo\\bar\nbaz'],
          6:['diff()']
          }
    return ques,opt,ans

def pattern():
    res = input('Enter the Answer ---> ')
    print(Fore.GREEN+"          For previous question press 'p'\n\
          For Next question press 'n'\n\
          For quit press 'q'\n\
          ".ljust(50,' '))
    print(Style.RESET_ALL)
    k = input("Press any key ------>")

    animation = '|/-\\'
    for _ in range(10):
        for c in animation:
            print(f'\rLoading {c}',end = '')
            time.sleep(0.1)
        print('\n'*100)

    return k,res

    
    
def display():
    col = questions()
    ques_count = len(col[0])
    curr_que=1
    marks_list = []
    while curr_que <= ques_count:
        question = col[0][curr_que]
        option = col[1][curr_que]
        print(f"Question {curr_que}: {question}")
        print("Options:")
        for i, option in enumerate(option, start = 1):
            print(f'    {i}.{option}')
        k, ans = pattern()

        if ans == col[2][curr_que]:
            marks_list.append(1)

        if k == 'p':
            if curr_que >1:
                curr_que -=1
                print('\n'*100)
            continue
        elif k =='n':
            if curr_que < ques_count:
                curr_que +=1
                print('\n'*100)
            elif curr_que == ques_count:
                break
            continue
        elif k =='q':
            break

        curr_que +=1
        print('\n'*100)
        
    total_marks = sum(marks_list)
    print(f"Total marks obtained -----> {total_marks}")
    print(f'Accuarcy {total_marks/ques_count*100:.2f}%')

    



if __name__ == '__main__':
    print('\n'*100)
    intro()
    display()

