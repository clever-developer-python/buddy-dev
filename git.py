import os

def init():
    os.system('git init')
    return "Finished process exit code 0"

def commit():
    msg = input('commit message enter without saying anything for auto commit msg: ')
    if msg == "":
        os.system('git commit -m "changes" ')
        return "Finished process exit code 0"

    else:
        os.system(f'git commit -m "{msg}" ')
        return "Finished process exit code 0"


def autocreate():
    prompt = input('git url (HTTP): ')
    os.system('git init')
    os.system('git add -A')
    os.system('git commit -m "started new project" ')
    os.system('git branch -M main')
    os.system(f'git remote add origin {prompt}')
    os.system('git push -u origin main')
    return print("Finished process exit code 0")


def clone(url):
    os.system(f'git clone {url}')

def add():
    multi = input('do you want to add specific files [y/n/] (n for adding all the files "git add -A" basically) > ')
    if multi == 'y':
        ask = input('what files do you want to add keep spacing between file names> ')
        os.system(f'git add {ask}')
        print(f'added {ask} to local repo')
                    
    else:
        os.system('git add -A')
        print('added all files')

def status():
    os.system('git status')  


def remove_git(git_input):
    os.system(f"git rm -r {git_input} -f")


def branch():
    os.system('git branch')

def branch_a():
    os.system('git branch -a')

def create_branch(name):
    os.system(f'git branch {name}')

def delete_branch(name):
    os.system(f'git branch -d {name}')



def r_git_token(token_git):
    file = open("token.txt","w")
    file.write(token_git)
    file.close()

def read_token():
    file = open("token.txt","r")
    print(file.readlines())
    file.close()
