from slender import List, Set

def main():
    a = List([1, 2, 3, 4, 5]) \
        .delete_if(lambda x: x % 2 == 0) \
        .map(lambda x: x * 2) \
        .chain(['a', 'b']) \
        .each_with_index() \
        .to_list() 
        
    print(a) # => [[0, 2], [1, 6], [2, 10], [3, 'a'], [4, 'b]]









