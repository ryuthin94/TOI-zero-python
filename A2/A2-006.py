def count_valid_starting_positions(grid, n):
  dp = [[False for _ in range(n)] for _ in range(n)]

  dp[n-1][n-1] = True

  for i in range(n-1, -1, -1):
      for j in range(n-1, -1, -1):
          if i == n-1 and j == n-1:
              continue

          if grid[i][j] == 'X':
              dp[i][j] = False
              continue

          can_reach_target = False

          if j < n-1:
              can_reach_target |= dp[i][j+1]

          if i < n-1:
              can_reach_target |= dp[i+1][j]

          dp[i][j] = can_reach_target

  count = 0
  for i in range(n):
      for j in range(n):
          if grid[i][j] == '.' and dp[i][j]:
              count += 1

  return count

def main():
  n = int(input())
  grid = []
  for _ in range(n):
      row = input()
      grid.append(row)

  result = count_valid_starting_positions(grid, n)
  print(result)

if __name__ == "__main__":
  main()