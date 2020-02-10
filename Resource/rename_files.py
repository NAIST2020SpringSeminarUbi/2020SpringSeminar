import glob
import os

files = sorted(glob.glob("./Torii_VB/*.*"))


for i, old_name in enumerate(files):
    # ファイル名の決定
    new_name = "./Torii_VB/鳥居_{0:06d}.txt".format(i + 1)
    # ファイル名の変更
    os.rename(old_name, new_name)
    # 変更の表示
    print(old_name + " → " + new_name)
    num = i
