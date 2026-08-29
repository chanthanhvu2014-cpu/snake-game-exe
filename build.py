import os
import subprocess
import sys

def build_exe():
    """Build the snake game into an executable file"""
    print("🔨 Đang xây dựng file .exe cho Snake Game...")
    print("=" * 50)
    
    # Check if pyinstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("❌ PyInstaller chưa được cài đặt!")
        print("📦 Đang cài đặt PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Check if pygame is installed
    try:
        import pygame
    except ImportError:
        print("❌ Pygame chưa được cài đặt!")
        print("📦 Đang cài đặt Pygame...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    
    print("\n✅ Tất cả dependencies đã sẵn sàng!")
    print("\n🚀 Đang tạo file .exe...")
    print("=" * 50)
    
    # Build the exe
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=SnakeGame",
        "--add-data=snake_game.py:.",
        "snake_game.py"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("\n" + "=" * 50)
        print("✨ Xây dựng thành công!")
        print("=" * 50)
        print("\n📁 File .exe nằm tại:")
        exe_path = os.path.join(os.getcwd(), "dist", "SnakeGame.exe")
        print(f"   {exe_path}")
        print("\n💡 Bạn có thể:")
        print("   1. Chạy file .exe trực tiếp từ thư mục 'dist'")
        print("   2. Copy file .exe sang bất kỳ đâu để chạy")
        print("   3. Chia sẻ file .exe cho bạn bè (không cần Python)")
        
    except subprocess.CalledProcessError as e:
        print("\n❌ Lỗi khi xây dựng!")
        print(f"   {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_exe()