from collections import Counter
from dataclasses import dataclass
from pprint import pprint


def test_main():
    """
    To play Camel Cards, you are given a list of hands and their corresponding
    bid (your puzzle input). For example:

    32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483

    This example shows five hands; each hand is followed by its bid amount.
    Each hand wins an amount equal to its bid multiplied by its rank, where
    the weakest hand gets rank 1, the second-weakest hand gets rank 2, and
    so on up to the strongest hand.

    Because there are five hands in this example, the strongest hand will have
    rank 5 and its bid will be multiplied by 5.

    So, the first step is to put the hands in order of strength:

    32T3K is the only one pair and the other hands are all a stronger type,
    so it gets rank 1.

    KK677 and KTJJT are both two pair. Their first cards both have the same
    label, but the second card of KK677 is stronger (K vs T), so KTJJT gets
    rank 2 and KK677 gets rank 3.

    T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card,
    so it gets rank 5 and T55J5 gets rank 4.

    Now, you can determine the total winnings of this set of hands by adding
    up the result of multiplying each hand's bid with its rank (
        765 * 1 +
        220 * 2 +
        28 * 3 +
        684 * 4 +
        483 * 5).
    So the total winnings in this example are 6440.

    Find the rank of every hand in your set. What are the total winnings?

    Order of cards is A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2

    """
    data = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483",
    ]
    assert main(data) == 6440


def test_main2():
    """
    --- Part Two ---
    To make things a little more interesting, the Elf introduces one additional
    rule. Now, J cards are jokers - wildcards that can act like whatever card
    would make the hand the strongest type possible.

    To balance this, J cards are now the weakest individual cards, weaker even
    than 2. The other cards stay in the same order:

        A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

    J cards can pretend to be whatever card is best for the purpose of
    determining hand type; for example, QJJQ2 is now considered four of a
    kind. However, for the purpose of breaking ties between two hands of the
    same type, J is always treated as J, not the card it's pretending to be:

    JKKK2 is weaker than

    QQQQ2 because J is weaker than Q.

    Now, the above example goes very differently:

    32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483

    32T3K is still the only one pair; it doesn't contain any jokers, so its
    strength doesn't increase. KK677 is now the only two pair, making it the
    second-weakest hand.

    T55J5, KTJJT, and QQQJA are now all four of a kind!

    T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.

    With the new joker rule, the total winnings in this example are 5905.

    """
    data = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483",
    ]
    assert main2(data) == 5905


def test_qualify_set2():
    """..."""
    assert qualify_set2("JTJ63") == 3
    assert qualify_set2("QQQJA") == 4
    assert qualify_set2("T55J5") == 4
    assert qualify_set2("KTJJT") == 4
    assert qualify_set2("AAAJJ") == 32
    # T55J5, KTJJT, and QQQJA are now all four of a kind!
    # T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.

    all_cards_of_rank = []
    for cards, rank in zip(["QQQJA", "T55J5", "KTJJT", "AAAJJ"], [4, 4, 4, 32]):
        assert qualify_set2(cards) == rank
        all_cards_of_rank.append(
            PimpedCardSet(
                original=cards,
                original_values=[INDIVIDUAL_CARDS_VALUES_MAP[c] for c in cards],
                rank=4,
                rank_total=0,
                bid=123,
            )
        )

    result_rank = 1
    result = []
    for cardset in sorted(all_cards_of_rank, key=lambda c: c.original_values):
        cardset.rank_total = result_rank
        result_rank += 1
        result.append(cardset)

    assert result == [
        PimpedCardSet(
            original="T55J5",
            original_values=[10, 5, 5, 1, 5],
            rank=4,
            rank_total=1,
            bid=123,
        ),
        PimpedCardSet(
            original="QQQJA",
            original_values=[12, 12, 12, 1, 14],
            rank=4,
            rank_total=2,
            bid=123,
        ),
        PimpedCardSet(
            original="KTJJT",
            original_values=[13, 10, 1, 1, 10],
            rank=4,
            rank_total=3,
            bid=123,
        ),
        PimpedCardSet(
            original="AAAJJ",
            original_values=[14, 14, 14, 1, 1],
            rank=4,
            rank_total=4,
            bid=123,
        ),
    ]


@dataclass
class CardSet:
    original: list
    original_values: list
    rank: int
    rank_total: int
    bid: int


@dataclass
class PimpedCardSet:
    original: list
    original_values: list
    rank: int
    rank_total: int
    bid: int


CARDS_VALUES_MAP = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 10,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

INDIVIDUAL_CARDS_VALUES_MAP = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def qualify_set(cards: str) -> CardSet:
    """Return 'rank' of set according to its cards:

    5 : Five of a kind, where all five cards have the same label: AAAAA
    4 : Four of a kind, where four cards have the same label and one card
        has a different label: AA8AA
    32 : Full house, where three cards have the same label, and the remaining
        two cards share a different label: 23332
    3 : Three of a kind, where three cards have the same label, and the
        remaining two cards are each different from any other card in the
        hand: TTT98
    22 : Two pair, where two cards share one label, two other cards share a
        second label, and the remaining card has a third label: 23432
    2 : One pair, where two cards share one label, and the other three cards
        have a different label from the pair and each other: A23A4
    1 : High card, where all cards' labels are distinct: 23456

    """
    cards_counter = Counter(cards)
    rank = max(cards_counter.values())
    if rank in [1, 4, 5]:
        return rank

    if rank == 3:
        if len(cards_counter.values()) == 2:
            return 32
        return 3

    if rank == 2:
        if len(cards_counter.values()) == 3:
            return 22
        return 2


def qualify_set2(cards: str) -> CardSet:
    """Return 'rank' of set according to its cards:

    5 : Five of a kind, where all five cards have the same label: AAAAA
    4 : Four of a kind, where four cards have the same label and one card
        has a different label: AA8AA
    32 : Full house, where three cards have the same label, and the remaining
        two cards share a different label: 23332
    3 : Three of a kind, where three cards have the same label, and the
        remaining two cards are each different from any other card in the
        hand: TTT98
    22 : Two pair, where two cards share one label, two other cards share a
        second label, and the remaining card has a third label: 23432
    2 : One pair, where two cards share one label, and the other three cards
        have a different label from the pair and each other: A23A4
    1 : High card, where all cards' labels are distinct: 23456

    """
    cards_counter = Counter(cards)
    rank = max(cards_counter.values())

    if "J" in cards_counter:
        max_key = max(cards_counter, key=cards_counter.get)
        if max_key == "J":
            cards_without_j = [c for c in cards if c != "J"]
            for card in ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]:
                if card in cards_without_j:
                    max_key = card
                    break

        if cards_counter[max_key] == 3 and cards_counter["J"] == 2:
            # special special case - fucking full house
            print(
                """
                >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FULL HOUSE
            """
            )
            return 32

        rank = cards_counter[max_key] + cards_counter["J"]
        print(
            f"""
            cards: {cards} highest: {max_key} ['J']: {cards_counter['J']} rank: {rank}
        """
        )

    if rank in [1, 4, 5]:
        return rank

    if rank == 3:
        if len(cards_counter.values()) == 2:
            return 32
        return 3

    if rank == 2:
        if len(cards_counter.values()) == 3:
            return 22
        return 2


def main(data) -> int:
    all_cards = {}
    for entry in data:
        cards, bid = entry.split()
        rank = qualify_set(cards)
        if rank not in all_cards:
            all_cards[rank] = []
        all_cards[rank].append(
            CardSet(
                original=cards,
                original_values=[CARDS_VALUES_MAP[c] for c in cards],
                rank=rank,
                rank_total=0,
                bid=bid,
            )
        )
    pprint(all_cards)

    # The global rank which will be used to calculate the result
    result_rank = 1
    # List of all the resulting entries
    result = []
    for rank in [1, 2, 22, 3, 32, 4, 5]:
        try:
            all_cards_of_rank = all_cards[rank]
        except KeyError:
            print(f"Print no cardset found with rank {rank}")
            continue
        for cardset in sorted(all_cards_of_rank, key=lambda c: c.original_values):
            cardset.rank_total = result_rank
            result_rank += 1
            result.append(cardset)

    pprint(all_cards)
    final_result = 0
    for cardset in result:
        final_result += int(cardset.rank_total) * int(cardset.bid)

    print(f"sol1: {final_result}")
    return final_result


def main2(data) -> int:
    all_cards = {}
    for entry in data:
        cards, bid = entry.split()
        rank = qualify_set2(cards)
        if rank not in all_cards:
            all_cards[rank] = []
        all_cards[rank].append(
            PimpedCardSet(
                original=cards,
                original_values=[INDIVIDUAL_CARDS_VALUES_MAP[c] for c in cards],
                rank=rank,
                rank_total=0,
                bid=bid,
            )
        )
    # pprint(all_cards)

    # The global rank which will be used to calculate the result
    result_rank = 1
    # List of all the resulting entries
    result = []
    for rank in [1, 2, 22, 3, 32, 4, 5]:
        try:
            all_cards_of_rank = all_cards[rank]
        except KeyError:
            print(f"Print no cardset found with rank {rank}")
            continue
        for cardset in sorted(all_cards_of_rank, key=lambda c: c.original_values):
            cardset.rank_total = result_rank
            result_rank += 1
            result.append(cardset)

    # pprint(all_cards)
    final_result = 0
    for cardset in result:
        final_result += int(cardset.rank_total) * int(cardset.bid)

    print(f"sol2: {final_result}")
    return final_result


if __name__ == "__main__":
    data = None
    with open("./07/input.txt", "r") as input:
        data = input.read().splitlines()

    # sol1
    # main(data)

    # sol2
    main2(data)
