player_name = input("Enter your name: ")
print("Welcome",player_name+"!")
input("Press enter to start game ")
print('''==============================
        UNKNOWN SHORE
==============================

Cold water fills your lungs.

You wake coughing on black sand.

The ocean is silent.
No wreckage.
No footprints but yours.

In the distance:
Smoke… or fog.

1) Search the Shore
2) Enter the Jungle''')
choice = input("> ")
if (choice=="1"):
    choice=input('''You walk along the water.

You find wreckage.

1) Break It Apart
2) Leave It
> ''')
    if (choice=="1"):
        choice=input('''Inside: rope and metal shard.

Smoke rises in distance.

1) Follow Smoke
2) Stay and Build Signal
> ''')
        if (choice=="1"):
            print('''You find survivors.

    They are hostile.

    ==============================
            END: CAPTURED
    ==============================''')
        else:
            print('''A ship passes.

It sees the signal.

==============================
          END: RESCUED
==============================''')
    else:
        choice==input('''Tide rises quickly.

Water surrounds you.

1) Swim
2) Climb Rocks
>''')
        if (choice=="1"):
            print('''Current pulls you under.

        ==============================
                END: DROWNED
        ============================== ''')
        else:
            print('''You survive the tide.

Night falls cold.

==============================
          END: ALIVE (FOR NOW)
==============================''')
elif (choice=="2"):
    choice=input('''Dense trees.
Strange sounds.

1) Follow Animal Tracks
2) Walk Uphill
> ''') 
    if (choice=="1"):
        choice=input('''You find fresh water.

1) Drink Immediately
2) Boil First
> ''') 
        if(choice=="1"):
            print('''Water was unsafe.

==============================
          END: SICK
==============================''')  
        else:
           print('''You recover strength.

==============================
          END: STABLE
============================== ''')  
    else:
        choice=input('''You reach a cliff.

You see smoke far away.

1) Head Toward It
2) Stay Hidden
> ''') 
        if(choice=="1"):
            print('''It’s a rescue camp.

    ==============================
            END: SAVED
    ==============================''')  
        else:
            print('''Storm hits overnight.

    ==============================
            END: LOST
    ==============================''') 
else:
    print("Invalid input! Enter 1 or 2")