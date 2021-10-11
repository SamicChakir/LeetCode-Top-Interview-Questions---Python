class Solution:
    def mySqrt(self, x: int) -> int:
        # new ton method  y2 -x = 0 f' = 2y  x_k+1 = x_k - f(x_k)/f'(x_k)

        x_k = 1
        while abs(self.f(x_k, x)) > 0.001:
            print(x_k)
            x_k = x_k - self.f(x_k, x) / self.f_prime(x_k)

        return x_k

    def f(self, x_k, x):
        return x_k * x_k - x

    def f_prime(self, x):
        return 2 * x


sol = Solution()

print(sol.mySqrt(4))