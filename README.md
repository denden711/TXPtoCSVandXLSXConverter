# TXPtoCSVandXLSXConverter

## 概要
TXPtoCSVandXLSXConverterは、特定のフォルダ内にある全ての`.txp`ファイルを`.csv`形式に変換し、その後`.xlsx`形式に変換するPythonスクリプトです。このツールはGUIを使用してフォルダを選択し、選択されたフォルダ内のファイルを自動的に変換します。

## システム要件
このスクリプトを実行するには以下のものが必要です:
- Python 3.x
- pandas ライブラリ
- openpyxl ライブラリ
- tkinter ライブラリ

## インストール方法
以下の手順に従って必要なライブラリをインストールします:

```bash
pip install pandas openpyxl
```

## 使い方
1. スクリプトを実行します。
2. ポップアップされるフォルダ選択ダイアログから、変換したいファイルが含まれるフォルダを選択します。
3. スクリプトが自動的にフォルダ内の全`.txp`ファイルを`.csv`に変換し、その後`.xlsx`に変換します。
4. 各ファイルの変換が完了すると、結果がコンソールに表示されます。

## 注意点
- このスクリプトは`.txp`ファイルがタブ区切り形式であることを前提としています。
- すでに変換された`.csv`や`.xlsx`ファイルが存在する場合、そのファイルはスキップされます。

## ライセンス
このプロジェクトはMITライセンスのもとで公開されています。詳細はプロジェクトの`LICENSE`ファイルを参照してください。

