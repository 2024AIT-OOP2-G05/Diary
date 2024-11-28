from diaries.AbstractDiary import AbstractDiary

class KawaiDiary(AbstractDiary):
    
    def get_date(self):
        return "2024-11-28"
    
    def get_summary(self):
        return "1限と2限の教室の温度差で風邪をひきそうだった。x"
    
    def get_author(self):
        return "kawai"