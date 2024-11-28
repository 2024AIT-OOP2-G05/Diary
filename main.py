from diaries.DiarySample import DiarySample
from diaries.TakayaDiary import TakayaDiary
from diaries.HukurouDiary import HukurouDiary
from diaries.KawaiDiary import KawaiDiary

# ↓のリストには，メンバーの各日記が格納されます，
diaries = [DiarySample(),
           HukurouDiary(),
           KawaiDiary(),
           TakayaDiary()
           ]

for d in diaries:
    print("----------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()