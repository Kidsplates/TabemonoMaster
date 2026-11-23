# -*- coding: utf-8 -*-
"""たべものマスターの index.html を作る。

tools/app_template.html に、tools/ の3つのデータ（foods.json・dishes.json・events.json）を
埋め込んで、リポジトリ直下の index.html に書き出す。index.html は直接編集しない。

使い方（リポジトリ直下で）:
    python tools/build.py

データを確かめて、おかしいところがあれば書き出さずに止まる。
"""
import json
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent

GROUPS = {'r', 'y', 'g', None}          # 3色（赤・黄・緑、None は色に数えない）
SEASONS = {'haru', 'natsu', 'aki', 'fuyu', None}
BASES = {'daizu', 'milk', 'kome', 'komugi', 'sakana', None}   # もとはなに？
PARTS = {'tsubomi', 'mi', 'ha', 'kuki', 'ne', None}          # どこを食べてる？
DISH_KINDS = {'shu', 'sai', 'fuku', 'shiru', 'one', 'both'}  # 主食・主菜・副菜・汁物・主食とおかず・主菜にも副菜にも
STYLES = {'wa', 'yo', 'chu'}                                 # 和食・洋食・中華


def load(name, key):
    with open(TOOLS / name, encoding='utf-8') as f:
        return json.load(f)[key]


def dump(key, items):
    # 1行に1品。差分が見やすいように、この形をくずさない
    return '{"%s":[\n' % key + ',\n'.join(json.dumps(x, ensure_ascii=False, separators=(',', ':')) for x in items) + '\n]}'


def check(foods, dishes, events, template):
    errs = []
    ids = [x['id'] for x in foods + dishes + events]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        errs.append(f'id が重なっている: {sorted(dup)}')
    fid = {f['id'] for f in foods}
    icons = set(re.findall(r'^\s+([a-z_0-9]+): \{ face:', template, re.M))

    for f in foods:
        i = f['id']
        if not f.get('n'):
            errs.append(f'{i}: 名前（n）がない')
        if f.get('g', 'なし') not in GROUPS:
            errs.append(f'{i}: 3色（g）が r/y/g/null のどれでもない')
        if f.get('s') not in SEASONS:
            errs.append(f'{i}: 旬（s）が季節のどれでもない')
        if f.get('m') not in BASES:
            errs.append(f'{i}: もと（m）がおかしい')
        if f.get('p') not in PARTS:
            errs.append(f'{i}: どこ（p）がおかしい')
        # 旬を「食材歳時記」から足した品は、月を確かめた資料を1つ持つ
        if f.get('ss') == 'g' and not (isinstance(f.get('sm'), list) and len(f['sm']) == 2 and f['sm'][1].startswith('https://')):
            errs.append(f'{i}: 旬の月の資料（sm）がない')
        if i not in icons:
            errs.append(f'{i}: 絵（ICONS）がない')

    for d in dishes:
        i = d['id']
        if d.get('k') not in DISH_KINDS:
            errs.append(f'{i}: 料理の種類（k）がおかしい')
        for x in d.get('ing', []):
            if x not in fid:
                errs.append(f'{i}: 材料 {x} が foods.json にない')
        if not d.get('ing'):
            errs.append(f'{i}: 材料（ing）がない')
        st = [s for s in d.get('st', '').split(',') if s]
        if any(s not in STYLES for s in st):
            errs.append(f'{i}: 系統（st）がおかしい')
        # こんだてに出る料理（主食・主菜・副菜・汁物）は系統を持つ
        if d.get('k') in ('shu', 'sai', 'fuku', 'shiru') and not d.get('kx') and not st:
            errs.append(f'{i}: こんだてに出るのに系統（st）がない')
        if d.get('icon') not in icons:
            errs.append(f'{i}: 絵（icon: {d.get("icon")}）がない')

    for e in events:
        i = e['id']
        if not (1 <= e.get('mo', 0) <= 12):
            errs.append(f'{i}: 月（mo）がおかしい')
        if e.get('icon') not in icons:
            errs.append(f'{i}: 絵（icon: {e.get("icon")}）がない')
    mos = [e['mo'] for e in events]
    if mos != sorted(mos):
        errs.append('events.json が月の順に並んでいない')

    # こんだてで、正しい種類が2つ以上にならないための前提：系統ごとに主食・主菜・副菜・汁物がそろう
    for s in STYLES:
        for k in ('shu', 'sai', 'fuku', 'shiru'):
            if not any(d.get('k') == k and not d.get('kx') and s in d.get('st', '').split(',') for d in dishes):
                errs.append(f'系統 {s} に {k} の料理がない')
    return errs


def main():
    template = (TOOLS / 'app_template.html').read_text(encoding='utf-8')
    foods = load('foods.json', 'foods')
    dishes = load('dishes.json', 'dishes')
    events = load('events.json', 'events')
    errs = check(foods, dishes, events, template)
    if errs:
        print('データにおかしいところがあります。index.html は書き出していません。')
        for e in errs:
            print(' -', e)
        sys.exit(1)
    html = (template
            .replace('{{FOOD_DATA}}', dump('foods', foods))
            .replace('{{DISH_DATA}}', dump('dishes', dishes))
            .replace('{{EVENT_DATA}}', dump('events', events)))
    if any(p in html for p in ('{{FOOD_DATA}}', '{{DISH_DATA}}', '{{EVENT_DATA}}')):
        print('埋め込みの印が残っています。')
        sys.exit(1)
    (ROOT / 'index.html').write_text(html, encoding='utf-8', newline='\n')
    print(f'index.html を書き出しました（食材 {len(foods)}・料理 {len(dishes)}・行事 {len(events)}）')


if __name__ == '__main__':
    main()
