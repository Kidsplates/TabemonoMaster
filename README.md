# たべものマスター

家庭科の「食べもののなかま（3色の食品グループ）」と「旬（しゅん）」を中心に、食べもののことをクイズで覚える知育ゲームです。小学生（中学年くらい）とその親向け。

- 遊ぶ: https://kidsplates.github.io/TabemonoMaster/
- スマホの縦画面で、タップだけで遊べます。PC でも遊べます。

## 遊び方

- なかま分け（3色）: 食べものを 赤（おもに体をつくるもとになる）・黄（おもにエネルギーのもとになる）・緑（おもに体の調子をととのえるもとになる）に分ける。タイムアタックもある
- しゅん: 食べものの旬の季節を答える。ふつう・むずかしいでは「冬がしゅんのたべものはどれ？」の逆向きもまざる
- もとはなに？: とうふ・チーズ・せんべい などが、なにからできているかを答える
- どこを食べてる？: 野菜の、花（つぼみ）・実・葉・茎・根 のどこを食べているかを答える
- りょうりのなかま分け: 料理に入っている食材の色を、ぜんぶ選ぶ
- 行事のたべもの: 行事と、その日に食べるものを結ぶ
- こんだてをつくろう: 和食・洋食・中華の献立で、主食・主菜・副菜・汁物がそろうように、足りない品を選ぶ。むずかしいでは、同じ種類が2つある献立を入れかえる問題もある
- むずかしさは3段階。にがてリスト、ずかん（なかま・旬のカレンダー・もと・どこ・りょうり・行事）がある

## 収録

- 食材 121（3色に分けるもの 107。旬 45・もと 40・どこ 40）
- 料理 56（主食 6・主菜 18・副菜 12・汁物 6・主食とおかずを兼ねる料理 10・主菜にも副菜にもなる料理 4）
- 行事 13

## 作り

- HTML 1枚・素の JavaScript。外から読むのは Google Fonts（M PLUS Rounded 1c）だけ
- `index.html` は `tools/build.py` が `tools/app_template.html` にデータを埋め込んで書き出す。`index.html` は直接編集しない
  - `tools/foods.json` 食材（3色・旬・もと・どこ・解説）
  - `tools/dishes.json` 料理（材料・主食／主菜／副菜／汁物・和洋中）
  - `tools/events.json` 行事
- データを直したら、リポジトリ直下で `python tools/build.py` を実行する。データを確かめて（id の重なり、材料が食材にあるか、絵があるか、旬を足した品に月の資料があるか など）、おかしいところがあれば書き出さずに止まる
- 絵はすべてこのリポジトリのために描いた SVG（`tools/app_template.html` の `ICONS`）。写真・既存のキャラクター・ほかのサイトのイラストは使っていない
- カロリー・量・ダイエットの話はしない。「体にいい／わるい」とは言わず、「〜のもとになる」と言う

## データの出典

### 3色（なかま分け）
- 農林水産省「実践食育ナビ」三色食品群の説明 https://www.maff.go.jp/j/syokuiku/zissen_navi/balance/guide.html
- 文部科学省「食生活学習教材（小学校高学年用）」 https://www.mext.go.jp/a_menu/shotou/eiyou/06050810/001.pdf
- 上の2つの資料だけでは色が決められないもの（えだまめ・とうもろこし・くり など）と、調味料・おかしは、3色の問題に出さない（ずかんで理由を説明している）

### 旬（しゅん）
- 農林水産省「子どもの食育」食べ物と日本の四季 https://www.maff.go.jp/j/syokuiku/kodomo_navi/learn/seasons1.html
- 農林水産省「子どもの食育」食べ物の旬や季節がわかるかな https://www.maff.go.jp/j/syokuiku/kodomo_navi/learn/seasons2.html
- 上の2ページの27品に足した18品は、農林水産省の補助事業でつくられた『飲食事業者のためのインバウンド対応ガイドブック』（2017年）の「食材歳時記」で季節を決めた https://www.maff.go.jp/j/shokusan/gaisyoku/attach/pdf/inbound29-6.pdf
  - 月は品目ごとに別の資料で確かめた（`tools/foods.json` の `sm`）。農畜産業振興機構「食べて知る、野菜の底力」の旬の表 https://alic.go.jp/koho/kikaku03_000610.html 、同「野菜情報」、県・市・水産庁・ジェトロ・北海道大学の資料
- 季節の区切りは、気象庁などが使う区切り（春＝3〜5月・夏＝6〜8月・秋＝9〜11月・冬＝12〜2月）に合わせた。気象庁 よくある質問 https://www.jma.go.jp/jma/kishou/know/faq/faq22.html 、国立天文台 暦Wiki「季節」 https://eco.mtk.nao.ac.jp/koyomi/wiki/B5A8C0E1.html
- 2つの季節にまたがるもの（ぶどう・さば など）、ほとんどがハウスや室内で育てられているもの（こまつな・にら など）、資料どうしで季節が食い違うもの（かぼちゃ・わかさぎ など）は、旬の問題に出さない

### もとはなに？
- 農林水産省「子どもの食育」大豆編 https://www.maff.go.jp/j/syokuiku/kodomo_navi/learn/power11.html
- 同 お米編 https://www.maff.go.jp/j/syokuiku/kodomo_navi/learn/power12.html
- 同 牛乳・乳製品 https://www.maff.go.jp/j/syokuiku/kodomo_navi/learn/power08.html
- 農林水産省 麦の資料 https://www.maff.go.jp/j/syouan/keikaku/soukatu/attach/pdf/mugi_kanren-103.pdf
- 農林水産省「にっぽん伝統食図鑑」練り物 https://www.maff.go.jp/j/keikaku/syokubunka/traditional-foods/bunrui/nerimono.html 、節類（かつおぶし） https://www.maff.go.jp/j/keikaku/syokubunka/traditional-foods/bunrui/fushirui.html 、乾物（にぼし・しらすぼし） https://www.maff.go.jp/j/keikaku/syokubunka/traditional-foods/bunrui/kanbutsu.html

### どこを食べてる？
- 農林水産省「子どもの食育」副菜編（野菜は土からやってくる） https://www.maff.go.jp/j/syokuiku/kodomo_navi/learn/power04.html
- 文部科学省「食生活学習教材（小学校高学年用）」 https://www.mext.go.jp/a_menu/shotou/eiyou/06050810/001.pdf
- 農林水産省「野菜の区分」 https://www.maff.go.jp/j/heya/sodan/1205/05a.html
- しょくようぎく: 山形県の資料 https://www.pref.yamagata.jp/documents/4525/resipisyu-33.pdf

### 行事のたべもの
- 農林水産省「子どもの食育」行事食について https://www.maff.go.jp/j/syokuiku/kodomo_navi/learn/event.html
- 北陸農政局 食育ポスター（農林水産省「和食」より） https://www.maff.go.jp/hokuriku/safe/shokuiku/attach/pdf/poster_5-18.pdf ほか
- 農林水産省 aff「日本の年中行事と食 節分といわし料理」 https://www.maff.go.jp/j/pr/aff/2602/event05.html
- 世田谷区「五節句 七夕」 https://www.city.setagaya.lg.jp/documents/3022/gosekku_shichiseki.pdf
- 川口市立学校給食センター だより「給食で魚について知ろう！」（令和8年5月号、端午の節句の記事） https://www.city.kawaguchi.lg.jp/material/files/group/199/0805_dayori02.pdf

### りょうり・こんだて
- 農林水産省「子どもの食育」主食編・主菜編・副菜編 https://www.maff.go.jp/j/syokuiku/kodomo_navi/learn/power01.html ・ https://www.maff.go.jp/j/syokuiku/kodomo_navi/learn/power05.html ・ https://www.maff.go.jp/j/syokuiku/kodomo_navi/learn/power04.html
- 農林水産省「食事バランスガイド」自由に使える料理イラスト集（料理が主食・主菜・副菜のどれかを、ここで確かめた） https://www.maff.go.jp/j/syokuiku/zissen_navi/yun/illust.html
- 料理の色は、入っている食材の色で数える。油・さとう・粉・調味料は数えない
- このゲームでは汁物を副菜と分けて数える（食事バランスガイドでは野菜の汁物も副菜に数えるので、副菜が空いている問題では汁物を候補に出さない）
- 和食・洋食・中華の分け方は、このゲームの決めごと

## 確認

データは、公開の前にレビューで出典と照らして確かめた。正解が2つになる問題が出ないことは、問題をくり返し作って確かめている。
