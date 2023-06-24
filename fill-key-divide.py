import cv2
import numpy as np
import keyboard 

Ip = input('fill/keyに分離させたい静止画ファイルを指定してください:')

# 画像ファイルの読み込み
img = cv2.imread(Ip, cv2.IMREAD_UNCHANGED)

# imgがNoneの場合、エラーを出力して処理を終了する
if img is None:
    print('Failed to read the input image')
    exit()

# アルファチャンネルが存在する場合のみ、アルファチャンネルの取得を行う
if img.shape[-1] == 4:
    alpha = img[:, :, 3]
else:
    alpha = None
    print('Failed to read alpha channel')
    exit()

# Fill画像の作成
fill = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
if alpha is not None:
    fill[:, :, 0] = fill[:, :, 0] * (alpha / 255)
    fill[:, :, 1] = fill[:, :, 1] * (alpha / 255)
    fill[:, :, 2] = fill[:, :, 2] * (alpha / 255)

# Key画像の作成
key = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
if alpha is not None:
    key[:, :, 0] = key[:, :, 0] * ((255 - alpha) / 255)
    key[:, :, 1] = key[:, :, 1] * ((255 - alpha) / 255)
    key[:, :, 2] = key[:, :, 2] * ((255 - alpha) / 255)

# 画像ファイルの書き出し
cv2.imwrite('fill.png', fill)
cv2.imwrite('key.png', key)

