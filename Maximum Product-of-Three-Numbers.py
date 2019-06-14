class Solution:
    def maximumProduct(self, arr: List[int]) -> int:
        high = max(arr[0], arr[1])
        low = min(arr[0], arr[1])

        high_prod_2 = arr[0] * arr[1]

        low_prod_2 = arr[0] * arr[1]

        high_prod_3 = arr[0] * arr[1] * arr[2]

        for i in range(2, len(arr)):

            cur = arr[i]

            high_prod_3 = max(high_prod_3, cur*high_prod_2, cur*low_prod_2)

            high_prod_2 = max(high_prod_2, cur * high, cur * low)

            low_prod_2 = min(low_prod_2, cur*high, cur*low)

            high = max(high, cur)

            low = min(low, cur)

        return high_prod_3