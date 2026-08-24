import random

all_achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor',
                    'Master Explorer', 'Treasure Hunter', 'Unstoppable',
                    'First Steps', 'Collector Supreme',
                    'Untouchable', 'Sharp Mind', 'Boss Slayer']


def gen_player_achievements(all_a: list, player: str) -> set:
    a_num = random.randint(0, 12)
    a_list = random.sample(all_a, a_num)
    #   print(a_num)
    achievement_set = set(a_list)
    print(f"Player: {player}", achievement_set)
    return (achievement_set)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    #   each player
    p1 = gen_player_achievements(all_achievements, "Alice")
    p2 = gen_player_achievements(all_achievements, "Dingdong")
    p3 = gen_player_achievements(all_achievements, "Shrek")
    p4 = gen_player_achievements(all_achievements, "siusiakplacek\n")
    #   distinct
    a_all_p = p1.union(p2, p3, p4)
    print(f"All distinct achievements: {a_all_p}")
    #   common
    a_common = p1.intersection(p2, p3, p4)
    print(f"Common achievements: {a_common}\n")
    print(f"Only Alice has: {p1.difference(p2, p3, p4)}")
    print(f"Only Dingdong has: {p2.difference(p1, p3, p4)}")
    print(f"Only Shrek has: {p3.difference(p1, p2, p4)}")
    print(f"Only siusiakplacek has: {p4.difference(p1, p2, p3)}\n")

    #   missing
    all_achievements_set = set(all_achievements)
    print(f"Alice is missing: {all_achievements_set.difference(p1)}")
    print(f"Dingdong is missing: {all_achievements_set.difference(p2)}")
    print(f"Shrek is missing: {all_achievements_set.difference(p3)}")
    print(f"siusiakplacek is missing: {all_achievements_set.difference(p4)}")
