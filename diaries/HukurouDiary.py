from diaries.AbstractDiary import AbstractDiary

class HukurouDiary(AbstractDiary):
    
    def get_date(self):
        return "2021-11-28"
    
    def get_summary(self):
        return "Twitterで猫ちゃんをたくさん見た．とっても可愛かった"
    
    def get_author(self):
        return "Murase"