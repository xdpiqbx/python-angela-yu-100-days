import random
from day_BlackJack_art import logo


def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def add_ace_to_hand(total):
    if total + 11 > 21:
        return 1
    else:
        return 11


def add_card_to_hand(cards, card):
    cards.append(card)
    if sum(cards) > 21:
        for i in range(0, len(cards) - 1):
            if cards[i] == 11:
                cards[i] = 1
                break


def check_for_aa(cards):
    if sum(cards) == 22:
        for i in range(0, len(cards) - 1):
            if cards[i] == 11:
                cards[i] = 1
                break


def plus_one_more_card(cards):
    card = get_card()
    if card == 11:
        cards.append(add_ace_to_hand(sum(cards)))
    else:
        add_card_to_hand(cards, card)


def final_stats_prompt(player_cards, ai_cards):
    print("")
    print(f"Your final hand: {player_cards}, sum is: {sum(player_cards)}")
    print(f"Computer's final hand: {ai_cards}, sum is: {sum(ai_cards)}")
    print("")


def game_result_prompt(player_result, ai_result):
    if ((player_result <= 21) and (player_result > ai_result)) or ((ai_result > 21) and (player_result <= 21)):
        print("You win !")
    elif player_result == ai_result:
        print("Draw =)")
    else:
        print("You lose")
    print("")


def black_jack(player_cards, ai_cards):
    print(logo)
    print(f"Computer first card: [{ai_cards[0]}]")
    check_for_aa(player_cards)
    more = True
    while more:
        print(f"Your cards: {player_cards}, sum is - {sum(player_cards)}")
        if sum(player_cards) < 21:
            if input("'Y' to get 1 more card or 'N' to pass: ") == 'Y':
                plus_one_more_card(player_cards)
            else:
                more = False
        else:
            more = False

    ai_cards.append(get_card())

    more = True
    if sum(player_cards) >= 21:
        more = False

    while more:
        check_for_aa(ai_cards)
        print(f"Computer cards: {ai_cards}")
        if sum(ai_cards) < 17:
            plus_one_more_card(ai_cards)
        else:
            more = False

    final_stats_prompt(player_cards, ai_cards)
    game_result_prompt(sum(player_cards), sum(ai_cards))


while input("Do you want to play Black Jack ? ( 'Y' / 'N' ) ") == 'Y':
    black_jack([get_card(), get_card()], [get_card()])
