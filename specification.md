```
1 => 2
```
The number 1 becomes the number 2.

This is just shorthand for `n => {n == 1} [2] [n]`.

---

```
n => n + 1
```
All numbers are increased by 1.

---

```
n => {n < 10} [n * 2] [n * 3]
```
If a number is less than 10, it is multiplied by 2. If not, it is multiplied by 3.

---

```
2 + 3 => 2 + 3 + 5
```
The number 5 becomes the number 10. Note that `2 + 3` is intuitively not treated as a variable (even though it is not numeric), so this function is not equivalent to `n => n + 5`.