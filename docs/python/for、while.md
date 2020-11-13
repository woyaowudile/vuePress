# 循环

## 一.for
```python
for i in range(5,10):
    print(i) // 5,6,7,8,9

for i in range(5,10, 2):
    print(i) // 5,7,9
```
## 二.while
```python
while true:
    print(1)
```

## 三.区别
```text
知道循环次数用for，
满足某个条件后结束用while
```

## 四.逻辑运算符
```python
list = [1,2,3,4]
a = 10
print(1 and 0)        # 0
print(1 or 0)         # 1
print(not False)      # True
print(a in list)      # false
print(a not in list)  # true
# in 和 not in 既可用于[]，也可用于{}
```

## 五.条件为假
```python
print(not False)      # True
print(not 0)          # True
print(not '')         # True
print(not [])         # True
print(not {})         # True
print(not none)       # True
```


## 六.跳出循环
```text
break   :  跳出当前循环
continue ： 跳出此次循环，进入下一循环
pass： 不需要在循环体里使用
else： 和if else用法一样,在for循环或while循环中
    for i in range(100):
        xxx
    else:
```