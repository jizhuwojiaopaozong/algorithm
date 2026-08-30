class Solution:
    # 二分法
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l < r:
            mid = (l + r + 1) // 2
            if mid * mid <= x:
                l = mid
            else:
                r = mid - 1
        return l

    # 牛顿迭代法
    def mySqrt2(self, x: int) -> int:
        if not x:
            return 0

        r = x
        while r * r > x:
            r = (r + x // r) // 2

        return r

    # 浮点数二分
    def mySqrt3(self, x: float, k: int) -> float:
        if not x:
            return 0.0
        l = 0.0
        r = max(1.0, x)
        eps = 10 ** (-k - 2)
        while r - l > eps:
            mid = (l + r) / 2.0
            if mid * mid <= x:
                l = mid
            else:
                r = mid
        return r


solution = Solution()
# print(solution.mySqrt(4))
# print(solution.mySqrt(8))
# print(solution.mySqrt(16))
# print(solution.mySqrt(25))
# print(solution.mySqrt(36))
# print(solution.mySqrt(49))
# print(solution.mySqrt(64))
# print(solution.mySqrt(81))
# print(solution.mySqrt(100))

print(f"{solution.mySqrt3(4, 2):.2f}")
print(f"{solution.mySqrt3(8, 4):.4f}")
print(f"{solution.mySqrt3(8, 5):.5f}")
print(f"{solution.mySqrt3(0.25, 3):.3f}")