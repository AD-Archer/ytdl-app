# YouTube Downloader

A simple, user-friendly GUI application for downloading YouTube videos with quality selection and audio extraction capabilities.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey.svg)

## ✨ Features

- 🎯 **Multiple Quality Options**: Download videos in 240p, 360p, 480p, 720p, 1080p, or 4K resolution
- 🎵 **Audio Only**: Extract audio in MP3 format
- 📁 **Custom Download Location**: Choose where to save your downloads
- 🖥️ **Clean GUI**: Simple and intuitive interface built with tkinter
- 📦 **Single Executable**: No installation required - just run the executable
- 🚀 **Cross-Platform**: Works on macOS, Windows, and Linux

## 🚀 Quick Start

### For Users (Just want to download)

1. **Download the latest executable from [Releases](../../releases)**
   - Choose your platform: `ytdl-app-windows.zip`, `ytdl-app-macos.zip`, or `ytdl-app-linux.zip`

2. **Extract and run based on your platform:**

   **🪟 Windows:**
   - Extract the ZIP file
   - Double-click `main.exe`
   - If Windows shows "Windows protected your PC" warning:
     - Click "More info" → "Run anyway"
     - Or right-click the file → Properties → Unblock → OK

   **🍎 macOS:**
   - Extract the ZIP file
   - Right-click `main` → "Open" (don't double-click!)
   - If macOS shows "cannot be opened because it is from an unidentified developer":
     - Go to System Preferences → Security & Privacy → General
     - Click "Open Anyway" next to the blocked app message
   - Alternative: Run in Terminal: `chmod +x main && ./main`

   **🐧 Linux:**
   - Extract the ZIP file
   - Open Terminal in the extracted folder
   - Make executable: `chmod +x main`
   - Run: `./main`

3. **Use the app:**
   - Enter a YouTube URL
   - Select your preferred quality  
   - Choose download location
   - Click Download!

### For Developers (Want to build/modify)

```bash
# Clone the repository
git clone https://github.com/ad-archer/ytdl-app.git
cd ytdl-app

# Install dependencies
pip install yt-dlp pyinstaller

# Build executable
pyinstaller --onefile main.py

# Run the app
python main.py
```

## 📋 Requirements

- **For Users**: None! The executable is self-contained
- **For Developers**:
  - Python 3.8+
  - yt-dlp
  - PyInstaller (for building)

## 🛠️ Building from Source

```bash
# Install dependencies
pip install yt-dlp pyinstaller

# Build single executable
pyinstaller --onefile main.py

# The executable will be in dist/main
```

## 📖 Usage

1. **URL Input**: Paste the YouTube video URL
2. **Quality Selection**: Choose from available resolutions
3. **Audio Only**: Check this box to download audio only (MP3)
4. **Download Location**: Click "Browse" to select save location
5. **Download**: Click the green "Download" button

## 🔧 Technical Details

- Built with Python + tkinter for the GUI
- Uses yt-dlp for robust YouTube downloading
- Single executable created with PyInstaller
- Supports all yt-dlp format options

## 🚨 Troubleshooting

### "App can't be opened" (macOS)
- **Solution**: Right-click the file and select "Open" instead of double-clicking
- **Alternative**: System Preferences → Security & Privacy → General → "Open Anyway"

### "Windows protected your PC" (Windows)
- **Solution**: Click "More info" → "Run anyway"
- **Alternative**: Right-click file → Properties → Unblock → OK

### "Permission denied" (Linux)
- **Solution**: Run `chmod +x main` first, then `./main`

### App won't start
- Make sure you downloaded the correct version for your operating system
- Try running from Terminal/Command Prompt to see error messages
- Ensure you have an internet connection for downloading videos

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational purposes only. Please respect YouTube's Terms of Service and copyright laws. Only download content you have permission to download.

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The powerful YouTube downloader
- [PyInstaller](https://pyinstaller.org/) - For creating standalone executables