# Update this text to match your story.
start = '''
After a long day at the castle Princess Edith of
Cambridge decides to go up to bed to get her beauty sleep. When suddenly she
hears a sound that disrupts her plans, a magical sound of sparkles. She
heads downstairs to invesetigate the stange noises.
'''
i = 0
while True:
    i += 1
    print(start)

     # Update to match your story.
    user_input = input("Type left to go left or right to go right.")
    if not user_input == "left" or user_input == "right":
        print("Choose Again.")
    #else:
    #    user_input = input("left or right")

    if user_input == "right":
        print("Princess Edith choose to go right and head back to her room to not investigate but sleep.")
        break
    elif user_input == "left":
            print("Princess Edith decide to go left and head outside the castle to continue and investigae.
            print(After Princess Edith decides to contine her adventure she runs into a goblin with green skin and raggedy clothes who tries to rob her."
            " Type 'punch' to punch the goblin")


    #else:
        #user_input == "punch"
        #print("Other goblins appear out of the woods.")
        #break
