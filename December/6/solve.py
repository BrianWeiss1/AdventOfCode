def simulate_guard_route(grid, obstruction_pos=None):
    # Create a deep copy of the grid to avoid modifying the original
    grid = [list(row) for row in grid]
    
    # If an obstruction is provided, place it
    if obstruction_pos:
        grid[obstruction_pos[0]][obstruction_pos[1]] = '#'
    
    # Find initial guard position
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '^':
                start_pos = [i, j]
                break
    
    # Directions: Up (0), Right (1), Down (2), Left (3)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_dir = 0  # Initially facing up
    
    # Track visited states to detect loops
    visited_states = set()
    
    while True:
        # Create a unique state representation
        current_state = (tuple(start_pos), current_dir)
        
        # If we've seen this exact state before, we've found a loop
        if current_state in visited_states:
            return True
        
        visited_states.add(current_state)
        
        # Check next position in current direction
        next_row = start_pos[0] + directions[current_dir][0]
        next_col = start_pos[1] + directions[current_dir][1]
        
        # Check if out of bounds
        if (next_row < 0 or next_row >= len(grid) or 
            next_col < 0 or next_col >= len(grid[0])):
            return False
        
        # If obstacle, turn right
        if grid[next_row][next_col] == '#':
            current_dir = (current_dir + 1) % 4
        else:
            # Move forward
            start_pos[0] = next_row
            start_pos[1] = next_col

def find_loop_points(grid):
    loop_positions = 0
    
    # Try placing an obstacle at each position
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # Skip starting position and existing obstacles
            start_pos = None
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '^':
                        start_pos = (i, j)
                        break
                if start_pos:
                    break
            
            if (r, c) == start_pos or grid[r][c] == '#':
                continue
            
            # Check if this obstruction causes a loop
            if simulate_guard_route(grid, (r, c)):
                loop_positions += 1
    
    return loop_positions

# Read the input
with open("December/6/data.txt", 'r') as f:
    grid = f.read().splitlines()

# Solve the problem
print(find_loop_points(grid))