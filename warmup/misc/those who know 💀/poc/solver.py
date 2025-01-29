import base64

def solve(hex_input):
  return base64.b64encode(bytearray([x ^ 0x6 for x in bytearray.fromhex(hex_input)]))

if __name__ == '__main__':
  hex = input()
  print(solve(hex))