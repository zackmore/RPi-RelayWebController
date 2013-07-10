# -*- coding: UTF-8 -*-
from bottle import Bottle, route, run, template, request, static_file
import os
import commands

# 静态文件
@route('/js/<filename:path>')
def static_fileimg(filename):
    return static_file(filename, root='/home/zulius/Workspace/testlight/js')

@route('/')
def index_page():
    return open('index.html').read()

@route('/light', method='put')
def light_change():
    switchTo = int(request.params.get('switchTo'))
    if switchTo == 1:
        exec_str = 'echo Light On!'
    elif switchTo == 0:
        exec_str = 'echo Light Off!'
    (status, output) = commands.getstatusoutput(exec_str)
    return output


run(host='localhost', port=4321, debug=True)
