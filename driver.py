#!/usr/bin/python3

def c2f(c):
  fah = (c * 9 / 5) + 32
  return fah

def main():
  # input
  cel = 0
  # process
  fah = c2f(cel)  
  # output
  print(f'Temp (C,F): \n{cel} C \n{fah:.2f} F')
  return fah

if __name__ == "__main__":
  main()
