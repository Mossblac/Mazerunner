import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_number_of_cells(self):
        num_cols = 10
        num_rows = 11
        maze1 = Maze(0, 0, num_rows, num_cols, 50, 50)
        self.assertEqual(
            len(maze1._cells), num_cols
        )
        self.assertNotEqual(
            len(maze1._cells), num_rows
        )


    def test_total_number_of_cells(self):
        num_rows = 10
        num_cols = 10
        maze0 = Maze(0, 0, num_rows, num_cols, 50, 50)
        self.assertEqual(
            len(maze0._cells * len(maze0._cells[0])), 100
        )

    def test_if_open(self):
        num_rows = 10
        num_cols = 10
        maze0 = Maze(0, 0, num_rows, num_cols, 50, 50)
        self.assertEqual(maze0._cells[0][0].has_left_wall, False)

    def test_if_exit(self):
        num_rows = 10
        num_cols = 10
        maze0 = Maze(0, 0, num_rows, num_cols, 50, 50)
        self.assertEqual(maze0._cells[-1][-1].has_right_wall, False)
        
if __name__ == "__main__":
    unittest.main()