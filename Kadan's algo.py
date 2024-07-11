def maxSubArraySum(self,arr):
    max_current = max_sum = arr[0]
    for i in range(1, len(arr)):
    # Update the current sum to be 
    # either the current element or
    # the current sum plus the current element
        max_current=max(arr[i], max_current+arr[i])
    # Update the  maximum sum if the
    # current sum is greater
        if max_current > max_sum:
            max_sum = max_current

    return max_sum

