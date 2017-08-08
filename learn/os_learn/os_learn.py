#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '08/08'
from multiprocessing import Process
import os

def run_prco(name):
    print('Run child process %s (%s)' % (name, os.getpid()))

if __name__ == '__main__':
    print('Process (%s) start...' % os.getpid())
    p = Process(target=run_prco, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')

