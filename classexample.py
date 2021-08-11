'''class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def chechkAnswer(self,answer):
        return self.answer == answer

q1 = Question('En iyi programlama dili hangisidir ?', ['C#','Python','Javascript','Java'], 'Python')
q2 = Question('En popüler dili hangisidir ?', ['C#','Python','Javascript','Java'], 'Python')
q3 = Question('En çok kazandıran  dili hangisidir ?', ['C#','Python','Javascript','Java'], 'Python')


print(q1.chechkAnswer('Python'))'''





'''class Quiz:
    def  __init__(self,Questions):
        self.Questions = Questions
        self.score = 0
        self.questionsIndex = 0
    
    
    def getQuestion(self):
        return question == quiz.questions[quiz.questionsIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionsIndex + 1}: {question.text}')
q1 = Question('En iyi programlama dili hangisidir ?', ['C#','Python','Javascript','Java'], 'Python')
q2 = Question('En popüler dili hangisidir ?', ['C#','Python','Javascript','Java'], 'Python')
q3 = Question('En çok kazandıran  dili hangisidir ?', ['C#','Python','Javascript','Java'], 'Python')
question = [q1,q2]


quiz = Quiz(questions)
question = quiz.getQuestion()'''


class Şirket():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True

        def program(self):
            pass
        
        def menuSecim(self):
            secim = int(input('*** {} Otomasyonuna hoş geldiniz *** \n\n1-Çalışan Ekle\n2-Çalışan Çıkar\n3-Verilecek Maaş Göster\n4-Maaşları ver\5-Masraf Gir\n6-Gelir Gir\nSeçiminizi giriniz:'))
            while secim < 1 and secim > 6:
                secim = int(input('Lütfen 1 - 6  arasında belirtilen seçeneklerden birini giriniz'))
            return secim
        def calisanEkle(self):
            pass
        def calisanCikar(self):
            pass
        def verilecekMaasGoster(self,hesap = 'a'):
             '''hesap: a ise aylik, y ise yıllık hesap'''
            
        
        def maaslariVer(self):
            pass
        def masrafGir(self):
            pass
        def gelirGir(self):
            pass


