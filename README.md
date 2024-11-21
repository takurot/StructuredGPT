# StructuredGPT

StructuredGPT は、OpenAI の API を使用して、指定したトピックに関する段階的な思考プロセスを自動化し、議論内容をマークダウン形式で出力するツールです。

## 特徴

- トピックに基づいて段階的に議論を進める
- 各ステップの結果をマークダウン形式で保存
- 背景情報の収集、賛成・反対意見の検討、長期的影響の予測などを含む
- 最終結論を生成し、すべての内容を `output.md` ファイルに保存

## 必要な環境

- Python 3.7 以上
- OpenAI API キー

## インストール

1. このリポジトリをクローンします。

   ```bash
   git clone https://github.com/yourusername/StructuredGPT.git
   cd StructuredGPT
   ```

2. 必要な Python パッケージをインストールします。

   ```bash
   pip install openai
   ```

3. スクリプト内の `openai.api_key` をあなたの API キーに置き換えてください。

   ```python
   openai.api_key = "your-api-key"
   ```

## 使用方法

以下のコマンドでスクリプトを実行し、議論したいトピックを引数として指定します。

```bash
python StructuredGPT.py "日本企業がAI時代に勝利者になるにはどうしたらよいか？"
```

実行後、議論内容が `output.md` ファイルに保存されます。

### 引数

- **トピック**: 議論の対象となるトピックを文字列で指定します。

## 出力例

実行後、以下のような内容が `output.md` に保存されます。

```markdown
# 議論: 日本企業が AI 時代に勝利者になるにはどうしたらよいか？

## Step 1: 問題の分析

日本企業が AI 時代で直面している課題は...

## Step 2: 背景情報の収集

AI 市場における日本の立ち位置は...

## Step 3: 関係者の視点

- 従業員: AI スキル向上が必要
- 経営者: デジタルトランスフォーメーションの推進が必須

## Step 4: 賛成意見の収集

AI を活用することで...

## Step 5: 反対意見の収集

AI 導入には...

## Step 6: 長期的影響の予測

長期的には...

## Step 7: 最終結論

これらを踏まえると、日本企業は...
```

## プロジェクト構成

```
StructuredGPT/
│
├── StructuredGPT.py  # メインスクリプト
├── README.md         # このドキュメント
└── output.md         # 実行結果が保存されるファイル
```

## 注意点

- OpenAI の API キーが必要です。取得方法は [OpenAI 公式サイト](https://platform.openai.com/) を参照してください。
- API の利用には料金が発生する場合があります。詳細は [OpenAI の料金ページ](https://openai.com/pricing) を確認してください。

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 貢献

貢献を歓迎します！バグ報告、機能追加の提案、プルリクエストをお待ちしています。
