#Portal

Portal is an esoteric language that loosely implements the [Wang B-Machine](http://en.wikipedia.org/wiki/Wang_B-machine). It is, you guessed it, named after the video game and namesake **Portal**.

## What is this Portal language?

| Portal      | Description                                                             |
|:---------:  | :-----------------------------------------------------------------------|
| **o**         | **Move the pointer to the other o portal**                                    |
| >           | Move the pointer to the right                                           |
| <           | Move the pointer to the left                                            |
| +           | Increment the memory cell under the pointer                             |
| -           | Decrement the memory cell under the pointer                             |
| .           | Output the character signified by the cell at the pointer               |
| ,           | Input a character and store it in the cell at the pointer               |
| **]**         | **Move the first o portal to the right**                                      |
| **[**         | **Move the last o portal to the left**                                        |

| Portal 2    | Description                                                             |
|:---------:  | :-----------------------------------------------------------------------|
| **o**         | **Move the pointer to the other o portal**                                    |
| **O**         | **Move the pointer to the other O portal**                                    |
| >           | Move the pointer to the right                                           |
| <           | Move the pointer to the left                                            |
| +           | Increment the memory cell under the pointer                             |
| -           | Decrement the memory cell under the pointer                             |
| .           | Output the character signified by the cell at the pointer               |
| ,           | Input a character and store it in the cell at the pointer               |
| **]**         | **Move the first o portal to the right**                                      |
| **[**         | **Move the last o portal to the left**                                        |
| **}**         | **Move the first O portal to the right**                                      |
| **{**         | **Move the last O portal to the left**                                        |

Important note: A pointer does not go in the a portal on the first pass. Check the examples.

## Example

###**Portal**: Prints an ampersand(&):
```
+++++++++++++o+++++]]]]]o++++++++++++++++++++. 
```

Code trace:
```
+++++++++++++o+++++]]]]]o++++++++++++++++++++.
# omitted
+++++++++++++o+++++]]]]]o++++++++++++++++++++.
++++++++++++++o++++]]]]]o++++++++++++++++++++.
+++++++++++++++o+++]]]]]o++++++++++++++++++++.
++++++++++++++++o++]]]]]o++++++++++++++++++++.
+++++++++++++++++o+]]]]]o++++++++++++++++++++.
++++++++++++++++++o]]]]]o++++++++++++++++++++.
++++++++++++++++++o]]]]]o++++++++++++++++++++.
++++++++++++++++++]o]]]]o++++++++++++++++++++.
++++++++++++++++++]]o]]]o++++++++++++++++++++.
++++++++++++++++++]]]o]]o++++++++++++++++++++.
++++++++++++++++++]]]]o]o++++++++++++++++++++.
++++++++++++++++++]]]]]o++++++++++++++++++++.
++++++++++++++++++]]]]]o++++++++++++++++++++.
++++++++++++++++++]]]]]o++++++++++++++++++++.
# omitted
++++++++++++++++++]]]]]o++++++++++++++++++++.
```

###**Portal 2**

The following code prints an **Ö** (O with diaeresis)[http://en.wikipedia.org/wiki/%C3%96]
```
O++++++o----}}o]]O.
```

Code trace:
```
O++++++o----}}o]]O.
O++++++o----}}o]]O.
O++++++o----}}o]]O.
O++++++o----}}o]]O.
O++++++o----}}o]]O.
O++++++o----}}o]]O.
O++++++o----}}o]]O.
O++++++o----}}o]]O.
O++++++o----}}o]]O.
O++++++o----}}o]]O.
O++++++o----}}o]]O.
O++++++o----}}o]]O.
+O+++++o----}}o]]O.
++O++++o----}}o]]O.
++O++++o----}}o]]O.
++O++++o----}}o]]O.
++O++++o----}}o]]O.
++O++++o----}}o]]O.
++O++++o----}}o]]O.
+++O+++o----}}o]]O.
++++O++o----}}o]]O.
++++O++o----}}o]]O.
++++O++o----}}o]]O.
++++O++o----}}o]]O.
++++O++o----}}o]]O.
++++O++o----}}o]]O.
+++++O+o----}}o]]O.
++++++Oo----}}o]]O.
++++++Oo----}}o]]O.
++++++Oo----}}o]]O.
++++++Oo----}}o]]O.
++++++Oo----}}o]]O.
++++++Oo----}}o]]O.
++++++oO----}}o]]O.
++++++o-O---}}o]]O.
++++++o-O---}}o]]O.
++++++o-O---}}o]]O.
++++++o-O---}}o]]O.
```
A little cönfused? eh?

## Run

```
$  ./portal.py [filename]
$  ./portal2.py [filename]
```

# Help wanted

If you can help figure out an idiosyncratic way to print the ubiquitous "Hello World", you will be the first one to program on a Wang B-Machine.


# Acknowledgement

The python interpreter is a fork of [pocmo/Python-Brainfuck](https://github.com/pocmo/Python-Brainfuck).
