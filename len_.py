def len_list(x):
    count = 0
    for i in x:
        count += 1
    print count 

def len_liststring(x):
    count = 0
    for i in x:
        count += 1
    print count 

    ###############################################################################
def main():   # DO NOT CHANGE BELOW
    len_list(['a', 'b', 'c'])
    len_liststring('abcdefg')


if __name__ == '__main__':
    main()