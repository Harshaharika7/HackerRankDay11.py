# Read the 6x6 array
arr = [list(map(int, input().strip().split())) for _ in range(6)]

# Initialize maximum to the lowest possible hourglass sum
max_sum = -63  # Since min value is -9 and an hourglass has 7 values: 7 * -9 = -63

# Loop through possible hourglass centers (i,j)
for i in range(4):
    for j in range(4):
        # Calculate hourglass sum
        hourglass = (
            arr[i][j] + arr[i][j+1] + arr[i][j+2]
            + arr[i+1][j+1]
            + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        )
        # Update max_sum
        max_sum = max(max_sum, hourglass)

# Output the maximum hourglass sum
print(max_sum)
