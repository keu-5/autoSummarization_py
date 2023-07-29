### autoSummarization.pyを利用するにあたっての事前準備
このファイルではyoutubeの動画の字幕をまとめ、それらをchatgptによって要約する機能が利用できます

1 コマンドプロンプトを管理者権限で起動し、「*pip install youtube_transcript_api*」と入力、インストールする。その後同様に「*pip install openai*」と入力、インストールする。(初回時のみ)
2 [openAI公式サイト](https://openai.com/)にてopenAIのAPIキーを取得(__キーを取得したら必ずすぐにコピーや撮影して保存すること!!!__)、そしてもともとあるOrganization IDと合わせて用意する（詳しいやり方は聞いたり調べたりして）(初回時のみ)
3 YouTubeにて任意の動画を開き、URLの「*v=*」のあとの文字列をコピー 
例(https://www.youtube.com/watch?v=*TWqJ5P8oaUM*&list=PLF9FCB56776EBCABB&index=1&t=8s)
4 autoSummarization.pyにて指定された箇所にそれぞれ入力、ファイルを実行
5 結果がtxtファイルとしてカレントディレクトリに保存されます
6 あとは自由に使ってください

### temp.pyを利用するにあたっての事前準備
このファイルはautoSummarizationの準備が面倒な人や、APIに制限がかかった人向けです。youtubeの動画の字幕をまとめる機能のみ利用できます。

1 コマンドプロンプトを管理者権限で起動し、「*pip install youtube_transcript_api*」と入力、インストールする。(すでにインストールしている場合無視してよい)
2 YouTubeにて任意の動画を開き、URLの「*v=*」のあとの文字列をコピー
例(https://www.youtube.com/watch?v=*TWqJ5P8oaUM*&list=PLF9FCB56776EBCABB&index=1&t=8s)
3 ファイルを実行すると「_idを入力してください_」と出るのであらかじめコピーしたidを入力
4 結果がtxtファイルとしてカレントディレクトリに保存されます。
5 あとは自由に使ってください

詳しいやり方は私に聞いたり調べたりしてください。
