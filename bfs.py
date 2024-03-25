from collections import deque

graph = {}

graph["you"] = ["alice", "bob", "claire"]

graph["bob"] = ["anuj", "claire"]

graph["alice"] = ["peggy"]

graph["claire"] = ["thom", "jonny"]

graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []
graph["peggy"] = []

268586


def person_is_seller(name):
    return name[-1] == "m"

def bfs(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            searched += person
            if person_is_seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
    return False

print(bfs("claire"))