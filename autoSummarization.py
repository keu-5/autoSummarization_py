from youtube_transcript_api import YouTubeTranscriptApi
import openai
openai.organization = "ここにOrganization IDを入力"
openai.api_key = "ここにAPIキーを入力"

id = "ここにYouTubeの動画のIDを入力"

#動画のIDを渡す
transcript_list = YouTubeTranscriptApi.list_transcripts(id)

sentenceList = []

#文字起こしデータを出力(リスト形式に変換)
for transcript in transcript_list:
    for tr in transcript.fetch():
        print(tr)
        sentenceList.append(tr['text'])

#n分割関数
def split_list(l, n):
    """
    リストをサブリストに分割する
    :param l: リスト
    :param n: サブリストの要素数
    :return: 
    """
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]

#リストを三分割
result = list(split_list(sentenceList, len(sentenceList) // 3))

for i in range(3):
    result[i] = '、'.join(result[i])
    result[i].replace('[音楽]、', '')

    result[i] = f"「{result[i]}」を要約してください"

def Ask_ChatGPT(message):
    # 応答設定
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", # モデルを選択
        messages = [{
            "role":"user", # 役割
            "content":message, # メッセージ 
        }],
    
        max_tokens = 1024, # 生成する文章の最大単語数
        n = 1, # いくつの返答を生成するか
        stop = None, # 指定した単語が出現した場合、文章生成を打ち切る
        temperature = 0.5, # 出力する単語のランダム性（0から2の範囲） 0であれば毎回返答内容固定
    )
    # 応答
    response = completion.choices[0].message.content
    # 応答内容出力
    return response

lastLesult = []

#要約第一段階
for i in range(len(result) - 1):
    
    # 質問内容
    message = str(result[i])
    # ChatGPT起動
    res = Ask_ChatGPT(message)
    # 出力
    print(res)
    lastLesult.append(res)

#txtファイルに書き込み
f = open(f'./{id}.txt', 'a')

for i in range(len(lastLesult)):
    print(lastLesult[i])
    f.writelines(lastLesult[i])
    print("--------------------------------------------------------")
    f.writelines("----------------------------------------------------------\n")

f.close()

