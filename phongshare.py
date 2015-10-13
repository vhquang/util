#!/usr/local/bin/python

import requests, os.path, subprocess

def write_tofile(filename, data):
    with open(filename, 'w') as f_out:
        f_out.write(data)
    
if __name__ == '__main__':
    page = requests.get('http://www.monamcali.com/quangcao/Phongchothue.htm')
    if os.path.isfile('new.html'):
        os.rename('new.html', 'old.html')
        write_tofile('new.html', page.text.encode('utf8'))
        command = ['diff', 'old.html', 'new.html']
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = proc.communicate()
        if proc.returncode != 0:
            print output
    else:
        write_tofile('new.html', page.text.encode('utf8'))
