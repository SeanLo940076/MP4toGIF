# mp4-to-gif
To implement a basic program which converts an mp4 file to a GIF file. Basically it is called a GIF converter built by using pymovie

# from 
https://github.com/shreyamalogi/mp4-to-gif

# run code

```bash
pip install moviepy
```

```bash
python main.py
```

# 說明
在 moviepy.editor 中，clip.write_gif() 用於將 clip（剪輯）對象轉換為 GIF 文件。該方法的用法如下：

clip.write_gif(filename, fps=None, program='imageio', opt='nq', fuzz=1, loop=0, dispose=True)

其中：

filename：轉換後的 GIF 文件名稱（包括路徑）。
fps：GIF 文件的幀率，預設值為 None（由 clip 的 duration 自動計算）。
program：指定轉換的工具，預設值為 'imageio'，也可以選擇 'ffmpeg'。
opt：指定用於生成 GIF 的選項。預設值 'nq' 表示使用沒有 dithering（抖動）的最近鄰值量化，還可以選擇 'better'、'fast'、'bettercolor' 等選項。
fuzz：GIF 文件的調色板的容錯值，預設為 1。
loop：GIF 文件的循環次數，預設為 0（無限循環）。
dispose：指定 GIF 文件的“Dispose”方法，預設為 True。
該方法將返回轉換後的 GIF 文件的路徑。

# 參數該怎寫才能盡可能減小檔案大小
要減小 GIF 檔案大小，可以調整 clip.write_gif() 方法中的 opt 和 fuzz 參數。

opt 參數可以設置為 'better' 或 'fast' 以減小文件大小，但會以圖像質量的代價換取較低的轉換速度和/或較差的圖像品質。

fuzz 參數指定了GIF文件調色板的容錯值。這是一個介於1和30之間的整數值。較高的容錯值可以導致更大的檔案大小，但通常會提供更好的圖像品質。

以下是一個範例：

clip.write_gif('output.gif', fps=24, opt='fast', fuzz=10)

這將把 clip 轉換為 24 fps 的 GIF 文件，並使用 'fast' 選項和 fuzz 值為 10，以最小化文件大小。你可以調整 opt 和 fuzz 參數的值來優化檔案大小和圖像品質。
