# #import math
#
# # Creating a shortcut for int, int pair type
# Pair = tuple[int, int]
#
# # A structure to hold the necessary parameters
# class Cell:
#     def __init__(self, parent_i: int, parent_j: int, f: float, g: float, h: float):
#         self.parent_i = parent_i
#         self.parent_j = parent_j
#         self.f = f
#         self.g = g
#         self.h = h
#
#
# # A Utility Function to check whether given cell (row, col) is a valid cell or not.
# def is_valid(row: int, col: int, ROW: int, COL: int) -> bool:
#     return 0 <= row < ROW and 0 <= col < COL
#
#
# # A Utility Function to check whether the given cell is blocked or not
# def is_unblocked(grid: list[list[int]], row: int, col: int) -> bool:
#     return grid[row][col] == 1
#
#
# # A Utility Function to check whether destination cell has been reached or not
# def is_destination(row: int, col: int, dest: Pair) -> bool:
#     return row == dest[0] and col == dest[1]
#
#
# # A Utility Function to calculate the 'h' heuristics.
# def calculate_h_value(row: int, col: int, dest: Pair) -> float:
#     # Return using the distance formula
#     return math.sqrt((row - dest[0]) ** 2 + (col - dest[1]) ** 2)
#
#
# # A Utility Function to trace the path from the source to destination
# def trace_path(cell_details: list[list[Cell]], dest: Pair) -> None:
#     print("\nThe Path is ", end="")
#     row, col = dest
#
#     path = []
#     while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
#         path.append((row, col))
#         temp_row, temp_col = cell_details[row][col].parent_i, cell_details[row][col].parent_j
#         row, col = temp_row, temp_col
#
#     path.append((row, col))
#     while path:
#         p = path.pop()
#         print(f"-> {p}", end=" ")
#
#
# # A Function to find the shortest path between a given source cell to a destination cell
# # according to A* Search Algorithm
# def a_star_search(grid: list[list[int]], src: Pair, dest: Pair) -> None:
#     ROW, COL = len(grid), len(grid[0])
#
#     # If the source is out of range
#     if not is_valid(src[0], src[1], ROW, COL):
#         print("Source is invalid")
#         return
#
#     # If the destination is out of range
#     if not is_valid(dest[0], dest[1], ROW, COL):
#         print("Destination is invalid")
#         return
#
#     # Either the source or the destination is blocked
#     if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
#         print("Source or the destination is blocked")
#         return
#
#     # If the destination cell is the same as the source cell
#     if is_destination(src[0], src[1], dest):
#         print("We are already at the destination")
#         return
#
#     # Create a closed list and initialise it to False which means that no cell has been included yet
#     closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
#
#     # Declare a 2D array of structure to hold the details of that cell
#     cell_details = [[Cell(-1, -1, float('inf'), float('inf'), float('inf')) for _ in range(COL)] for _ in range(ROW)]
#
#     # Initialising the parameters of the starting node
#     i, j = src
#     cell_details[i][j] = Cell(i, j, 0.0, 0.0, 0.0)
#
#     # Create an open list having information as- <f, <i, j>> where f = g + h,
#     # and i, j are the row and column index of that cell
#     open_list = [(0.0, (i, j))]
#
#     # We set this boolean value as False as initially the destination is not reached.
#     found_dest = False
#
#     while open_list:
#         # Remove this vertex from the open list
#         p = min(open_list)
#         open_list.remove(p)
#
#         # Add this vertex to the closed list
#         i, j = p[1]
#         closed_list[i][j] = True
#
#         successors = [
#             (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1),
#             (i - 1, j + 1), (i - 1, j - 1), (i + 1, j + 1), (i + 1, j - 1)
#         ]
#
#         for successor in successors:
#             successor_i, successor_j = successor
#
#             # Only process this cell if this is a valid one
#             if is_valid(successor_i, successor_j, ROW, COL):
#                 # If the destination cell is the same as the current successor
#                 if is_destination(successor_i, successor_j, dest):
#                     # Set the Parent of the destination cell
#                     cell_details[successor_i][successor_j].parent_i = i
#                     cell_details[successor_i][successor_j].parent_j = j
#                     print("The destination cell is found")
#                     trace_path(cell_details, dest)
#                     found_dest = True
#                     return
#
#                 # If the successor is already on the closed list or if it is blocked, then ignore it.
#                 # Else do the following
#                 elif not closed_list[successor_i][successor_j] and is_unblocked(grid, successor_i, successor_j):
#                     g_new = cell_details[i][j].g + 1.0
#                     h_new = calculate_h_value(successor_i, successor_j, dest)
#                     f_new = g_new + h_new
#
#                     # If it isn’t on the open list, add it to the open list.
#                     # Make the current square the parent of this square.
#                     # Record the f, g, and h costs of the square cell.
#                     if cell_details[successor_i][successor_j].f == float('inf') or cell_details[successor_i][
#                         successor_j].f > f_new:
#                         open_list.append((f_new, (successor_i, successor_j)))
#
#                         # Update the details of this cell
#                         cell_details[successor_i][successor_j] = Cell(i, j, f_new, g_new, h_new)
#
#     # When the destination cell is not found and the open list is empty,
#     # then we conclude that we failed to reach the destination cell.
#     # This may happen when there is no way to the destination cell (due to blockages)
#     if not found_dest:
#         print("Failed to find the Destination Cell")
#
#
# # Driver program to test above function
# if __name__ == "__main__":
#
#
# # Source and Destination Points
# # a_star_search(grid, src, dest)
# #import math
#
# # Creating a shortcut for int, int pair type
# Pair = tuple[int, int]
#
# # A structure to hold the necessary parameters
# class Cell:
#     def __init__(self, parent_i: int, parent_j: int, f: float, g: float, h: float):
#         self.parent_i = parent_i
#         self.parent_j = parent_j
#         self.f = f
#         self.g = g
#         self.h = h
#
#
# # A Utility Function to check whether given cell (row, col) is a valid cell or not.
# def is_valid(row: int, col: int, ROW: int, COL: int) -> bool:
#     return 0 <= row < ROW and 0 <= col < COL
#
#
# # A Utility Function to check whether the given cell is blocked or not
# def is_unblocked(grid: list[list[int]], row: int, col: int) -> bool:
#     return grid[row][col] == 1
#
#
# # A Utility Function to check whether destination cell has been reached or not
# def is_destination(row: int, col: int, dest: Pair) -> bool:
#     return row == dest[0] and col == dest[1]
#
#
# # A Utility Function to calculate the 'h' heuristics.
# def calculate_h_value(row: int, col: int, dest: Pair) -> float:
#     # Return using the distance formula
#     return math.sqrt((row - dest[0]) ** 2 + (col - dest[1]) ** 2)
#
#
# # A Utility Function to trace the path from the source to destination
# def trace_path(cell_details: list[list[Cell]], dest: Pair) -> None:
#     print("\nThe Path is ", end="")
#     row, col = dest
#
#     path = []
#     while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
#         path.append((row, col))
#         temp_row, temp_col = cell_details[row][col].parent_i, cell_details[row][col].parent_j
#         row, col = temp_row, temp_col
#
#     path.append((row, col))
#     while path:
#         p = path.pop()
#         print(f"-> {p}", end=" ")
#
#
# # A Function to find the shortest path between a given source cell to a destination cell
# # according to A* Search Algorithm
# def a_star_search(grid: list[list[int]], src: Pair, dest: Pair) -> None:
#     ROW, COL = len(grid), len(grid[0])
#
#     # If the source is out of range
#     if not is_valid(src[0], src[1], ROW, COL):
#         print("Source is invalid")
#         return
#
#     # If the destination is out of range
#     if not is_valid(dest[0], dest[1], ROW, COL):
#         print("Destination is invalid")
#         return
#
#     # Either the source or the destination is blocked
#     if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
#         print("Source or the destination is blocked")
#         return
#
#     # If the destination cell is the same as the source cell
#     if is_destination(src[0], src[1], dest):
#         print("We are already at the destination")
#         return
#
#     # Create a closed list and initialise it to False which means that no cell has been included yet
#     closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
#
#     # Declare a 2D array of structure to hold the details of that cell
#     cell_details = [[Cell(-1, -1, float('inf'), float('inf'), float('inf')) for _ in range(COL)] for _ in range(ROW)]
#
#     # Initialising the parameters of the starting node
#     i, j = src
#     cell_details[i][j] = Cell(i, j, 0.0, 0.0, 0.0)
#
#     # Create an open list having information as- <f, <i, j>> where f = g + h,
#     # and i, j are the row and column index of that cell
#     open_list = [(0.0, (i, j))]
#
#     # We set this boolean value as False as initially the destination is not reached.
#     found_dest = False
#
#     while open_list:
#         # Remove this vertex from the open list
#         p = min(open_list)
#         open_list.remove(p)
#
#         # Add this vertex to the closed list
#         i, j = p[1]
#         closed_list[i][j] = True
#
#         successors = [
#             (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1),
#             (i - 1, j + 1), (i - 1, j - 1), (i + 1, j + 1), (i + 1, j - 1)
#         ]
#
#         for successor in successors:
#             successor_i, successor_j = successor
#
#             # Only process this cell if this is a valid one
#             if is_valid(successor_i, successor_j, ROW, COL):
#                 # If the destination cell is the same as the current successor
#                 if is_destination(successor_i, successor_j, dest):
#                     # Set the Parent of the destination cell
#                     cell_details[successor_i][successor_j].parent_i = i
#                     cell_details[successor_i][successor_j].parent_j = j
#                     print("The destination cell is found")
#                     trace_path(cell_details, dest)
#                     found_dest = True
#                     return
#
#                 # If the successor is already on the closed list or if it is blocked, then ignore it.
#                 # Else do the following
#                 elif not closed_list[successor_i][successor_j] and is_unblocked(grid, successor_i, successor_j):
#                     g_new = cell_details[i][j].g + 1.0
#                     h_new = calculate_h_value(successor_i, successor_j, dest)
#                     f_new = g_new + h_new
#
#                     # If it isn’t on the open list, add it to the open list.
#                     # Make the current square the parent of this square.
#                     # Record the f, g, and h costs of the square cell.
#                     if cell_details[successor_i][successor_j].f == float('inf') or cell_details[successor_i][
#                         successor_j].f > f_new:
#                         open_list.append((f_new, (successor_i, successor_j)))
#
#                         # Update the details of this cell
#                         cell_details[successor_i][successor_j] = Cell(i, j, f_new, g_new, h_new)
#
#     # When the destination cell is not found and the open list is empty,
#     # then we conclude that we failed to reach the destination cell.
#     # This may happen when there is no way to the destination cell (due to blockages)
#     if not found_dest:
#         print("Failed to find the Destination Cell")
#
#
# # Driver program to test above function
# if __name__ == "__main__":
#
#
# # Source and Destination Points
# # a_star_search(grid, src, dest)
a = [{'latitude': 9.9261153, 'longitude': 78.1140983}, {'latitude': 13.0836939, 'longitude': 80.270186}, {'latitude': 44.9391565, 'longitude': -123.033121}, {'latitude': 11.4126769, 'longitude': 76.7030504}, {'latitude': 9.9261153, 'longitude': 78.1140983}]

print(a[0])