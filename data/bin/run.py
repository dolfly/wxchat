#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import ctypes
import sys
sdk = ctypes.cdll.LoadLibrary("")
def help():
    print("\nUsage: \n启动: python run.py start port [debug]\n关闭: python run.py stop\nport: 命令端口, 消息端口为命令端口+1\n")
    sys.exit(0)
    
def main():
    debug = False
    argc = len(sys.argv)
    argv = sys.argv
    print(argc,argv)
    if argc < 3 or argc > 5 :
        help()
    elif argc == 4 :
        debug = argv[3] == "debug" 
    if argv[1] == "start":
        print("starting")
        port = int(argv[2])
        print(port)
        ret = sdk.WxInitSDK(debug,port)
    elif argv[1] == "stop":
        print("stopping")
        ret = sdk.WxDestroySDK(debug,port)
    else:
        help()
if __name__ == "__main__":
    main()