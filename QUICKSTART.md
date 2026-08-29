# Hướng Dẫn Nhanh Tạo File .EXE

## 🎯 Mục Tiêu
Chuyển đổi game Rắn Săn Mồi từ Python thành file .exe có thể chạy độc lập trên Windows.

---

## 📋 Yêu Cầu Trước Khi Bắt Đầu

✅ **Bạn cần có:**
- Windows 7 trở lên
- Python 3.7+ (tải từ python.org)
- Kết nối Internet để tải dependencies

---

## 🚀 Bước 1: Chuẩn Bị Môi Trường

### 1.1 Tải Python
1. Truy cập: https://www.python.org/downloads/
2. Tải **Python 3.10 hoặc mới hơn**
3. **QUAN TRỌNG**: Khi cài đặt, chọn ✅ "Add Python to PATH"
4. Chọn "Install Now"

### 1.2 Kiểm Tra Python
Mở PowerShell hoặc CMD và gõ:
```bash
python --version
```
Nếu hiển thị version (ví dụ: Python 3.10.0) → ✅ Thành công

---

## 🎮 Bước 2: Chuẩn Bị Game

### 2.1 Tải Repository
Mở PowerShell tại Desktop (Shift + Click phải → "Open PowerShell window here")

Gõ lệnh:
```bash
git clone https://github.com/chanthanhvu2014-cpu/snake-game-exe.git
cd snake-game-exe
```

Hoặc tải thủ công từ GitHub và giải nén vào thư mục

### 2.2 Cài Đặt Dependencies
```bash
pip install -r requirements.txt
```

Đợi cho đến khi thấy thông báo "Successfully installed"

---

## 🔨 Bước 3: Tạo File .EXE

### ⚡ Cách 1: Sử Dụng Script Build (DỄ NHẤT)

#### Trên Windows:
```bash
python build.py
```
Hoặc nhấp đôi vào `build.bat`

#### Trên Mac/Linux:
```bash
bash build.sh
```

**Đợi quá trình hoàn thành (khoảng 2-5 phút)**

### 🛠️ Cách 2: Sử Dụng Lệnh PyInstaller Trực Tiếp

```bash
pyinstaller --onefile --windowed --name=SnakeGame snake_game.py
```

---

## ✅ Bước 4: Xác Nhận Thành Công

### 📁 Tìm File .EXE
Sau khi build xong, file .exe nằm tại:
```
snake-game-exe/dist/SnakeGame.exe
```

### 🎮 Chạy Game
Nhấp đôi vào `SnakeGame.exe` để chơi!

---

## 📊 Cây Thư Mục Sau Build

```
snake-game-exe/
├── snake_game.py
├── requirements.txt
├── build.py
├── build.bat
├── README.md
├── dist/
│   ├── SnakeGame.exe          ← FILE NÀY!
│   ├── SnakeGame.exe.manifest
│   └── ... (các file hỗ trợ)
├── build/
│   └── (thư mục build tạm)
└── SnakeGame.spec             (spec file)
```

---

## 🔄 Cách Sử Dụng File .EXE

### ✨ Ưu Điểm:
- ✅ Chạy trên bất kỳ máy Windows nào
- ✅ Không cần cài Python
- ✅ Có thể copy, chia sẻ, chuyển đi
- ✅ Chạy nhanh

### 📦 Phân Phối:
```bash
# Copy file từ dist/
cp dist/SnakeGame.exe ~/Desktop/

# Hoặc gửi cho bạn bè - họ chỉ cần nhấp đôi!
```

---

## ⚠️ Khắc Phục Sự Cố

### ❌ Lỗi: "Python is not recognized"
**Giải pháp**: Cài đặt lại Python với ✅ "Add to PATH"

### ❌ Lỗi: "No module named 'pygame'"
**Giải pháp**:
```bash
pip install pygame
```

### ❌ Lỗi: "No module named 'PyInstaller'"
**Giải pháp**:
```bash
pip install pyinstaller
```

### ❌ File .exe không chạy
**Giải pháp**:
```bash
pip install --upgrade pygame
pyinstaller --onefile --windowed --name=SnakeGame snake_game.py
```

### ❌ Lỗi "DLL not found"
**Giải pháp**:
```bash
pip uninstall pygame -y
pip install pygame --upgrade
pyinstaller --onefile --windowed --name=SnakeGame snake_game.py
```

---

## 🎮 Hướng Dẫn Chơi Game

### Điều Khiển:
- **⬆️⬇️⬅️➡️**: Di chuyển rắn
- **SPACE**: Khởi động lại game
- **ESC**: Thoát game

### Luật Chơi:
- Ăn mồi (hình vuông đỏ) để tăng điểm
- Không va chạm vào tường hoặc chính mình
- Mỗi mồi ăn được = 10 điểm

---

## 💡 Mẹo Nâng Cao

### Tạo Shortcut Trên Desktop
1. Nhấp chuột phải vào `SnakeGame.exe`
2. Chọn "Send to" → "Desktop (create shortcut)"
3. Game sẽ xuất hiện trên Desktop

### Thêm Icon Tùy Chỉnh
1. Tìm hoặc tạo file `icon.ico`
2. Đặt vào thư mục dự án
3. Sửa lệnh build:
```bash
pyinstaller --onefile --windowed --icon=icon.ico --name=SnakeGame snake_game.py
```

### Tạo Installer (Nâng cao)
Sử dụng NSIS hoặc Inno Setup để tạo installer chuyên nghiệp

---

## 📚 Tài Liệu Thêm

- [Python Documentation](https://docs.python.org/3/)
- [PyInstaller Docs](https://pyinstaller.readthedocs.io/)
- [Pygame Documentation](https://www.pygame.org/docs/)

---

## 🎉 Hoàn Thành!

**Xin chúc mừng!** Bạn đã tạo thành công file .exe từ Python!

Bây giờ bạn có thể:
- 🎮 Chơi game bất kỳ lúc nào
- 📤 Chia sẻ với bạn bè
- 🔧 Sửa đổi source code và build lại
- 🚀 Phát triển thêm các game khác

---

**Happy Gaming! 🎮🐍**
