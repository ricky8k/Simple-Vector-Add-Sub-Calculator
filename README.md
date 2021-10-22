# Simple-Vector-Add-Sub-Calculator
Simple Vector Add-Sub Calculator developed using Python.

This application allows you to add or subtract any given vectors.

The calculator can work offline if downloaded, no internet access is required.

## Installation
You will need:
- Python (works with 3.9.2)

Download `Simple.Vector.Add-Sub.Calculator.py` from the Releases tab. Run/open to start the script.

There are multiple variations of this program, the following are available:
- `Simple.Vector.Add-Sub.Calculator.py`

File should work with most online IDEs.

Works offline with Python 3.9.2 on Windows 10 19043.1237. Older versions of Python will most likely work. Other versions of Windows or Linux-based distros should also be able to run this file with no issue, though I have not personally tested it.

## Usage
You will need the polar forms of two given vectors.

Type in the measurement and angle for both vectors to get the answer.

### Example
Given a pair of vectors in polar form:
```
A = 3m @ 120
B = 2m @ 180
R = A + B
```
I want to find the sum of the two vectors.

The input to the calculator for vector `A` is as follows:
```
Enter vector A in Polar:
3
120
```
The input to the calculator for vector `B` is as follows:
```
Enter vector B in Polar:
2
180
```
Then, select the desired mode by typing `+` or `-`.
```
Select mode:
Type [+] for Addition
Type [-] for Subtraction
+
```
To get an output of:
```
Input:
A = 3.0 @ 120.0
B = 2.0 @ 180.0
R = A + B
```
which displays the input for the user to double-check.

Below you'll find the table, showing how the calculator got the answer in rectangular form:
```
Table:
-1.5 2.5981
-2.0 0.0
--------------------
-3.5 2.5981
```
You will also find the work area, which shows the step-by-step process on how the calculator got the answer in polar form:
```
Work:
R = sqrt(-3.5^2 + 2.5981^2)
R = sqrt(12.25 + 6.75)
R = sqrt(19.0)
R = 4.3589
Θ = tan-1(2.5981 / -3.5)
Θ = tan-1(-0.7423)
Θ = -36.5868
```
Finally, you'll find the solution, displayed in both rectangular and polar forms, respectively.
```
Solution:
--------------------
R = -3.5i + 2.5981j
R = 4.3589 @ 143.4132
```

## 
*ricky8k*
- https://github.com/ricky8k
