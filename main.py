from diaries.TakayaDiary import TakayaDiary

# ↓のリストには，メンバーの各日記が格納されます，
diaries = [TakayaDiary()]

for d in diaries:
    print("----------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()