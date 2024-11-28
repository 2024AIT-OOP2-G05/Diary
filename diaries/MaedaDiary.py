from diaries.AbstractDiary import AbstractDiary
class MaedaDiary(AbstractDiary):
    def get_date(self):
        return "2024-11-28"
    
    def get_summary(self):
        return """とても眠たい。"""

    def get_author(self):
        return "Maeda"