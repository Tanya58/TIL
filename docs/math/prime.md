# 소수 판별법
소수(prime number)는 1과 자기 자신만 약수로 가지는 1보다 큰 자연수이다.

```c
#include <math.h>

// 시간 복잡도 : O(N)
int is_prime1(int n)
{
    for (int i = 2; i < n; i++) if (n % i == 0) return 0;
    return 1;
}
// 시간 복잡도 : O(√N)
int is_prime2(int n)
{
    for (int i = 2; i<= sqrt(n); i++) if (n % i == 0) return 0;
    return 1;
}
```
# 에라토스테네스의 체
빠른 시간 내에 소수를 판별하기 위한 알고리즘이다. (시간 복잡도 `O(N log long N)`)

1. **2부터 N까지의 모든 자연수를 나열한다.**
2. **남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.**
3. **남은 수 중에서 i의 배수를 모두 제거한다. (i는 제거하지 않는다.)**
4. **더 이상 반복할 수 없을 때 까지 2~3번의 과정을 반복한다.**


```python
# 2부터 n 사이의 소수 목록
def eratosthenes(n):
    primes = [True for i in range(n+1)]  # 1 : 0 ~ n
    for i in range(2, int(n**0.5) + 1):
        if primes[i] == True:
            for j in range(i+i, n+1, i):
                primes[j] = False
    return [i for i in range(2, n+1) if primes[i] == True]

arr = eratosthenes(50) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print(True if 26 in arr else False) # False
```

```python
# a부터 b 사이의 소수 목록
def eratosthenes(a, b):
    primes = [True for i in range(b+1)]
    for i in range(2, int(b**0.5)+1):
        if primes[i] == True:
            for j in range(i+i, b+1, i):
                primes[j] = False
    return [i for i in range(a, b+1) if i != 1 and primes[i] == True]
```

