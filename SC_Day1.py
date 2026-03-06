# 2.create your project demo and make demo file has operational functions (+
# ,-)
# 3.make commit for each functions seperatly
# 4.create a branch with name “branch2” and by it make ( / ,
# * ) functions
# 5.create another branch with your name and switch to it , then:
# make SayHello function
# 6.merge the branch which with your name to the main/master branch
# note: each change you add , make it with a different commit.
from py_compile import main


def add(a, b):
    return a + b

def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def say_hello(name):
    return f"Hello, {name}!"

#git status
#git add .
#git commit -m "add function"
#git log --oneline
#git status
#git add .
#git commit -m "sub function"
#git checkout -b branch2
#git add .
#git commit -m "add mul and div functions"
#git checkout master
#git merge branch2
#git checkout -b mohamed
#git add .
#git commit -m "add say_hello"
#git checkout master
#git merge mohamed
#git branch -d branch2

###############################################
#day2
#git branch -r
#git fetch 
#git switch -c aliaa_saudi origin/aliaa_saudi
#git pull origin aliaa_saudi
#git switch main
#git merge aliaa_saudi
#git pull origin main
######################################
#git branch -r
#git fetch 
#git switch -c Bodaa origin/Bodaa
#git pull origin Bodaa
#git switch main
#git merge Bodaa
#git pull origin main


# git fetch
# git switch -c aliaa_saudi origin/aliaa_saudi
# git switch main
# git pull origin main
# git merge aliaa_saudi
# git push origin main

