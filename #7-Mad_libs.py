story = '''One <adjective> morning, <name> the <animal> walked into the <place> carrying a <object>. Suddenly, a <color> <animal2> jumped out and began to <verb> loudly. Startled, <name> grabbed a <silly_object> and <verb_past> across the <place>, knocking over chairs and a table. A nearby <profession> laughed while the <plural_noun> rolled everywhere. Soon the whole <place> was cheering and laughing. In the end, everyone said it was the most <adjective2> adventure ever.'''

words = set()
target_start = "<"
target_end = ">"
start_of_word = -1

for i , char in enumerate(story):
    if char==target_start:
        start_of_word=i
    
    if char==target_end and start_of_word!=-1:
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word=-1



for word in words:
    answer=input("Enter word for "+word+": ")
    story = story.replace(word,answer)

print()
print(story,end="\n")


