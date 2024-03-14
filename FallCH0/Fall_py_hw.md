P12 4; P14 2;P17 4;P19 2;P26 3;P27 1;P28 2; P29 3;
P35 2;['2020', '20.20', 'Python', 2020, [2020, '2020'], 2024];
P36 2;P37 4;P39 1;P48 Hello;P49 2;P50 553;
P51 aaabbbc;P52 1,3,5,7,9,;

##### P53

```python
s=input()
s=s[-1::-1]
print(s)
print(len(s))
```

##### P54

```python
x0, y0, x1, y1 = map(float, input().split())
distance = ((x0-x1)**2+(y0-y1)**2)**0.5
print(distance)
```

##### P55

```python
s=input()
if len(s)<20:
    print(s.rjust(20,' '))
else:
    print(s[:20])
```

