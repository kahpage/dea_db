from pathlib import Path
from db_structs import Circle, is_to_add, Source, Medium, ReliabilityTypes, OriginTypes
from bs4 import BeautifulSoup
import lxml
import json
import openpyxl
import re

def remove_span(string: str) -> str:
    # use re
    return re.sub(r'<span[^>]*>.*?</span>', r'', string)

def clean_link(link: str) -> str:
    # remove web.archive.org prefix if exists
    return re.sub(r'^https?://web\.archive\.org/web/\d+/', '', link)

PATH_CURRENT = Path(__file__).parent

if __name__ == '__main__':
    circles: list[Circle] = [
        Circle(
            aliases=["七色快男児"],
            pen_names=["仁科将人"],
            position="灯1",
            links=["https://x.com/247ruriruri", "https://www.pixiv.net/en/users/1345745"],
            media=[
                Medium("1/1766317346153-1766317218820.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))])
            ],
#            comments=""
        ),
        Circle(
            aliases=["月桃プラネタリウム＆Miraflores"],
            pen_names=["宵やま"],
            position="灯2",
            links=["https://x.com/yamatojiliner5", "https://www.youtube.com/@%E3%81%A1%E3%82%86%E3%82%8A%E3%82%93%E3%81%A1%E3%82%83%E3%82%93%E3%81%AD%E3%82%8B", "https://www.pixiv.net/en/users/302926"],
            media=[
                Medium("1/1765354721811-circle_cut.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))])
            ],
#            comments=""
        ),
        Circle(
            aliases=["あち"],
            pen_names=["やまおかえりこ"],
            position="灯3",
            links=["https://x.com/a_c_h_i_1210"],
            media=[
                Medium("1/1765374950444-IMG_6548.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))])
            ],
            comments="魔理沙ティッシュポーチ@東方星蓮船モチーフ\n魔理沙ペンケース"
        ),
        Circle(
            aliases=["あんころ餅出張所"],
            pen_names=["赤福"],
            position="灯4",
            links=["https://x.com/kenpi_imo01000", "https://www.youtube.com/channel/UCH3YLdBKYZwaYQj-ADT5Hdw", "https://www.pixiv.net/en/users/50645422"],
            media=[
                Medium("1/LTUzLmpwZw==.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1766235473367-G8m9rMabgAAdFLR.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1766235473779-G8m9rMYbAAAeR4E.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/lKgucG5n.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))])
            ],
           comments="当サークルはドット絵のグッズを中心に活動しているサークルです。今回の魔理沙オンリーでは新作の香霖堂衣装の魔理沙アクキーを中心に、シールやクリアファイルも持って行きます～！\n・アクリルキーホルダー（600円）\n→魔理沙以外もあります。\n・シール（100円）\n→ポケモンパンのオマケシールみたいな手触りのやつです。\n・クリアファイル+シール（500円）\n→両面印刷で全キャラ大集合のクリアファイルです。上記のシールがランダムで1枚入ってます。"
        ),
        Circle(
            aliases=["min it's"],
            pen_names=["イルミーネ"],
            position="灯7",
            links=["https://x.com/min_it_s", "https://www.pixiv.net/en/users/105218199"
                   "https://lit.link/en/minits", 
                   "https://min-it-s.booth.pm/",
                   "https://bsky.app/profile/min-it-s.bsky.social",
                   "https://www.threads.com/@min_it_s",
                   "https://www.instagram.com/min_it_s/",
                   "https://mixi.social/@min_it_s",
                   ],
            media=[
                Medium("1/1762244214510-circle_cut.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/cGc=.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/grPjg5Tjg7wuanBn.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/huaymS5qcGc=.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/mS5qcGc=.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))])
            ],
            comments="╭━━━━━━━━━━━━━━╮\n꒰ঌ💜魔理沙オンリーお品書き💜໒꒱\n╰━━ｖ━━━━━━━━━━━╯\n\n『たまゆらの灯は夜を還く』\n参加します...!!✨\n\n‧ ₊˚ ୨୧ ゆめかわメイド魔理沙୨୧˚₊ ‧\nなどの魔理沙のグッズを頒布です໒꒱\nよろしくお願いします...!!🌟\n\nʚ 配置：灯7 ɞ"
        ),
        Circle(
            aliases=["工房-白蛇神宮社"],
            pen_names=["春岡茅秋"],
            position="灯8",
            links=["https://x.com/haruokatisyu193"],
            media=[
                Medium("1/q-OAgC5wbmc=.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ],
#            comments=""
        ),
        Circle(
            aliases=["東方生活教導団"],
            pen_names=["m4go"],
            position="灯10",
            links=["https://x.com/_m4go_", "https://www.pixiv.net/en/users/15662978"],
            media=[
                Medium("1/1762480920362-circle_cut.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ],
#            comments=""
        ),
        Circle(
            aliases=["ShellBlade"],
            pen_names=["水斗"],
            position="灯11",
            links=["https://x.com/SB_Hiroron"],
            media=[
                Medium("1/Zw==.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ],
#            comments=""
        ),
        Circle(
            aliases=["ズガキヤ金山本店"],
            pen_names=["オーナー橙"],
            position="灯12",
            links=["https://x.com/niwatatsuG", "https://www.pixiv.net/en/users/846661"],
            media=[
                Medium("1/cG5n.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ],
#            comments=""
        ),
        Circle(
            aliases=["Magus Wortcraft"],
            pen_names=["きー"],
            position="灯13",
            links=["https://x.com/kiiii326"],
            media=[
                Medium("1/1757068388803-maguswortcraft_circlecut.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ],
#            comments=""
        ),
        Circle(
            aliases=["あとりえバルボン"],
            pen_names=["バルボン"],
            position="灯14",
            links=["https://x.com/balbon0218", "https://www.pixiv.net/en/users/89199262"],
            media=[
                Medium("1/LnBuZw==.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/IDEucG5n.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/IDIucG5n.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1766238529392-251220193430940~2.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1762962368775-251113003851110~2.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1762962438119-251113004013335~2.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ],
           comments="サンタ魔理沙アクキー\n約80×60サイズの大きめのアクキーです\n変なミニタオル\n変Tデザインのミニタオルです(25×25)\nなミニタオル2\nちやりちゃんデザインのミニタオルです(25×25)"
        ),
        Circle(
            aliases=["虹持屋"],
            pen_names=["みかげ"],
            position="灯15",
            links=["https://x.com/Remikaflan", "https://sites.google.com/view/koujiyamfmf/%E3%83%9B%E3%83%BC%E3%83%A0"],
            media=[
                Medium("1/bmc=.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1766398884904-1000013998.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1765798642760-IMG_1187-1.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1765798780596-IMG_1132.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ],
           comments="魔理沙ちゃんのブランケットです。\n大きさは650×480(ｍｍ)です。サイズは個体差により異なる場合がございます。\nイラスト:モフぶとん(@Mofubuton22km)\nA5サイズの魔理沙クリアファイルです。\n個包装でお渡しします。\nイラスト:オブシディアニキ(@Dizzy74665)"
        ),
        Circle(
            aliases=["サークル丙"],
            pen_names=["シズキ"],
            position="灯16",
            links=["https://x.com/circle_HEI", "https://www.youtube.com/@circle_HEI"],
            media=[
                Medium("1/LnBuZw==2.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/MjExMTAwMTUucG5n.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/Zw==2.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/Zw==3.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ],
           comments="近代幻想\nボーカロイド歌唱の東方アレンジCD\nインスト楽曲もあります。\n普通になる。\n魔理沙に関連する原曲のみで構成されたアレンジ楽曲CD。\n鏡音レンと鏡音リンによる歌唱。\nコールドスリーパー\n東方錦上京の原曲オンリーのシングルCDです。\nA面は「最後は一人は慣れてるから」、B面は「プレステ・ジョアンの黄金境」のアレンジになっています。\nボーカロイドとSynthesizerVによる歌唱です。"
        ),
        Circle(
            aliases=["化けたぬき"],
            pen_names=["里ひかり"],
            position="灯18",
            links=["https://x.com/mimim3kn", "https://mimim3kn.wixsite.com/liliy30", "https://www.pixiv.net/en/users/17943988"],
            media=[
                Medium("1/1765739857139-IMG_1992.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1766435375282-IMG_2081.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1765813294206-IMG_1998.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1765979508286-IMG_2039.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1765979150978-IMG_2035.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1765979203123-IMG_2032.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1765805372283-IMG_1997.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ],
           comments="【アクキー】霧雨魔理沙\n5センチ　星のホログラムのアクキーです\n【缶バッジセット】レイマリ【おめかし】\n38mmの缶バッジセットです\nお花のホログラムでキラキラです❇︎\n【ハンカチ】ぴちゅん魔理沙\n20センチの正方形\n【ハンカチ】読書魔理沙\n20センチ正方形\n【フェルトしおり】霧雨魔理沙\n2025年12月\n【缶バッジセット】あきゅすずちゃんおめかし\nあきゅすずちゃんの缶バッジセットです\n【アクキー】　にっこりこいしちゃん\nにっこりこいしちゃんのアクリルキーホルダーです\n【アクキー】夏のこいしちゃん\n夏のこいしちゃんのアクリルキーホルダーです。\n約6cm\n【アクキー】冬のこいしちゃん\n冬のこいしちゃんのアクリルキーホルダーです。\n約6cm\n【アクキー】小鈴ちゃんのお手紙\n小鈴と手紙のアクキーです。\nピンクカラーのアクリルです。\n6cm\n【スクエイラストカード】　akyusuzu tea time\nakyusuzu tea timeの正方形イラストカードです(右)\n10cm正方形\nトレーシングペーパーの透け感もお楽しみください\n【スクエアイラストカード】　おやすみあきゅすずちゃん\nおやすみあきゅすずちゃんの正方形イラストカードです(左)\n10cmの正方形\nきらきらしたパール調の紙です"
        ),
        Circle(
            aliases=["nil_lie"],
            pen_names=["niru"],
            position="灯19",
            links=["https://x.com/niru___05", "https://www.pixiv.net/en/users/38334959"],
            media=[
                Medium("1/NC5wbmc=.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ],
#            comments=""
        ),
        Circle(
            aliases=["にゃんとかしたい"],
            pen_names=["にゃん"],
            position="灯20",
            links=["https://x.com/NYAN_SHITAI", "https://www.pixiv.net/en/users/16976929"],
            media=[
                Medium("1/1766363917110-2nd.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1766363613423-acrylic_memostand.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))])
            ],
           comments="アクリルメモスタンド/500円"
        ),
        Circle(
            aliases=["とばり湊"],
            pen_names=["こよぬい"],
            position="灯21",
            links=["https://x.com/koyo_nui", "https://bsky.app/profile/koyonui.bsky.social" , "https://www.pixiv.net/en/users/736760"],
            media=[
                Medium("1/iua5ii5qcGc=.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/lOacrF8wMTMuanBn.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/lOacrF8wMDEuanBn.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/lOacrF8wMDIuanBn.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/lOacrF8wMDMuanBn.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/cGc=2.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1763355825268-0.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/1763549382168-nobeezu.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/hu-9kOeUqC5qcGc=.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ],
           comments="A5/本文12p　￥100\n人里の少女達から覗く魔理沙の話。\n魔理沙オンリーコピ本\n人里の少女達から覗く魔理沙の話。\nあれはだれかの凶星\n2025.11.22発行\n\n飯綱丸に焦がれたモブ天狗の少女……から始まる龍×典本です。モブに救いはない。天狗社会に幸あれ。\n六秀日の化け者\n2018.10.21発行\n\n人里で突如湧き出した、命蓮寺に対しての黒い噂話。\n嬉々として取材に走る射命丸だったが……。\n\n緩いミステリー好きの方にお勧め。\n幻想郷延絵図\n2018.6発行\n\n紅～憑の全キャラ+幻想郷全土図を妄想したイラスト集です。\nマキャベリストの成り損ない\n2019.10.13 発行\n\n鬼形獣ex後の、八千慧→早鬼へのどうしようもない感情の話。\nやちさきってBLだと思うんですよね。"
        ),
        Circle(
            aliases=["朔望堂"],
            pen_names=["朔平"],
            position="灯22",
            links=["https://x.com/kazakiri_kikyo"],
            media=[
                Medium("1/cGc=3.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                Medium("1/geabuOOBjS5wbmc=.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ]
        ),
        Circle(
            aliases=["nekojam"],
            pen_names=["みけ"],
            position="灯23",
            links=["https://x.com/mike_ne", "https://www.pixiv.net/en/users/691397"],
            media=[
                Medium("1/1765300412164-IMG_1406.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
                ]
        ),
        Circle(
            aliases=["BLACK　LABEL", "BLACK LABEL"],
            pen_names=["HIKARV"],
            position="灯25,26",
            # links=[""],
            media=[
                Medium("1/gIDlrozmiJAucG5n.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ]
        ),
        Circle(
            aliases=["アイドル魔法使い幽霊"],
            pen_names=["のろろ"],
            position="灯27",
            links=["https://x.com/WhoGoesSlowly", "https://www.youtube.com/@NororoGhost", "https://www.pixiv.net/en/users/2301467"],
            media=[
                Medium("1/Zw==4.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ]
        ),
        Circle(
            aliases=["魔法猫みぃぃ手描きイラスト"],
            pen_names=["魔法猫みぃぃ"],
            position="灯29",
            links=["https://x.com/mahounekomii2", "https://www.youtube.com/@mahounekomii"],
            media=[
                Medium("1/1764046837582-IMG_8714.avif",
                    [Source("https://hamp.ai/event/tamayuratomosibi2025?subEvent=%E3%81%9F%E3%81%BE%E3%82%86%E3%82%89%E3%81%AE%E7%81%AF%E3%81%AF%E5%A4%9C%E3%82%92%E9%82%84%E3%81%8F", (ReliabilityTypes.Reliable, OriginTypes.OfficialExt))]),
            ]
        ),
    ]


    with (PATH_CURRENT / "all_circles_export.json").open("w", encoding='utf-8') as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=4)
    print(f"Saved {len(circles)} circles.")


        