class Solution:
    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.total = n_rows * n_cols
        self.used = set()

    def flip(self) -> List[int]:
        while True:
            r = random.randint(0, self.total - 1)
            if r not in self.used:
                self.used.add(r)
                return [r // self.n_cols, r % self.n_cols]

    def reset(self) -> None:
        self.used = set()
