EMOJI_MAP = {
  'a': '😤', 'b': '😎', 'c': '😣', 'd': '😋', 'e': '🤓', 'f': '🤑',
  'g': '😷', 'h': '🤔', 'i': '😍', 'j': '🤣', 'k': '😘', 'l': '😔',
  'm': '😓', 'n': '😡', 'o': '🤕', 'p': '😌', 'q': '🤫', 'r': '😥',
  's': '🤧', 't': '🤒', 'u': '🙃', 'v': '🤮', 'w': '😨', 'x': '🧑‍🎄',
  'y': '😜', 'z': '😴',
  '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣',
  '5': '5️⃣', '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣',
  '_': '💩🐸', '{': '💩🌚', '}': '💩🌝'
}

def encode(text):
  result = []
  caps_active = False
  
  for char in text:
    if char.isupper():
      if not caps_active:
        result.append('🧢')
        caps_active = True
      result.append(EMOJI_MAP[char.lower()])
    else:
      if caps_active:
        result.append('🧢')
        caps_active = False
      result.append(EMOJI_MAP.get(char, char))
      
  if caps_active:  # Close any remaining caps
    result.append('🧢')
    
  return ''.join(result)

def decode(emoji_text):
  # Create reverse mapping
  reverse_map = {v: k for k, v in EMOJI_MAP.items()}
  
  # Split the text into chunks that we can process
  result = []
  i = 0
  current_caps = False
  
  while i < len(emoji_text):
    # Handle caps emoji
    if emoji_text[i:i+1] == '🧢':
      current_caps = not current_caps
      i += 1
      continue
    
    # Try matching number emojis first (they're longer)
    found_match = False
    for length in [3, 2, 1]:  # Try different emoji lengths
      chunk = emoji_text[i:i+length]
      if chunk in reverse_map:
        char = reverse_map[chunk]
        result.append(char.upper() if current_caps else char)
        i += length
        found_match = True
        break
    
    if not found_match:
      result.append(emoji_text[i])
      i += 1
      
  return ''.join(result)

# Test it
choice = input("Enter option (encode/decode): ")
test_text = input("Enter text: ")

if choice == "encode":
  encoded = encode(test_text)
  print("Original:", test_text)
  print("Encoded:", encoded)
elif choice == "decode":
  decoded = decode(test_text)
  print("Original:", test_text)
  print("Decoded:", decoded)
else:
  print("Invalid option")
