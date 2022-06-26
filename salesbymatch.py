"""
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example


There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

"""
def sockMerchant(n, ar):
 
    pairs = 0
    #get the maximum value from the list
    maxVal = max(ar)

    #create list with 0 for counting each
    counter=[]
    for e in range(maxVal + 1):
        counter.append(0)

    #get the current val from ar and sum it to counter with his respective position
    for ind in ar:
        counter[ind] += 1

    #sum the pairs for each
    for c in counter:
        pairs += c // 2

    #return total of pairs 
    return pairs
