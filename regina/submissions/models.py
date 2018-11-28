from django.db import models
from django.contrib.auth.models import User

def all_questions(request):
    questions = Question.objects.annotate(number_of_answers=models.Count('answer'))

class Submission(models.Model):
    visible_title = models.TextField(blank=False)
    content = models.TextField(blank=False)
    perp_name = models.TextField(blank=False)
    place = models.TextField(blank=False)
    # should be changed to 'author' if we have time to refactor
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    matches = models.IntegerField(default=0)
    matches_users = models.ManyToManyField(User, related_name='matches_users')
    def add_match(self):
        self.matches += 1
    def match(self):
        name_matches = Submission.objects.filter(perp_name=self.perp_name)
        matches = name_matches.filter(place=self.place)
        if matches:
            return matches
        else:
            return None
    def update_matches(self):
        my_matches = self.match()
        self.matches = 0
        # self.matches_users = []
        for submission in my_matches:
            self.matches_users.add(submission.user)
            self.matches += 1

    def __str__(self):
        return self.visible_title


'''
# if __name__ == '__main__':
from submissions import models
s = models.Submission()
s.visible_title = "Murph"
s.content = "My dog won't stop barking and it pisses me off."
s.perp_name = "Scruffles"
s.place = "555 Post Street"
s.save()
print(s.matches)
r = models.Submission()
r.visible_title = "Surph"
r.content = "My dog won't stop barking and it pisses me off."
r.perp_name = "Scruffles"
r.place = "555 Post Street"
r.save()
print(s.matches)
print("Now for the soup du jour")
s.update_matches()
print(s.matches)
'''