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

1. Download the latest executable from [Releases](../../releases)
2. Double-click to run (or `./ytdl-app` on Linux/macOS)
3. Enter a YouTube URL
4. Select your preferred quality
5. Choose download location
6. Click Download!

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