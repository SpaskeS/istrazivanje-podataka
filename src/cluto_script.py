import os
import sys

def main():
    if len(sys.argv) != 2:
        print('python3 cluto_script.py genes/cells')
        exit(1)

    for i in range(2, 31):
        os.system('../../cluto-2.1.2/Linux-x86_64/vcluster ../data/{}.mat {} > ../outputs/CLUTO/{}_{}.txt'.format(sys.argv[1], i, sys.argv[1], i))

if __name__ == '__main__':
    main()
