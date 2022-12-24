from functions.git import *
from functions.general import *
import os
#do not tamper with this file. Only do if you know what you are doing.

try:
    def engine():
        prompt = input('> ')

        #git engine
        if prompt == 'init':
            init()
            engine()

        elif prompt == 'commit':
            commit()
            engine()

        elif prompt == 'autocreate':
            autocreate()
            engine()

        elif prompt == 'clone':
            url = input('Url for cloning git repo (HTTP/SSH): ')
            clone(url)
            engine()

        elif prompt == 'r_git_token':
            token = input('github repo token: ')
            r_git_token(token)
            engine()

        elif prompt == 'g_token':
            read_token()
            engine()

        elif prompt == 'add':
            add()
            engine()

        elif prompt == 'status':
            status()
            engine()

        elif prompt == 'grm':
            prompt_2 = input('file name: ')
            remove_git(prompt_2)
            engine()

        elif prompt == 'branch':
            branch()
            engine()

        elif prompt == 'new branch':
            create_branch()
        
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        #general commands
        elif prompt == 'calc':
            opencalc()
            engine()

        elif prompt == 'quit()':
            quit()

        elif prompt == 'restart':
            restart()

        elif prompt == 'restart-c':
            restartc()

        elif prompt == 'joke':
            joke()
            engine()

        elif prompt == 'gen-joke':
            joke()
            engine()

        elif prompt == "itest":
            itest()
            engine()

        elif prompt == 'cpu':
            cpu()
            engine()

        elif prompt == 'cpu-stats':
            cpu_stats()
            engine()

        elif prompt == 'main.file.buddy.engine.open':
            name  = __file__.rsplit("/", 1)[1].split('.')[0]
            open_main_file(name)
            engine()


        else:
            os.system(prompt)
            engine()



    engine()

except:
    pass

#end of main command list code
