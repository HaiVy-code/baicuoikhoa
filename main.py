# Sudoku / Crossword (ô chữ học tập)

# Sudoku số học.
# Crossword chủ đề kiến thức.

# SUDOKU GAME - MAIN FILE
from guizero import App, Box, Text, Combo, PushButton
from generator import generateboard
from uigame import start_game
# TẠO CỬA SỔ CHÍNH
app = App(title = "Sudoku", height = 550)
# CÁC MÀN HÌNH (BOX)
menubox = Box(app)      # màn hình menu
gamebox = Box(app)      # màn hình chơi game
helpbox = Box(app)      # màn hình hướng dẫn
# ẩn game và help lúc đầu
gamebox.hide()
helpbox.hide()
# NỘI DUNG MENU
Text(menubox, text = "SUDOKU GAME", size = 20)
difficulty = Combo(menubox, options = ["Easy (dễ)", "Medium (trung bình)", "Hard (khó)"], width = 20)
sizechoice = Combo(menubox, options = ["2x2 (4x4)", "3x3 (9x9)"], width = 10)
# NỘI DUNG HELP
Text(helpbox, text = "HOW TO PLAY SUDOKU", size=18)
Text(helpbox, text = """
- Each row has a unique number
- Each column has a unique number
- Each large cell has a unique number
""")
Text(helpbox, text = """
- Mỗi hàng không được trùng lặp số
- Mỗi cột không được trùng lặp số
- Mỗi ô lớn không được trùng lặp số
""")
# HÀM BẮT ĐẦU GAME
def startgame():
    global gamebox
    diff = difficulty.value
    size = sizechoice.value
    # chưa chọn đủ thì không làm gì
    if diff == "" or size == "":
        return
    # tạo board theo size
    if "2x2" in size:
        play_board, solution_board = generateboard("2x2", diff.split()[0])
    else:
        play_board, solution_board = generateboard("3x3", diff.split()[0])
        # xóa gamebox cũ, tạo lại gamebox mới
    gamebox.destroy()
    gamebox = Box(app)
    # ẩn menu và help
    menubox.hide()
    helpbox.hide()
    gamebox.show()
    # vẽ giao diện game
    start_game(gamebox, play_board, solution_board)
    # nút quay lại menu (tạo SAU khi vẽ game)
    PushButton(gamebox, text = "Back to Menu (quay lại)", command = backtomenu)
# HÀM QUAY LẠI MENU
def backtomenu():
    gamebox.hide()
    helpbox.hide()
    menubox.show()
# HÀM MỞ HELP
def showmenu():
    helpbox.show()
    gamebox.hide()
    menubox.hide()
# NÚT BẤM MENU
PushButton(menubox, text = "How to play (cách chơi)", command = showmenu)
PushButton(menubox, text = "Start Game (bắt đầu)", command = startgame)
PushButton(helpbox, text = "Back To Menu (quay lại)", command = backtomenu)
# CHẠY APP
app.display()
