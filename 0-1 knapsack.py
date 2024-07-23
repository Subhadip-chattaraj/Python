class Solution:
    def knapsack(self, w, wait, vl, ni):
        ans = []
        for i in range(0, ni + 1):
            l = []

            for j in range(0, w + 1):
                if i == 0 or j == 0:
                    l.append(0)
                elif wait[i - 1] <= j:
                    l.append(max(vl[i - 1] + ans[i - 1][j - wait[i - 1]], ans[i - 1][j]))
                else:
                    l.append(ans[i - 1][j])

            ans.append(l)

        return ans[ni][w]


if __name__ == '__main__':
    test_cases = int(input("Enter Number of Test Cases:"))
    for cases in range(test_cases):
        n = int(input("Enter Number of items:"))
        W = int(input("Enter wait of the items:"))
        print("Enter Value of the items:", end='')
        val = list(map(int, input().strip().split()))
        print("Enter Wait of the items:", end='')
        wt = list(map(int, input().strip().split()))
        Ob = Solution()
        print("Max value of Knapsack is:", Ob.knapsack(W, wt, val, n))
