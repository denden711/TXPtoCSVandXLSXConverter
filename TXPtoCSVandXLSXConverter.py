import tkinter as tk
from tkinter import filedialog
import csv
import glob
import os

def convert_txp_to_csv(txp_path):
    # 出力するCSVファイルのパスを決定
    csv_path = txp_path.rsplit('.', 1)[0] + '.csv'
    
    # 既にCSVファイルが存在するか確認
    if os.path.exists(csv_path):
        print(f"既に存在するためスキップ: {csv_path}")
        return
    
    # CSVファイルが存在しない場合、変換処理を実行
    with open(txp_path, 'r') as infile, open(csv_path, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile)
        for row in reader:
            writer.writerow(row)
    print(f"変換完了: {csv_path}")

def select_folder_and_convert():
    # フォルダ選択ダイアログを表示
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return
    
    # 指定フォルダ内の.txpファイルを検索
    txp_files = glob.glob(os.path.join(folder_path, '*.txp'))
    
    # 各.txpファイルをCSVに変換（既にCSVが存在する場合はスキップ）
    for txp_file in txp_files:
        convert_txp_to_csv(txp_file)
    
    print("すべての処理が完了しました。")

# GUIの初期化
root = tk.Tk()
root.withdraw()  # メインウィンドウを非表示にしてダイアログのみを表示

# フォルダ選択と変換プロセスの実行
select_folder_and_convert()
