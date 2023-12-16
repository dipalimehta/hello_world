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






# from datetime import datetime, timedelta
# from random import randint
# import os

# for i in range(100, 365):
#     for j in range(0, randint(1, 10)):
#         days_ago = timedelta(days=i)
#         date_string = (datetime.now() - days_ago).strftime('%Y-%m-%d')

#         with open('file.txt', 'a') as file:
#             file.write(date_string + '\n')

#         os.system('git add .')
#         os.system('git commit --date="' + date_string + '" -m "commit"')

# os.system('git push -u origin main')


# import os
# from random import randint
# from datetime import datetime, timedelta

# for i in range(1, 365):
#     for j in range(0, randint(1, 10)):
#         days_ago = timedelta(days=i)
#         commit_date = (datetime.now() - days_ago).strftime('%Y-%m-%d %H:%M:%S')
        
#         with open('file.txt', 'a') as file:
#             file.write(str(i) + ' days ago\n')
        
#         os.system('git add .')
#         os.system(f'git commit --date="{commit_date}" -m "commit"')

# os.system('git push -u origin main')


#!/usr/bin/env python
# import argparse
# import os
# from datetime import datetime
# from datetime import timedelta
# from random import randint
# from subprocess import Popen
# import sys


# def main(def_args=sys.argv[1:]):
#     args = arguments(def_args)
#     curr_date = datetime.now()
#     directory = 'repository-' + curr_date.strftime('%Y-%m-%d-%H-%M-%S')
#     repository = args.repository
#     user_name = args.user_name
#     user_email = args.user_email
#     if repository is not None:
#         start = repository.rfind('/') + 1
#         end = repository.rfind('.')
#         directory = repository[start:end]
#     no_weekends = args.no_weekends
#     frequency = args.frequency
#     days_before = args.days_before
#     if days_before < 0:
#         sys.exit('days_before must not be negative')
#     days_after = args.days_after
#     if days_after < 0:
#         sys.exit('days_after must not be negative')
#     os.mkdir(directory)
#     os.chdir(directory)
#     run(['git', 'init', '-b', 'main'])

#     if user_name is not None:
#         run(['git', 'config', 'user.name', user_name])

#     if user_email is not None:
#         run(['git', 'config', 'user.email', user_email])

#     start_date = curr_date.replace(hour=20, minute=0) - timedelta(days_before)
#     for day in (start_date + timedelta(n) for n
#                 in range(days_before + days_after)):
#         if (not no_weekends or day.weekday() < 5) \
#                 and randint(0, 100) < frequency:
#             for commit_time in (day + timedelta(minutes=m)
#                                 for m in range(contributions_per_day(args))):
#                 contribute(commit_time)

#     if repository is not None:
#         run(['git', 'remote', 'add', 'origin', repository])
#         run(['git', 'branch', '-M', 'main'])
#         run(['git', 'push', '-u', 'origin', 'main'])

#     print('\nRepository generation ' +
#           '\x1b[6;30;42mcompleted successfully\x1b[0m!')


# def contribute(date):
#     with open(os.path.join(os.getcwd(), 'README.md'), 'a') as file:
#         file.write(message(date) + '\n\n')
#     run(['git', 'add', '.'])
#     run(['git', 'commit', '-m', '"%s"' % message(date),
#          '--date', date.strftime('"%Y-%m-%d %H:%M:%S"')])


# def run(commands):
#     Popen(commands).wait()


# def message(date):
#     return date.strftime('Contribution: %Y-%m-%d %H:%M')


# def contributions_per_day(args):
#     max_c = args.max_commits
#     if max_c > 20:
#         max_c = 20
#     if max_c < 1:
#         max_c = 1
#     return randint(1, max_c)


# def arguments(argsval):
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-nw', '--no_weekends',
#                         required=False, action='store_true', default=False,
#                         help="""do not commit on weekends""")
#     parser.add_argument('-mc', '--max_commits', type=int, default=10,
#                         required=False, help="""Defines the maximum amount of
#                         commits a day the script can make. Accepts a number
#                         from 1 to 20. If N is specified the script commits
#                         from 1 to N times a day. The exact number of commits
#                         is defined randomly for each day. The default value
#                         is 10.""")
#     parser.add_argument('-fr', '--frequency', type=int, default=80,
#                         required=False, help="""Percentage of days when the
#                         script performs commits. If N is specified, the script
#                         will commit N%% of days in a year. The default value
#                         is 80.""")
#     parser.add_argument('-r', '--repository', type=str, required=False,
#                         help="""A link on an empty non-initialized remote git
#                         repository. If specified, the script pushes the changes
#                         to the repository. The link is accepted in SSH or HTTPS
#                         format. For example: git@github.com:user/repo.git or
#                         https://github.com/user/repo.git""")
#     parser.add_argument('-un', '--user_name', type=str, required=False,
#                         help="""Overrides user.name git config.
#                         If not specified, the global config is used.""")
#     parser.add_argument('-ue', '--user_email', type=str, required=False,
#                         help="""Overrides user.email git config.
#                         If not specified, the global config is used.""")
#     parser.add_argument('-db', '--days_before', type=int, default=365,
#                         required=False, help="""Specifies the number of days
#                         before the current date when the script will start
#                         adding commits. For example: if it is set to 30 the
#                         first commit date will be the current date minus 30
#                         days.""")
#     parser.add_argument('-da', '--days_after', type=int, default=0,
#                         required=False, help="""Specifies the number of days
#                         after the current date until which the script will be
#                         adding commits. For example: if it is set to 30 the
#                         last commit will be on a future date which is the
#                         current date plus 30 days.""")
#     return parser.parse_args(argsval)


# if __name__ == "__main__":
#     main()