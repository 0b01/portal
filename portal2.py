#!/usr/bin/python
#
# Portal Interpreter
# Copyright 2014 Ricky Han
# Usage: ./portal.py [FILE]

import sys
import getch

def execute(filename):
  f = open(filename, "r")
  evaluate(f.read())
  f.close()


def evaluate(code):
  code     = cleanup(list(code))
  bracemap = buildbracemap(code)
  bracemap2 = buildbracemap2(code)
  
  cells, codeptr, cellptr = [0], 0, 0
  passed = False
  passed2 = False
  while codeptr < len(code):
    first, second = sorted(bracemap.values())
    first2, second2 = sorted(bracemap2.values())
    command = code[codeptr]

    if command == ">":
      cellptr += 1
      if cellptr == len(cells): cells.append(0)

    if command == "<":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "+": cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0
    if command == "-": cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

    if command == "o" and     passed and (-1 not in bracemap): codeptr = bracemap[codeptr]
    if command == "o" and not passed: passed = True
    if command == "]":
      code[first], code[first+1] = code[first+1], code[first]
      bracemap = buildbracemap(code)
    if command == "[":
      code[second], code[second-1] = code[second-1], code[second]
      bracemap = buildbracemap(code)

    if command == "O" and     passed2 and (-1 not in bracemap2): codeptr = bracemap2[codeptr]
    if command == "O" and not passed2: passed2 = True
    if command == "}":
      code[first2], code[first2+1] = code[first2+1], code[first2]
      bracemap2 = buildbracemap2(code)
    if command == "{":
      code[second2], code[second2-1] = code[second2-1], code[second2]
      bracemap2 = buildbracemap2(code)

    if command == ".": sys.stdout.write(chr(cells[cellptr]))
    if command == ",": cells[cellptr] = ord(getch.getch())
      
    if (-1 in bracemap): code = list(''.join(code).replace('oo','o'))
    if (-1 in bracemap2): code = list(''.join(code).replace('OO','O'))

    codeptr += 1
    # print ''.join(code)

def cleanup(code):
  return filter(lambda x: x in ['.', ',', '[', ']', '<', '>', 'o', '{', '}', 'O', '+', '-'], code)


def buildbracemap(code):
  temp_bracestack, bracemap = [], {}
  passed = False
  if 'oo' in ''.join(code) or 'OO' in ''.join(code):
    return {-1:-1, -2:-2}
  for position, command in enumerate(code):
    if command == "o" and passed:
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
    if command == "o" and not passed:
      temp_bracestack.append(position)
      passed = True
  return bracemap

def buildbracemap2(code):
  temp_bracestack, bracemap = [], {}
  passed = False
  if 'OO' in ''.join(code):
    return {-1:-1, -2:-2}
  for position, command in enumerate(code):
    if command == "O" and passed:
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
    if command == "O" and not passed:
      temp_bracestack.append(position)
      passed = True
  return bracemap

def main():
  if len(sys.argv) == 2: execute(sys.argv[1])
  else: print "Usage:", sys.argv[0], "filename"

if __name__ == "__main__": main()

