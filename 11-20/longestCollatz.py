def iseven(n):
    return n % 2 == 0

def collatz(n):
    if iseven(n):
        return n // 2
    else:
        return 3 * n + 1

def collatz_sequence(n, memo):
    if n not in memo:
        seq = [n]
        while n != 1:
            n = collatz(n)
            seq.append(n)
            if n in memo:
                seq.extend(memo[n])
                break
        memo[seq[0]] = seq
    return memo[seq[0]]

def longest_collatz_sequence(n):
    longest = 0
    memo = {}
    for i in range(1, n):
        seq = collatz_sequence(i, memo)
        if len(seq) > len(memo.get(longest, [])):
            longest = i
    return longest

print(longest_collatz_sequence(1000000))
