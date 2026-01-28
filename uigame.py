# UIGAME.PY
# IMPORT THƯ VIỆN GUIZERO
# Box        : khung chứa các widget khác
# Text       : hiển thị chữ
# PushButton : nút bấm
from guizero import Box, Text, PushButton
# BIẾN TOÀN CỤC
# lưu số mà người chơi đang chọn (1–9)
# ban đầu chưa chọn gì nên để None
selected_number = None
# danh sách 2 chiều lưu các nút ô sudoku
# cell_buttons[row][col] -> PushButton của ô đó
# dùng để truy cập nhanh khi người chơi bấm ô
cell_buttons = []
current_board = []     # board người chơi đang điền
solution_board = []    # board lời giải đúng
cell_buttons = []      # nút giao diện
# HÀM CHỌN SỐ
def choose_number(number):
    """
    Hàm này chạy khi người chơi bấm
    vào nút số bên dưới (1-9)
    """
    global selected_number
    # lưu lại số mà người chơi chọn
    selected_number = number
# HÀM CLICK VÀO Ô SUDOKU
def cell_clicked(row, col):
    """
    Hàm này chạy khi người chơi bấm
    vào một ô trống trong bảng sudoku
    """
    # chưa chọn số thì không làm gì
    if selected_number is None:
        return
    # cập nhật board người chơi
    current_board[row][col] = selected_number
    button = cell_buttons[row][col]
    button.text = str(selected_number)
    # === CHECK ĐÚNG / SAI ===
    if selected_number == solution_board[row][col]:
        button.bg = "lightgreen"   # đúng
    else:
        button.bg = "lightcoral"   # sai
def create_board(parent_box, board):
    """
    parent_box : box cha (gamebox trong main.py)
    board      : bảng sudoku dạng list 2 chiều
    """
    global cell_buttons
    # kích thước bảng (4 hoặc 9)
    size = len(board)
    # kích thước block (2 hoặc 3)
    block = int(size ** 0.5)
    # box chứa toàn bộ bảng sudoku
    # layout = "grid" để xếp các block thành hình vuông
    board_box = Box(parent_box, layout = "grid")
    # reset danh sách nút mỗi lần tạo game mới
    cell_buttons = []
    # tạo danh sách rỗng size x size
    for r in range(size):
        cell_buttons.append([None] * size)
    # duyệt từng block lớn theo hàng
    for block_row in range(block):
        # duyệt từng block lớn theo cột
        for block_col in range(block):
            # mỗi block lớn là một box riêng có viền
            block_box = Box(
                board_box,
                layout = "grid",              # các ô trong block xếp dạng lưới
                border = True,                # tạo viền block
                grid = [block_col, block_row] # vị trí block trong bảng lớn
            )
            # duyệt từng ô nhỏ trong block
            for r in range(block):
                for c in range(block):
                    # tính vị trí thật trong bảng sudoku
                    real_row = block_row * block + r
                    real_col = block_col * block + c
                    # giá trị tại ô đó
                    value = board[real_row][real_col]
                    # nếu ô trống (0)
                    if value == 0:
                        button = PushButton(
                            block_box,
                            text = "",                     # không hiện số
                            width = 3,
                            height = 1,
                            command = cell_clicked,        # khi bấm ô
                            args = [real_row, real_col],   # truyền vị trí ô
                            grid = [c, r]                  # vị trí trong block
                        )
                    else:
                        # ô có sẵn số -> khóa lại, không cho sửa
                        button = PushButton(
                            block_box,
                            text = str(value),
                            width = 3,
                            height = 1,
                            enabled = False,           # vô hiệu hóa
                            grid = [c, r]
                        )
                    # lưu nút vào danh sách 2 chiều
                    cell_buttons[real_row][real_col] = button
# TẠO DÃY NÚT SỐ (1–9)
def create_controls(parent_box, size):
    """
    Tạo các nút số bên dưới bảng
    để người chơi chọn số cần điền
    """
    # box chứa các nút số
    control_box = Box(parent_box, layout = "grid")
    # tạo nút từ 1 đến size (4 hoặc 9)
    for i in range(1, size + 1):
        PushButton(
            control_box,
            text = str(i),                 # số hiển thị trên nút
            width = 3,
            command = choose_number,       # khi bấm thì chọn số
            args = [i],                    # truyền số được chọn
            grid = [(i - 1) % size,        # cột
                    (i - 1) // size]       # hàng
        )
# HÀM BẮT ĐẦU GAME
def start_game(parent_box, board, solution):
    """
    Hàm này được gọi từ main.py
    khi người chơi nhấn Start Game
    """
    global current_board, solution_board, cell_buttons

    current_board = board
    solution_board = solution
    # xóa toàn bộ widget cũ trong gamebox
    # để tránh chồng giao diện khi chơi lại
    for widget in parent_box.children:
        widget.destroy()
    # tiêu đề game
    Text(parent_box, text = "SUDOKU", size = 20)
    # tạo bảng sudoku
    create_board(parent_box, board)
    # tạo dãy nút số
    create_controls(parent_box, len(board))
