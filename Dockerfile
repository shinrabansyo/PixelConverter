# ベースイメージとして公式のPythonイメージを使用
FROM python:3.9-slim

# Pillowライブラリのインストール
RUN pip install Pillow

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY convert.py .
COPY input.png .

# コンテナ起動時に自動的にconvert.pyを実行（デフォルトで input.png -> output.png）
ENTRYPOINT ["python", "convert.py", "input.png", "output.png"]
