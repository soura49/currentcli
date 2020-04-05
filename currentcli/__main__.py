import argparse
import sys
import datetime
import time


class Command():
    def __init__(self):
        const ='''cli [OPTIONS] COMMAND
Commands:
    time      To get the curent time 
    date      To get the Current date
    day       To get the Current Day
'''
        parser = argparse.ArgumentParser(description="Automated Cli to get the Currnet date and time",usage=const)
        parser.add_argument('command',help='subcommand to show')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self,args.command):
            print("unrecongized command")
            parser.print_help()
            exit(1)
        getattr(self,args.command)()

    def time(self):
        parser = argparse.ArgumentParser(description='Gives the current Time')
        print(str(datetime.datetime.now()).split(' ')[1])

    def date(self):
        parser = argparse.ArgumentParser(description='Gives the Currnet Date')
        print(str(datetime.datetime.now()).split(' ')[0])

    def day(self):
        print(time.strftime("%A"))


def main():
    Command()

if __name__ == '__main__':
    main()
