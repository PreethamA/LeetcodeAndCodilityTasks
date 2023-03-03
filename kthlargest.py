def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    def partition(l, r, pivot_index):
        pivot = nums[pivot_index]
        # move pivot to the end
        nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
        store_index = l
        for i in range(l, r):
            if nums[i] > pivot:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1
        # move pivot to its final place
        nums[store_index], nums[r] = nums[r], nums[store_index]
        return store_index

    def quickselect(l, r, k_smallest):
        if l == r:
            return nums[l]
        pivot_index = r
        pivot_index = partition(l, r, pivot_index)
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(l, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, r, k_smallest)

    return quickselect(0, len(nums) - 1, k-1)

print(findKthLargest([3, 2, 1, 5, 6, 4],2))