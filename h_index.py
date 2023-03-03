def hIndex(citations):
    citations.sort(reverse = True) #sorting in descending order
    i = 0 #initializing i
    for i,citation in enumerate(citations): #i is index and citations is the value at that index
        print("I:",i)
        if i >= citation: #if constraint breaks
            return i #answer
	#if the compiler gets out of the loop then the constraint didn't break
	#hence return length
    return i+1 #i+1 gives length because i reached till the end

def odd_even(nums):
    mid = len(nums)//2
    nums[0::2], nums[1::2] = nums[:mid], nums[mid:]

    return nums

print(hIndex([1,3,1]))
print(odd_even([1,3,2,2,3,1]))