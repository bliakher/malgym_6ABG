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
- **figure** - celá obrazovka s grafy
- **axes** - jeden graf
- **axis** - osa grafu - graf má 2 nebo 3 (u 3D grafu)

- vytvoření grafu

```python
fig, ax = plt.subplots() # obrazovka s jedním grafem
fig, axs = plt.subplots(2, 2) # obrazovka se 4 grafy v mřížce 2x2
# axs je dvourozměrné pole 2x2 s objekty grafů
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2) # rovnou rozložím pole na objekty
```
Příklad se 4 grafy
```python
import matplotlib.pyplot as plt

# vytvoření grafu
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

# data pro graf
x = [1, 2, 3, 4]
y = [3, 1, 2, 4]

ax1.plot(x, y) # lomenná čára
ax2.scatter(x, y) # jednotlivé body
ax3.bar(x, y) # sloupcový graf
ax4.stem(x, y)

# zobrazení grafu
plt.show() 

```
```python

```
```python

```

