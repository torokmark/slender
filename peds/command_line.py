from peds import List

def main():
    l = List([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(l)
    print(l[2])
    l[2] = 4
    print(l[2])
    print(l + ['a', 'b', 'c'])
    #dif = l.delete_if(lambda x: x % 3 == 0)
    #print(dif)









