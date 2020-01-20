from cmd import Cmd
import sys
import random


class MainPrompt(Cmd):
    prompt = 'itt> '
 
    def do_exit(self, inp):
        print("Bye")
        exit(0)
    
    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')
 
    def do_process(self, inp):
        print("processing the user input from stdin (accepts multiline input)... hit Ctrl+D to end")
        return True
 
    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        if inp =='p':
            return self.do_process(inp)
 
        print("Unrecognized Command: {}".format(inp))
 
    do_EOF = do_exit
    help_EOF = help_exit



def gen_rnd_word(lb, ub):
    if ub < lb:
        print("wrong lower bound and upper bound!")
        return ''
    length = random.randint(lb, ub)
    # 'a' is 97, 'z' is 122
    ascii_list = [ random.randint(97, 122) for i in range(0, length)]
    return ''.join(chr(i) for i in ascii_list)


def wrap_gift(wd):
    return '\\makebox[0pt][l]{\\transparent{0.0}'+wd+'}'


def process(line):
    if line[0] == '%':
        print(line)
        return
    
    line = line.rstrip()
    tokens = line.split(' ')
    final_tokens = []
    for token in tokens:
        if len(token) <= 3:
            final_tokens.append(token)
            continue
        #TODO: add more identifier exceptions
        if '\\' in token or '{' in token or '}' in token or '$' in token or '_' in token or ',' in token:
            final_tokens.append(token)
            continue 

        pos = random.randint(1, len(token)-1)
        #TODO: later let user set the rnd range
        new_token = token[0:pos] + wrap_gift(gen_rnd_word(3, 5)) + token[pos:]
        final_tokens.append(new_token)

    print(' '.join(final_tokens))



def main():
    print("Welcome! Type ? to list commands")

    while True:
        MainPrompt().cmdloop()
        lines = sys.stdin.readlines()
        print("####################")
        print("#  protected       #")
        print("####################")
        for line in lines:
            process(line)

  
if __name__== "__main__":
    main()

