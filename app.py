# import os
# from random import randint

# for i in range(1,365):
#     for j in range(0,randint(1,10)):
#         d = str(i) + 'days ago'
#         with open('file.txt','a') as file:
#             file.write(d)
#         os.system('git add .')
#         os.system('git commit --date"' + d + '" -m "commit"')
# os.system('git push -u origin main')

import os
from random import randint
from datetime import datetime, timedelta

for i in range(1, 365):
    for j in range(0, randint(1, 10)):
        days_ago = timedelta(days=i)
        commit_date = (datetime.now() - days_ago).strftime('%Y-%m-%d %H:%M:%S')
        
        with open('file.txt', 'a') as file:
            file.write(str(i) + ' days ago\n')
        
        os.system('git add .')
        os.system(f'git commit --date="{commit_date}" -m "commit"')

os.system('git push -u origin main')
