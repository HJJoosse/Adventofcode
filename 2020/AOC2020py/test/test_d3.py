import unittest
import AOC2020py.src.day3 as aoc

example_trees = \
    "..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#"
tc = aoc.TreeCounter(example_trees)
tc.split_inputs()


class TestDay3(unittest.TestCase):

    def outputs_is_right(self):
        self.assertEqual(tc.make_total_sum(), 336)

if __name__ == '__main__':
    unittest.main()