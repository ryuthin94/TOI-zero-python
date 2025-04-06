def solve_rabbit_buu(text):
  text_lower = text.lower()

  if "buu" in text_lower:
      max_u_count = 0

      for i in range(len(text_lower)):
          if text_lower[i] == 'b':
              u_count = 0
              j = i + 1
              while j < len(text_lower) and text_lower[j] == 'u':
                  u_count += 1
                  j += 1

              max_u_count = max(max_u_count, u_count)

      return f"Yes {max_u_count}"

  elif 'b' in text_lower:
      result = ""
      found_b = False

      for char in text:
          if not found_b and char.lower() == 'b':
              result += char
              found_b = True
          elif found_b:
              result += 'U'
          else:
              result += char

      return result

  else:

      pattern = "BUU"
      repetitions = len(text) // len(pattern)
      remainder = len(text) % len(pattern)

      return pattern * repetitions + pattern[:remainder]

user_input = input().strip()
print(solve_rabbit_buu(user_input))