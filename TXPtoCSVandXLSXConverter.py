import tkinter as tk
from tkinter import filedialog
import pandas as pd
import glob
import os

def convert_txp_to_csv(txp_path):
    csv_path = txp_path.rsplit('.', 1)[0] + '.csv'
    if not os.path.exists(csv_path):
        # TXPファイルをデータフレームとして読み込む
        df = pd.read_csv(txp_path, delimiter='\t')
        # CSVファイルとして保存
        df.to_csv(csv_path, index=False)
        print(f"変換完了: {csv_path}")
    else:
        print(f"既に存在するためスキップ: {csv_path}")

def convert_csv_to_xlsx(csv_path):
    xlsx_path = csv_path.rsplit('.', 1)[0] + '.xlsx'
    if not os.path.exists(xlsx_path):
        # CSVファイルをデータフレームとして読み込む
        df = pd.read_csv(csv_path)
        # XLSXファイルとして保存
        df.to_excel(xlsx_path, index=False)
        print(f"変換完了: {xlsx_path}")
    else:
        print(f"既に存在するためスキップ: {xlsx_path}")

def select_folder_and_convert():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return
    
    txp_files = glob.glob(os.path.join(folder_path, '*.txp'))
    for txp_file in txp_files:
        # .txpを.csvに変換
        convert_txp_to_csv(txp_file)
        # 変換した.csvを.xlsxに変換
        convert_csv_to_xlsx(txp_file.rsplit('.', 1)[0] + '.csv')
    
    print("すべての処理が完了しました。")

# GUIの初期化
root = tk.Tk()
root.withdraw()

# フォルダ選択と変換プロセスの実行
select_folder_and_convert()
