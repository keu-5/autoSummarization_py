from youtube_transcript_api import YouTubeTranscriptApi

id = input("idを入力してください")

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

#リストを五分割
result = list(split_list(sentenceList, len(sentenceList) // 5))

for i in range(5):
    result[i] = '、'.join(result[i])
    result[i].replace('[音楽]、', '')

    result[i] = f"「{result[i]}」を要約してください\n"

f = open(f'./{id}.txt', 'a')

for i in range(len(result)):
    print(result[i])
    f.writelines(result[i])
    print("--------------------------------------------------------")
    f.writelines("----------------------------------------------------------\n")

f.close()