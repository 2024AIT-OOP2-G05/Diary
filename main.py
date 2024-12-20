from diaries.HukurouDiary import HukurouDiary
from diaries.KawaiDiary import KawaiDiary
from diaries.SakuraiDiary import SakuraiDiary
from diaries.TakayaDiary import TakayaDiary
from diaries.MaedaDiary import MaedaDiary
from diaries.HiromiDiary import HiromiDiary

# ↓のリストには，メンバーの各日記が格納されます，
diaries = [HukurouDiary(),
           KawaiDiary(),
           SakuraiDiary(),
           TakayaDiary(),
           MaedaDiary(),
           HiromiDiary ()]

for d in diaries:
    print("----------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()