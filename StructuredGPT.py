from openai import OpenAI
import argparse

# OpenAI APIキーの設定
client = OpenAI()

def call_openai_api(prompt, max_tokens=1000):
    """APIを呼び出して結果を返す"""
    response = client.chat.completions.create(
        model="gpt-4o",  # 使用するモデルに応じて変更
        messages=[
            {"role": "system", "content": "あなたは段階的に思考プロセスを進めるAIアシスタントです。"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

def save_to_markdown(filename, content):
    """マークダウンファイルに内容を保存する"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def main(topic):
    # 出力用のマークダウン文字列
    markdown_content = f"# 議論: {topic}\n\n"

    # ステップ1: 問題の分析
    step1_prompt = f"""
    以下のトピックについて問題を分析し、必要な情報をリストアップしてください。
    トピック: {topic}
    """
    step1_response = call_openai_api(step1_prompt)
    markdown_content += f"## Step 1: 問題の分析\n{step1_response}\n\n"

    # ステップ2: 背景情報の収集
    step2_prompt = f"""
    トピック: {topic}
    このトピックに関連する背景情報や統計データを収集してください。
    """
    step2_response = call_openai_api(step2_prompt)
    markdown_content += f"## Step 2: 背景情報の収集\n{step2_response}\n\n"

    # ステップ3: 関係者の視点
    step3_prompt = f"""
    トピック: {topic}
    このトピックが影響を与える関係者をリストアップし、それぞれの視点から賛成意見と反対意見を考えてください。
    """
    step3_response = call_openai_api(step3_prompt)
    markdown_content += f"## Step 3: 関係者の視点\n{step3_response}\n\n"

    # ステップ4: 賛成意見の収集
    step4_prompt = f"""
    トピック: {topic}
    上記の分析を踏まえ、このトピックについて賛成意見を列挙してください。
    """
    step4_response = call_openai_api(step4_prompt)
    markdown_content += f"## Step 4: 賛成意見の収集\n{step4_response}\n\n"

    # ステップ5: 反対意見の収集
    step5_prompt = f"""
    トピック: {topic}
    上記の分析を踏まえ、このトピックについて反対意見を列挙してください。
    """
    step5_response = call_openai_api(step5_prompt)
    markdown_content += f"## Step 5: 反対意見の収集\n{step5_response}\n\n"

    # ステップ6: 長期的影響の予測
    step6_prompt = f"""
    トピック: {topic}
    このトピックについて、長期的に考えられるメリットとデメリットをリストアップしてください。
    """
    step6_response = call_openai_api(step6_prompt)
    markdown_content += f"## Step 6: 長期的影響の予測\n{step6_response}\n\n"

    # ステップ7: 最終結論
    step7_prompt = f"""
    トピック: {topic}
    賛成意見:
    {step4_response}

    反対意見:
    {step5_response}

    長期的影響:
    {step6_response}

    賛成意見、反対意見、長期的影響を加味し、最終的にこのトピックに関する結論を出してください。
    """
    step7_response = call_openai_api(step7_prompt)
    markdown_content += f"## Step 7: 最終結論\n{step7_response}\n\n"

    # マークダウンファイルに保存
    save_to_markdown("output.md", markdown_content)
    print("議論内容が 'output.md' に保存されました。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="トピックを指定して段階的な思考を行うスクリプト")
    parser.add_argument("topic", type=str, help="議論したいトピックを入力してください")
    args = parser.parse_args()
    main(args.topic)