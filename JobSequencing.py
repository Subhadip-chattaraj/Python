class Solution:
    def JobScheduling(self, Jobs, n):
        Jobs.sort(key=lambda j: j.profit, reverse=True)
        maxi = 1
        for i in Jobs:
            if i.deadline > maxi:
                maxi = i.deadline

        arr = []
        for i in range(0, maxi+1):
            arr.append(-1)

        maxJob = 0
        maxProfit = 0

        for i in Jobs:
            for j in range(i.deadline,0,-1):
                if arr[j] == -1:
                    arr[j] = 1
                    maxJob += 1
                    maxProfit += i.profit
                    break

        return maxJob, maxProfit


class Job:
    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':

    n = int(input())
    info = list(map(int, input().strip().split()))
    Jobs = [Job() for i in range(n)]
    for i in range(n):
        Jobs[i].id = info[3 * i]
        Jobs[i].deadline = info[3 * i + 1]
        Jobs[i].profit = info[3 * i + 2]
    ob = Solution()
    res = ob.JobScheduling(Jobs, n)
    print(res[0], res[1], end=" ")
