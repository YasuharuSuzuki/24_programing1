CHARACTER_COUNT = 5

character_data = [input().split() for i in range(CHARACTER_COUNT)]
wave_damages = list(map(int, input().split())) # タイダルウエイブのダメージ入力
heal = int(input()) # 回復量入力
thunder_damages = list(map(int, input().split())) # いなづまのダメージ入力

characters = []
for i in range(CHARACTER_COUNT):
    hp = int(character_data[i][0])
    equips = character_data[i][1:]  # 装備品リスト
    # print(f'キャラクタ{i} hp='+str(hp), "equips="+str(equips))
    characters.append([hp, equips])

# 各キャラクターの状態管理用リスト
current_hp = [char[0] for char in characters]

# 1ターン目：タイダルウエイブ
for i in range(CHARACTER_COUNT):
    damage = wave_damages[i]
    if "珊瑚の指輪" in characters[i][1]:
        damage //= 3
    current_hp[i] -= damage
    # print(f'タイダルウエイブ{i} damage='+str(damage), "hp="+str(current_hp[i]))

# 回復フェイズ
for i in range(CHARACTER_COUNT):
    if current_hp[i] > 0:  # 生存している場合のみ回復
        current_hp[i] = min(characters[i][0], current_hp[i] + heal)
    # else:
        # print(f'初見殺しで死にました{i}')

# 2ターン目：いなづま
for i in range(CHARACTER_COUNT):
    if current_hp[i] > 0:  # 生存している場合のみダメージを受ける
        damage = thunder_damages[i]
        if "珊瑚の指輪" in characters[i][1]:
            damage *= 2
        if "ダイアの鎧" in characters[i][1]:
            damage //= 3
        current_hp[i] -= damage
        # print(f'いなづま{i} damage='+str(damage), "hp="+str(current_hp[i]))

# 生存者数をカウント
survivors = sum(1 for hp in current_hp if hp > 0)

# print(heal)
# print(current_hp)

# 結果出力
print("ラグナロク入手！" if survivors >= 3 else "全滅した......")