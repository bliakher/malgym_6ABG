# 11. hodina - 20. 5. 2022

## Grafy - knihovna `matplotlib`

Jednoduchá ukázka použití knihovny
```python
import matplotlib.pyplot as plt

# vytvoření grafu
fig, ax = plt.subplots()

# nastevení popisků
ax.set_title("můj graf")
ax.set_xlabel("osa x")
ax.set_ylabel("osa y")

# data pro graf
x = [1, 2, 3, 4]
y = [3, 1, 2, 4]

# ax.plot(x, y) # lomenná čára
# ax.scatter(x, y) # jednotlivé body
# ax.bar(x, y) # sloupcový graf
ax.stem(x, y)

# zobrazení grafu
plt.show() 
```

```python

```
