# GENERATOR.PY
# Tạo bảng Sudoku
import random
# HÀM CHÍNH GỌI TỪ MAIN.PY
def generateboard(size, difficulty):
    """
    Hàm tổng:
    - size: "2x2" hoặc "3x3"
    - difficulty: "Easy", "Medium", "Hard"
    Trả về:
    - play_board: bảng để chơi (có ô trống = 0)
    - solution_board: bảng lời giải đầy đủ
    """
    if size == "2x2":
        empty = {"Easy": 8, "Medium": 10, "Hard": 12}[difficulty]
        return generate2x2(empty)
    elif size == "3x3":
        empty = {"Easy": 30, "Medium": 40, "Hard": 50}[difficulty]
        return generate3x3(empty)
# TẠO SUDOKU 2x2 (4x4)
def generate2x2(empty):
    """
    Tạo Sudoku 4x4
    """
    # base board hợp lệ
    base = [
        [1, 2, 3, 4],
        [3, 4, 1, 2],
        [2, 3, 4, 1],
        [4, 1, 2, 3]
    ]
    # tạo lời giải từ base
    solution_board = copyboard(base)
    # xáo trộn để nhìn ngẫu nhiên
    shuffle_numbers(solution_board)
    shuffle_rows(solution_board)
    shuffle_cols(solution_board)
    # tạo bảng chơi từ lời giải
    play_board = copyboard(solution_board)
    # xóa bớt ô
    remove_cells(play_board, empty)
    return play_board, solution_board
# TẠO SUDOKU 3x3 (9x9)
def generate3x3(empty):
    """
    Tạo Sudoku 9x9
    """
    base = [
        [1,2,3,4,5,6,7,8,9],
        [4,5,6,7,8,9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [2,3,4,5,6,7,8,9,1],
        [5,6,7,8,9,1,2,3,4],
        [8,9,1,2,3,4,5,6,7],
        [3,4,5,6,7,8,9,1,2],
        [6,7,8,9,1,2,3,4,5],
        [9,1,2,3,4,5,6,7,8]
    ]
    solution_board = copyboard(base)
    shuffle_numbers(solution_board)
    shuffle_rows(solution_board)
    shuffle_cols(solution_board)
    play_board = copyboard(solution_board)
    remove_cells(play_board, empty)
    return play_board, solution_board
# COPY BOARD
def copyboard(board):
    """
    Copy bảng 2 chiều
    row[:] giúp tạo bản sao, không dính reference
    """
    return [row[:] for row in board]
# XÁO TRỘN SỐ (1-9)
def shuffle_numbers(board):
    """
    Đổi tên các số:
    ví dụ 1->7, 2->3, 3->9,...
    vẫn giữ luật Sudoku
    """
    size = len(board)
    nums = list(range(1, size + 1))
    random.shuffle(nums)
    # mapping số cũ -> số mới
    mapping = {}
    for index in range(len(nums)):
        old_number = index + 1
        new_number = nums[index]
        mapping[old_number] = new_number
    # thay toàn bộ bảng theo mapping
    for r in range(size):
        for c in range(size):
            board[r][c] = mapping[board[r][c]]
# XÁO TRỘN HÀNG
def shuffle_rows(board):
    """
    Chỉ xáo trộn các hàng
    TRONG cùng 1 block
    """
    size = len(board)
    block = int(size ** 0.5)
    for b in range(0, size, block):
        rows = board[b : b + block]
        random.shuffle(rows)
        board[b : b + block] = rows
# XÁO TRỘN CỘT
def shuffle_cols(board):
    """
    Xáo trộn các cột
    TRONG cùng 1 block
    """
    size = len(board)
    block = int(size ** 0.5)
    for b in range(0, size, block):
        cols = list(range(b, b + block))
        random.shuffle(cols)
        for r in range(size):
            new_part = []
            for c in cols:
                new_part.append(board[r][c])
            for i in range(block):
                board[r][b + i] = new_part[i]
# XÓA Ô
def remove_cells(board, empty):
    """
    Đặt 0 vào các ô ngẫu nhiên
    0 = ô trống
    """
    size = len(board)
    while empty > 0:
        r = random.randint(0, size - 1)
        c = random.randint(0, size - 1)
        if board[r][c] != 0:
            board[r][c] = 0
            empty -= 1
