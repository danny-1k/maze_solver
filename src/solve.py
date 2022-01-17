import argparse
from maze import Maze

parser = argparse.ArgumentParser()
parser.add_argument('--maze_path',help="Maze path",required=True)
parser.add_argument('--solve_color', help="color to solve the maze in; 'r' or 'g' or 'b'")

args = parser.parse_args()

maze_path = args.maze_path
solve_color = str(args.solve_color)

maze = Maze(maze_path)
maze.solve(highlight=solve_color)
maze.save_solved()
print('Look in the "solved" folder')