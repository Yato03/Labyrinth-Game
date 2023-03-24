from read_file import read_file

def test_read_file():
        print(read_file("levels/level1.txt"))

        assert read_file("levels/level1.txt") == [
                [(0, 2), (2, 0), (4, 2)],
                [(0, 1), (1, 4), (2, 2), (3, 1), (3, 4)],
                [(0,0),(4, 4)],
                5
        ]
        
if __name__ == "__main__":
    test_read_file()