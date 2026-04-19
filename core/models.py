from django.db import models

from django.db import models


class Session(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session {self.id}"


class Answer(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    step = models.CharField(max_length=1)  # S, C, O, R, E
    question = models.TextField()
    answer = models.TextField()

    # для 5 WHY
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.step}: {self.answer[:30]}"
