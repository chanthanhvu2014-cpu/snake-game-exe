# Snake Game - Rắn Săn Mồi 🐍

Một trò chơi rắn săn mồi cổ điển được phát triển bằng Python và Pygame, có thể chuyển đổi thành file .exe để chạy trên Windows.

## Tính Năng

- 🎮 Gameplay cổ điển với điều khiển mượt
- 🎯 Hệ thống điểm số
- 🎨 Giao diện đơn giản, dễ sử dụng
- 💻 Có thể tạo thành file .exe

## Cách Chơi

- **Mũi tên lên/xuống/trái/phải**: Di chuyển rắn
- **SPACE**: Khởi động lại game khi thua
- **ESC**: Thoát game

## Yêu Cầu

- Python 3.7+
- pygame
- pyinstaller (để tạo .exe)

## Cài Đặt

### 1. Clone repository
```bash
git clone https://github.com/chanthanhvu2014-cpu/snake-game-exe.git
cd snake-game-exe
```

### 2. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 3. Chạy game
```bash
python snake_game.py
```

## Tạo File .exe

### Cách 1: Sử dụng PyInstaller (Dễ nhất)

```bash
# Tạo .exe đơn giản
pyinstaller --onefile --windowed --icon=snake_icon.ico snake_game.py

# Hoặc tạo .exe với tên tuỳ chỉnh
pyinstaller --onefile --windowed --icon=snake_icon.ico --name="SnakeGame" snake_game.py
```

File .exe sẽ nằm trong thư mục `dist/`

### Cách 2: Sử dụng Script Build (Tự động)

Chạy script `build.py`:
```bash
python build.py
```

## Hướng Dẫn Chi Tiết Tạo .exe trên Windows

### Bước 1: Mở Command Prompt
Nhấp chuột phải vào Desktop → "Open PowerShell window here" hoặc mở CMD

### Bước 2: Điều hướng tới thư mục dự án
```bash
cd C:\Users\chant\Desktop\PYTHON\snake-game-exe
```

### Bước 3: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Bước 4: Tạo .exe
```bash
pyinstaller --onefile --windowed --name="SnakeGame" snake_game.py
```

### Bước 5: Tìm file .exe
File .exe nằm tại: `C:\Users\chant\Desktop\PYTHON\snake-game-exe\dist\SnakeGame.exe`

Bạn có thể copy file này ra bất kỳ đâu và chạy trực tiếp mà không cần Python!

## Cấu Trúc Thư Mục

```
snake-game-exe/
├── snake_game.py          # File chính của game
├── requirements.txt       # Dependencies
├── build.py              # Script để build .exe tự động
├── build_setup.py        # Setup.py cho distutils
└── README.md             # Tài liệu này
```

## Khắc Phục Sự Cố

### Lỗi: "pygame not found"
```bash
pip install pygame
```

### Lỗi: "pyinstaller not found"
```bash
pip install pyinstaller
```

### .exe không chạy hoặc lỗi DLL
Thử cài đặt lại pygame:
```bash
pip install --upgrade pygame
```

## Tác Giả

- chanthanhvu2014-cpu

## License

MIT License - Tự do sử dụng và sửa đổi

---

**Chúc bạn chơi game vui vẻ! 🎮**
