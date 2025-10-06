import json
from collections import defaultdict

"""
{
  "performances":[
    {
      "performance_id": 1,
      "director_id": 901,
      "actor_ids": [911, 912],
      "audience_ids": [921, 922],
      "date": "2025-05-10"
    },
    {
      "performance_id": 2,
      "director_id": 902,
      "actor_ids": [913],
      "audience_ids": [923],
      "date": "2025-05-12"
    }
  ],
  "feedback": [
    { "performance_id": 1, "user_id": 921, "score": 5 },
    { "performance_id": 1, "user_id": 922, "score": 4 },
    { "performance_id": 1, "user_id": 901, "score": 3 },
    { "performance_id": 1, "user_id": 912, "score": 5 },
    { "performance_id": 2, "user_id": 923, "score": 4 },
    { "performance_id": 2, "user_id": 902, "score": 5 }
  ]
}

- audience -> directors
- director -> actors
- actors -> director
data = json_string
"""


user_set = set()


class Data:
    performances = []
    feedback = []


class Performance:
    actor_ids = set()
    audience_ids = set()

    def __init__(self, id, director, actors, audience, date):
        self.id = id
        self.director = director
        self.actors = actors
        self.audience = audience
        self.date = date
        for actor in actors:
            self.actor_ids.add(actor)
            user_set.add(actor)
        for aud in audience:
            self.audience_ids.add(aud)
            user_set.add(aud)
        user_set.add(director)


class Feedback:
    def __init__(self, perfomance_id, user_id, score):
        self.id = perfomance_id
        self.user = user_id
        self.score = score


performances_data = []
performances_data.append(Performance(1, 901, [911, 912], [921, 922], "2025-05-10"))
performances_data.append(Performance(2, 902, [913], [923], "2025-05-10"))

feedback_data = []
feedback_data.append(Feedback(1, 921, 5))
feedback_data.append(Feedback(1, 922, 4))
feedback_data.append(Feedback(1, 901, 3))
feedback_data.append(Feedback(1, 912, 5))
feedback_data.append(Feedback(2, 923, 4))
feedback_data.append(Feedback(2, 902, 3))

# def parse_pe5formances(input_str:str) -> Performance[]:
#     return []


# make objects out of values in dictonary
# consolidate data based on which kind of user wrote the review (actor, director, audience)
# calculate averages and make dictionary output

data = Data()
data.performances = performances_data
data.feedback = feedback_data

performances = {}
feedbacks = {}
feedback_scores = defaultdict(list)  # user_ids -> list of reviews of them

for performance in data.performances:
    performances[performance.id] = Performance(
        performance.id,
        performance.director,
        performance.actors,
        performance.audience,
        performance.date,
    )
    performances[performance.id].actor_ids = performance.actors

for feedback in data.feedback:
    feedbacks[feedback.id] = Feedback(feedback.id, feedback.user, feedback.score)


for feedback in data.feedback:
    performance = performances[feedback.id]
    if feedback.user == performance.director:
        for actor in performance.actors:
            feedback_scores[actor].append(feedback.score)
    elif feedback.user in performance.actor_ids:
        feedback_scores[performance.director].append(feedback.score)
    elif feedback.user in performance.audience_ids:
        feedback_scores[performance.director].append(feedback.score)


def get_avg_score(user: int) -> float:
    scores = feedback_scores[user]
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


for user in user_set:
    print(get_avg_score(user))
