player_cards = [list(input()) for _ in range(3)]


def play_card(player_cards):
    return player_cards.pop(0) if player_cards else None


player_names = ["A", "B", "C"]
current_player_index = 0

while True:
    # 現在のプレイヤーのカードを出す
    card = play_card(player_cards[current_player_index])
    if card is None:  # 手札がなくなったらループを抜ける
        break

    # 次のプレイヤー
    current_player_index = {"a": 0, "b": 1, "c": 2}[card]

print(player_names[current_player_index])
