from collections import Counter

Users = [{"id": 0,"name":"Cem"},
        {"id": 1,"name":"Burak"},
        {"id": 2,"name":"Gökhan"},
        {"id": 3,"name":"Dilara"},
        {"id": 4,"name":"Salih"},
        {"id": 5,"name":"Sevinç"},
        {"id": 6,"name":"Selim"},
        {"id": 7,"name":"Tarkan"},
        {"id": 8,"name": "Fatoş"},
        {"id": 9,"name":"Gürkan"},
        {"id": 10,"name":"Ada"},
        {"id": 11,"name":"Mert"},
        {"id": 12,"name":"Pırıl"},
        {"id": 13,"name":"Pelin"},
        {"id": 14,"name":"Defne"},
        {"id": 15,"name":"Kerem"},]


friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 9), (5, 9), (5, 11), (6, 8), (7, 8), (8, 9), (10,8),(12,5),(14,8),(12,9),(11,0),(15,4),(14,3),(9,12)]

interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (10, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (10, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (11, "scikit-learn"), (12, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (11, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (13, "decision trees"),
(4, "libsvm"), (13, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (14, "statistics"),
(6, "probability"), (14, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(15, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (15, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def Most_Friends():
    liste = []
    for a,b in friendships:
        liste.append(a)
        liste.append(b)
    friend_counts =(Counter(liste))
    sorted(friend_counts,reverse=True)


def FriendSuggester(i):
    friends = []
    interest = []
    FriendsToSuggest = []
    for a in range(0,len(friendships)):
        if friendships[a][0] == i:
            friends.append(friendships[a][1])
        elif friendships[a][1] == i:
            friends.append(friendships[a][0])
    for a in range(0,len(interests)):
        if interests[a][0] == i:
            interest.append(interests[a][1])

    for a in range(0,len(friends)):

        Pass = True
        x = 0
        for b in range(0, len(friendships)):
            if friendships[b][0] == friends[a] and friendships[b][1] != i:
                for c in range(0,len(FriendsToSuggest)):
                    if FriendsToSuggest[c][1] == friendships[b][1]:
                        Pass = False
                        FriendsToSuggest[c][1] += 2
                if Pass:
                    x += 2
                    FriendsToSuggest.append([friendships[b][1], x])

            elif friendships[b][1] == friends[a] and friendships[b][0] != i:
                for c in range(0,len(FriendsToSuggest)):
                    if FriendsToSuggest[c][0] == friendships[b][0]:
                        Pass = False
                        FriendsToSuggest[c][1] += 2
                if(Pass == True):
                    x += 2
                    FriendsToSuggest.append([friendships[b][0], x])
    NewList = []
    for a in range(0,len(FriendsToSuggest)):

        Pass = True
        for b in range(0,len(friends)):
            if friends[b] == FriendsToSuggest[a][0]:
                Pass = False
        if Pass:
            NewList.append(FriendsToSuggest[a])
    FriendsToSuggest = NewList
    for a in range(0,len(FriendsToSuggest)):
        for b in range(0,len(interests)):
            if interests[b][0] == FriendsToSuggest[a][0]:
                for c in range(0,len(interest)):
                    if interest[c] == interests[b][1]:
                        FriendsToSuggest[a][1] += 1
    BestSugestion = ""
    SecondSugestion = ""
    ThirdSugestion = ""
    f = 0
    s = 0
    t = 0
    print(FriendsToSuggest)
    for a in range(0,len(FriendsToSuggest)):

        if FriendsToSuggest[a][1] > f:
            for b in range(0,len(Users)):
                if Users[b]["id"] == FriendsToSuggest[a][0]:
                    ThirdSugestion = SecondSugestion
                    SecondSugestion = BestSugestion
                    t = s
                    s = f
                    BestSugestion = Users[b]["name"]

                    f = FriendsToSuggest[a][1]
        elif FriendsToSuggest[a][1] == f and FriendsToSuggest[a][1] > s:
            for b in range(0,len(Users)):
                if Users[b]["id"] == FriendsToSuggest[a][0]:
                    ThirdSugestion = SecondSugestion
                    t = s
                    SecondSugestion = Users[b]["name"]
                    s = FriendsToSuggest[a][1]
        elif FriendsToSuggest[a][1] == f and FriendsToSuggest[a][1] == s:
            for b in range(0,len(Users)):
                if Users[b]["id"] == FriendsToSuggest[a][0]:
                    ThirdSugestion = Users[b]["name"]
                    t = FriendsToSuggest[a][1]
        elif FriendsToSuggest[a][1] > s:
            for b in range(0,len(Users)):
                if Users[b]["id"] == FriendsToSuggest[a][0]:
                    ThirdSugestion = SecondSugestion
                    t = s
                    SecondSugestion = Users[b]["name"]
                    s = FriendsToSuggest[a][1]
        elif FriendsToSuggest[a][1] > t:
            for b in range(0,len(Users)):
                if Users[b]["id"] == FriendsToSuggest[a][0]:
                    ThirdSugestion = Users[b]["name"]
                    t = FriendsToSuggest[a][1]


    print("\n","1- ",BestSugestion,"\n","2- ",SecondSugestion,"\n","3- ",ThirdSugestion)



FriendSuggester(15)