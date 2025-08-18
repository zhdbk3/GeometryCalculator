# Documentation

## Unknown

The name of an unknown can be

- a lowercase English letter (excluding `x` and `y`)
- the English name of a Greek letter (excluding `pi`)

## Point

Point names must be uppercase English letters. Subscripts and superscripts are not supported.  
~~(If you ever need more than 26 points... well, good luck.)~~

## Expressions

Our expression parser is built on Python’s `eval` ~~(which means you can totally inject arbitrary code and attack the backend)~~, with some custom extensions on top.

### Operations

|   Symbol    |    Meaning     |
| :---------: | :------------: |
|     `+`     |    Addition    |
|     `-`     |  Subtraction   |
|     `*`     | Multiplication |
|     `/`     |    Division    |
|    `dot`    |  Dot product   |
| `^` or `**` | Exponentiation |

Note: The multiplication symbol `*` is required and cannot be omitted.

### Constants and Functions

|  Code  |   Meaning   |
| :----: | :---------: |
|  `pi`  |    $\pi$    |
| `sqrt` | Square root |
| `sin`  |    Sine     |
| `cos`  |   Cosine    |
| `tan`  |   Tangent   |

**Note:** Functions must be called with parentheses.

- ❌ Incorrect: `sin pi`
- ✅ Correct: `sin(pi)`

---

### Accessing Unknowns

Simply type the name you assigned when creating them.

For example: `a`, `alpha`

---

### Accessing Point Coordinates

Format: `x` or `y` followed by the point name

For example: `xA` represents $x_A$

---

### Segment Length

Just type the segment name directly.

For example: `AB` represents the length of segment $AB$

---

### Angles

Format: `ang` + three points that define the angle

For example: `angABC` represents $\angle ABC$

#### Degrees

Use `deg` to represent degrees ($^\circ$)

For example: `30 deg` means $30^\circ$

### Vectors

#### Vectors Represented by Directed Segments

Format: `vec` + starting point + ending point

For example: `vecAB` represents $\overrightarrow{AB}$

#### Vectors in Coordinate Form

Format: (x-component, y-component)

For example: `(114, 514)` represents the vector $(114, 514)$

### Area of Triangle

Format: `St` + the triangle’s three vertices

For example: `StABC` represents the area $S_{\triangle ABC}$

### Slope ($k$) and Intercept ($b$) of a Line

Format: `k` or `b` followed by the line name

For example: `kAB` represents the slope $k_{AB}$ of line $AB`

Note: You must ensure the line is not vertical.
