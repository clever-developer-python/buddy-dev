#general commands (buddy)
import speedtest
import os
import sys
import pyjokes
import psutil

def opencalc():
    os.system('open /System/Applications/Calculator.app')

def quit():
    print('quttted buddy')
    sys.exit()

def restart():
    print('restarting....')
    os.system('python3 main.py')

def restartc():
    os.system('clear')
    os.system('python3 main.py')

def joke():
    get_joke = pyjokes.get_joke(language='en',category='all')
    print(get_joke)


def itest():
    print('started internet speed test....')
    st = speedtest.Speedtest()
        # Download Speed
    ds = st.download()
    du  = st.upload()
    def humansize(nbytes):
            suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
            i = 0
            while nbytes >= 1024 and i < len(suffixes)-1:
                nbytes /= 1024.
                i += 1
            f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
            return '%s %s' % (f, suffixes[i])
        #Readable
    print('download speed: ' + humansize(ds))
    print('upload speed: '+ humansize(du))


def cpu():
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage = (load15/os.cpu_count()) * 100
    print(f'Cpu usage: {cpu_usage}%')


def cpu_stats():
    print(psutil.cpu_stats())


def open_main_file(data):
    print('Opening file... Please be advised to not tamper with the file...')
    print("this will only work if the Functions folder and main.py are in the SAME DIRECTORY.")
    os.system(f'open {data}.py')
