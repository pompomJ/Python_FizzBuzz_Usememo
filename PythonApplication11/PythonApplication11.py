# memoを用いてフィボナッチ数列を求める。とても高速。

def fastFib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except keyError:
        result = fastFib(n - 1, memo) + fastFib(n -2, memo)

        memo[n] = result
        return result

fastFib(50)

