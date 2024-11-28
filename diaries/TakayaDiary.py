from diaries.AbstractDiary import AbstractDiary


class TakayaDiary(AbstractDiary):
    
    def get_date(self):
        return "2024-11-28"
    
    def get_summary(self):
        return "今日はgithubの使い方を学んだ。"
    
    def get_author(self):
        return "KajitaTakaya"