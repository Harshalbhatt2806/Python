{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4f2fbf7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Z-transform of x[n] = 3^n u[n]:\n",
      "⎧     1             1       \n",
      "⎪   ─────      for ─── < 1/3\n",
      "⎪       3          │z│      \n",
      "⎪   1 - ─                   \n",
      "⎪       z                   \n",
      "⎪                           \n",
      "⎪  ∞                        \n",
      "⎨ ___                       \n",
      "⎪ ╲                         \n",
      "⎪  ╲    n  -n               \n",
      "⎪  ╱   3 ⋅z      otherwise  \n",
      "⎪ ╱                         \n",
      "⎪ ‾‾‾                       \n",
      "⎪n = 0                      \n",
      "⎩                           \n"
     ]
    }
   ],
   "source": [
    "import sympy as sp\n",
    "# Define symbols\n",
    "n, z = sp.symbols('n z')\n",
    "# Define the sequence x[n] = 3^n * u[n]\n",
    "x_n = 3**n   # u[n] automatically handled by starting sum at n = 0\n",
    "# Compute the Z-transform\n",
    "X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))\n",
    "# Print the symbolic result\n",
    "print(\"Z-transform of x[n] = 3^n u[n]:\")\n",
    "sp.pprint(X_z, use_unicode=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "41b7bd60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Z-transform of x[n] = cos(w n) u[n]:\n",
      "  ∞               \n",
      " ___              \n",
      " ╲                \n",
      "  ╲    -n         \n",
      "  ╱   z  ⋅cos(n⋅w)\n",
      " ╱                \n",
      " ‾‾‾              \n",
      "n = 0             \n"
     ]
    }
   ],
   "source": [
    "import sympy as sp\n",
    "\n",
    "# Define symbols\n",
    "n, z, w = sp.symbols('n z w')\n",
    "\n",
    "# Define the sequence x[n] = cos(w*n) * u[n]\n",
    "x_n = sp.cos(w * n)\n",
    "\n",
    "# Compute Z-transform\n",
    "X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))\n",
    "\n",
    "# Print result\n",
    "print(\"Z-transform of x[n] = cos(w n) u[n]:\")\n",
    "sp.pprint(X_z, use_unicode=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
