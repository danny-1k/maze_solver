import os
import cv2
import numpy as np

from astar import astarsolver


class Maze:
    def __init__(self, image_path):
        self.image_path = image_path
        self.maze = cv2.imread(self.image_path)
        self.solved = self.maze.copy()

    def save_solved(self):
        img_dir = '../imgs/solved/'
        f = self.image_path.replace('\\', '/').split('/')[-1]

        if f in os.listdir(img_dir):
            os.remove(os.path.join(img_dir,f))

        cv2.imwrite(os.path.join(img_dir,f), self.solved)

    def to_2d(self, img):
        img = img.tolist()
        for i in range(len(img)):
            for j in range(len(img[0])):
                if sum(img[i][j]) <600:
                    img[i][j] = 0

                else:
                    img[i][j] = 1

        return np.array(img)

    def to_3d(self, img):
        img = img.tolist()
        for i in range(len(img)):
            for j in range(len(img[0])):
                if img[i][j] == 0:
                    img[i][j] = [0, 0, 0]

                else:
                    img[i][j] = [255, 255, 255]

        return np.array(img)

    def solve(self, highlight='g'):

        if highlight in 'rgb':

            highlight = [0, 0, 255] if highlight == 'r' else\
                        [0, 255, 0] if highlight == 'g' else \
                        [255, 0, 0] # cv2 is in brg

        else:
            highlight = [0, 255, 0]

        points = astarsolver(self.to_2d(self.maze))

        for p in points:
            y,x = p
            self.solved[y][x] = highlight


    def reset_solved(self):
        self.solved = self.maze.copy()
