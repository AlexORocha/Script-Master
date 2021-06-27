import sys

def main(argv):
    if argv[1] == 'master':
        from main.main import run as master
        master()
    if argv[1] == 'teste':
        print('TESTE')

if __name__ == '__main__':
    main(sys.argv)