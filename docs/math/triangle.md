# 삼각형

### 삼각형의 성립 조건

```css
# 가장 긴 변의 길이만 고려할 경우
 - a, b, c 중에 가장 큰 값 c
 - c < a + b

# 모든 변의 길이를 고려할 경우
 - a < b + c
 - b < a + c
 - c < a + b

/* 위 조건이 동일한 이유 */
                  c < a + b
a < c < c + b  => a < b + c
b < c < c + a  => b < b + c
```

성립 조건 관련 예제

```c
// 가장 긴 변의 길이만 고려할 경우
#include <stdio.h>
int main()
{
    int len[3] = {0};
    scanf("%d %d %d", &len[0], &len[1], &len[2]);

    int flag = 0;
    for (int i = 0; i < 3; i++)
    {
        if (len[i] >= len[(i + 1) % 3] && len[i] >= len[(i + 2) % 3]) {
            if (len[i] < len[(i + 1) % 3] + len[(i + 2) % 3]) {
                flag = 1;
                break;
            }
        }
    }
    printf("%s", flag ? "yes" : "no");
    return 0;
}

// 모든 변의 길이를 고려한 경우
#include <stdio.h>
int main()
{
    int a = 0, b = 0, c = 0;
    scanf("%d %d %d", &a, &b, &c);
    printf("%s", a < b + c && b < a + c && c < a + b ? "yes" : "no");
    return 0;
}
```
