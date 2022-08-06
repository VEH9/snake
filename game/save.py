import shelve
from pathlib import Path


def delete_save(have_save, save_level):
    have_save.save(False)
    save_level.delete()


path = Path('all_saves')
if not path.is_dir():
    path.mkdir()


class Save:
    def __init__(self):
        file = path / "data"
        self.file = shelve.open(str(file))

    def save(self, level, score):
        self.file[f'{level}'] = score

    def get(self, name):
        try:
            return self.file[name]
        except Exception:
            return 0

    def add(self, name, value):
        self.file[name] = value

    def __del__(self):
        self.file.close()


class Save_Level:
    def __init__(self):
        file = path / "data_save"
        self.file = shelve.open(str(file))

    def save(self, blocks_count, bad_blocks, name, total, lives, snake_blocks, apple, speed,
             d_row, d_col, can_move):
        self.file['blocks_count'] = blocks_count
        self.file['bad_blocks'] = bad_blocks
        self.file['name'] = name
        self.file['total'] = total
        self.file['lives'] = lives
        self.file['snake_blocks'] = snake_blocks
        self.file['apple'] = apple
        self.file['speed'] = speed
        self.file['d_row'] = d_row
        self.file['can_move'] = can_move
        self.file['d_col'] = d_col

    def get(self, name):
        return self.file[name]

    def add(self, name, value):
        self.file[name] = value

    def delete(self):
        self.file.clear()

    def __del__(self):
        self.file.close()


class Have_save:
    def __init__(self):
        file = path / "have_save"
        self.file = shelve.open(str(file))

    def save(self, value):
        self.file['name'] = value

    def get(self):
        try:
            return self.file['name']
        except Exception:
            return False

    def add(self, name, value):
        self.file[name] = value

    def __del__(self):
        self.file.close()
