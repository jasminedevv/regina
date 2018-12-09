from django.db import models
from django.contrib.auth.models import User


class Submission(models.Model):
    visible_title = models.TextField(blank=False)
    content = models.TextField(blank=False)
    perp_name = models.TextField(blank=False)
    place = models.TextField(blank=False)
    # TODO should be changed to 'author' if we have time to refactor
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    matches = models.IntegerField(default=0)
    matches_users = models.ManyToManyField(User, related_name='matches_users')
    def add_match(self):
        self.matches += 1

    def match(self):
        '''
            Returns all submissions that match the current submission.
        '''
        name_matches = Submission.objects.filter(perp_name=self.perp_name)
        matching_submissions = name_matches.filter(place=self.place)
        print(type(matching_submissions))
        # TODO: make sure this works when u have wifi
        return list(matching_submissions)

    def add_matches_user(self, user):
        self.matches_users.add(user)
        self.matches = len(self.matches_users.all()) - 1
        self.save()

    def initialize_matches(self):
        '''
            Updates itself and matching submissions with related users.
        '''
        # TODO notify added users
        my_matches = self.match()
        self.matches = 0
        print(my_matches)
        # adds users in matching submissions to itself
        for submission in my_matches:
            self.add_matches_user(submission.user)
            submission.add_matches_user(self.user)
            # TODO: why isn't this working??
            print(isinstance(submission, Submission))
        # quick fix for submissions matching with themselves
        self.matches = len(self.matches_users.all()) -1
        self.save()

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


'''
call them incidents
situation
think about descriptions/brief description
'''