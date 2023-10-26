import os
import time

def initialize_repository():
    if not os.path.isdir('.git'):
        print("Initializing a new Git repository...")
        os.system('git init')
        os.system('git add .')
        os.system('git commit -m "Initial commit"')

def set_repository_url():
    if not os.popen('git remote get-url origin').read():
        repository_url = input("Please provide the repository URL: ")
        os.system(f'git remote add origin {repository_url}')

def commit_and_push():
    os.system('git add .')
    os.system('git commit -m "Automatic commit"')
    os.system('git branch -M main')
    os.system('git push origin main')

    if os.system('git push origin main') != 0:
        os.system('git push origin main --force')

initialize_repository()
set_repository_url()

while True:
    commit_and_push()
    time.sleep(1800) 
