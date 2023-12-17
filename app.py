import os
from random import randint
from datetime import datetime, timedelta

repo_url = "https://github.com/dipalimehta/hello_world.git"
local_repo_path = r"D:\STUDY MATERIAL\1.Life_Changing_folder\hello_world"  # Replace with the desired local directory

def run_git_command(command):
    print(f"Executing: {command}")
    os.system(command)

# Clone the repository
run_git_command(f'git clone {repo_url} {local_repo_path}')

for i in range(1, 365):
    for j in range(0, randint(1, 10)):
        days_ago = timedelta(days=i)
        date_string = (datetime.now() - days_ago).strftime('%Y-%m-%d')

        with open(os.path.join(local_repo_path, 'file.txt'), 'a') as file:
            file.write(date_string + '\n')

        run_git_command(f'cd {local_repo_path} && git add .')
        run_git_command(f'cd {local_repo_path} && git commit --date="{date_string}" -m "commit"')

run_git_command(f'cd {local_repo_path} && git push -u origin main')



## Note: Click on left bottom "Visualize commits in commit graph" and push all the changes to reflect