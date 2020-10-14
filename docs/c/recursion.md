
# 재귀(Recursion)
- 직관적이며 가독성이 뛰어나다. 
- 함수가 호출된 만큼 콜 스택에 쌓여 `O(n)`의 공간을 차지한다.
- <u>**호출 위치를 기억해야하므로 호출 횟수가 많아질수록 실행 속도가 느려지거나  <br />
  스택이 최대 램 사이즈를 넘게 되어 오버플로우가 발생하므로 주의가 필요하다.**</u>
```c
int factorial(int n) {
  if (n == 1) return 1;
  return n * factorial(n - 1); // 마지막 연산 = 곱셈
}
/* ex. CALL STACK 예시 
factorial(3)
3 * factorial(2)
3 * 2 * factorial(1)
3 * 2 * 1
3 * 2
6
*/
```

<br />

# 꼬리 재귀(Tail Recursion)
- 가장 마지막에 함수를 호출하여 `TCO(Tail Call Optimization)`를 사용한다. 
- 이전 스텍프래임을 무시하거나 재사용하여 재귀의 문제점을 해결할 수 있다. 

```c
// factorial(1,n);
int factorial(int acc, int n) {
  if (n == 1) return acc;
  return factorial(n * acc, n - 1); // 마지막 연산 = 함수 호출 
}
/* ex. CALL STACK 예시 
factorial(1,3)
factorial(3,2)
factorial(6,1)
6
*/
```
<br />

# TCO(Tail Call Optimization)
함수에서 가장 마지막으로 실행하는 것이 다른 함수의 호출이라면 해당 스택은 더 이상 필요하지 않으므로 <u>**마지막 함수 호출 전 스택을 비워 공간을 절약하는 기법**</u>이다. 
  - **TCO 제공** : C, Ruby, Javascript
  - **TCO 미제공** : Python, Java 등 대부분의 언어
 
<br />

컴파일러에서 1) 함수 호출로 끝난 재귀 함수를 인식하고 2) 반복문으로 최적화한다. <br />
**<span style = "color : red">
※ 컴파일 시, -O3 옵션이 적용되어 있지 않으면 최적화가 되지 않는다. 
</span>**

<br />

# 반복(Iteration)
```c
int factorial(int n) {
  int acc = 1;
  for (; n > 1 ; --n) acc *= n;
  return acc;
}
```
```c
int factorial(int n) {
  int acc = 1;
TOP:
  if (n == 1) return acc;
  acc = n * acc;
  n = n -1;
  goto TOP;
}
```

<br />

# 참고
- [테일 콜 최적화 란 무엇입니까?](https://qastack.kr/programming/310974/what-is-tail-call-optimization)