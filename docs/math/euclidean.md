# 유클리드 호제법 

## 유클리드 호제법
```css
두 양의 정수 a, b (a > b)에 대해서 a를 b로 나눈 나머지를 r이라 하면, 
a와 b의 최대 공약수는 b와 r의 최대 공약수와 같다.

이 성질에 따라, b를 r로 나눈 나머지 r¹을 구하고, r을 r¹으로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수 rⁿ이 a와 b의 최대 공약수이다. 

a  = b  * q  + r 
b  = r  * q¹ + r¹
r  = r¹ * q² + r²
r¹ = r² * q³ + r³
...
```
```c
78696과 19932의 최대 공약수는? 12

78696   = 19932 * 3 + 18900
19932   = 18900 * 1 + 1032
18900   = 1032 * 18 + 324
1032    = 324 * 3 + 60
324     = 60 * 5 + 24
60      = 24 * 2 + 12
24      = 12 * 2 + 0

// 최대 공약수 : Greatest Common Divisor
int gcd(int a, int b) { 
    return b? gcb(b, a%b) : a;
}
```

<br>

### 최소 공배수의 성질 
```css
A와 B의 최대공약수 G에 대해서 최소 공배수 L = A * B / G 를 만족한다.
```
```c
14 = 2 * 7
 6 = 2 * 3

14 와 6의 최대 공약수는?  2
14 = 6 * 2 + 2
 6 = 2 * 3 + 0

14와 6의 최소 공배수는? 48
= (2 * 7) * (2 * 3) / 2
= 2 * 3 * 7 = 48 
```

<br>

### 베주의 항등식
```css
Ax + By = C에서 C가 gcd(A, B)의 배수이면, x, y는 항상 정수해를 갖는다.
```
```c
Ax + By = gcd(A, B)에서 A가 102, B가 46일 경우 최대 공약수는? 2

102 = 46 * 2 + 10
46  = 10 * 4 + 6
10  = 6 * 1 + 4
6   = 4 * 1 + 2
4   = 2 * 2 + 0  

102x + 46y = 2가 성립된다.
51x + 23 y = 1의 정수 해는 x = -9, y = 20 이다.

// 최대 공약수 : Greatest Common Divisor
int gcd(int a, int b) { 
    return b? gcb(b, a%b) : a;
}

// 최소 공배수 : Least Common Multiple
int lcm(int a, int b) {
    return a * (b / gcd(a,b));
}
```

<br>

## 선형 디오판토스 방정식(Linear Diophantine Equation)
- 선형 디오판토스 방정식 : ax + by = c



> 양의 정수 a, b, c가 주어질 때 선형 디오판토스 방적식을 만족하는 정수 x, y를 구하라.

<br>

### 확장 유클리드 호제법 (Extended Euclidean Algorithm)
> c가 gcd(a,b)의 배수인 경우만 가능하다. a와 b가 서로소인 경우, a는 모듈러 연산의 곱의 역원이 된다.
```css
# 초기 조건 
r  = a, x  = 1, y  = 0
r₁ = b, x₁ = 0, y₁ = 1

# 공식 
q₃ = r₂ / r₃
r₃ = r₁ - r₂ * q₃   /* r₁ % r₂ */
x₃ = x₁ - x₂ * q₃   
y₃ = y₁ - y₂ * q₃   
```

| a   | b   | x₁  | y₁  |     | q   | x₂  | y₂  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 252 | 198 | 1   | 0   |     | 1   | 0   | 1   | 고정  |
| 198 | 54  | 0   | 1   |     | 3   | 1   | -1  |     |
| 54  | 36  | 1   | -1  |     | 1   | -3  | 4   |     |
| 36  | 18  | -3  | 4   |     | 2   | 4   | -5  |     |
| 18  | 0   |     |     |     |     |     |     |     |

```css
18 = 252 * 4 + 198 * (-5)

최소 공약수 : 18
x의 해 :  4
y의 해 : -5
```

<br>


소스 
```c
int egcd(int a, int b, int x1, int y1, int *x2, int *y2)
{
    if (a % b == 0)
        return a;
    int q = a / b;

    int x = x1 - (*x2 * q);
    x1 = *x2;
    *x2 = x;

    int y = y1 - (*y2 * q);
    y1 = *y2;
    *y2 = y;

    return egcd(b, a % b, x1, y1, x2, y2);
}

int main(){
    int a = 0, b = 0;
    scanf("%d %d", &a, &b);

    int x = 0;
    int y = 1;
    c = egcd(a, b, 1, 0, &x, &y);
    printf("%d %d %d", x, y, g);
    return 0;
}
```
