done = ["insult", "ignored", "apologised", "praised"] # Creates a list for the variable 'done'

for i in done:
    print(i, " --")

what_was_done = input (f"What did they do? Type either insult, ignored, apologised, praised")
liked_post = input (f"Did they like your latest post? Type either yes or no.")
real_friend = input (f"Are they your real life friend? Type either yes or no.")

if liked_post == "yes":
    post = True
elif liked_post == "no":
    post = False
else:
    liked_post = input (f"Invalid choice. Did they like your latest post? Type either yes or no.")

if real_friend == "yes":
    friend = True
elif real_friend == "no":
    friend = False
else:
    real_friend = input (f"Invalid choice. Are they your real life friend? Type either yes or no.")

print ("Cool. :)")

if done in what_was_done and what_was_done == done [0]:
    if liked_post == True and real_friend == True:
        print ("I'm sorry to hear that. Being insulted, especially by someone who's friends with you is wrong. It's weird they liked it, though.")
    elif liked_post == True and real_friend == False:
        print ("I'm sorry to hear that. It's weird they liked it, but at least it's not someone you know.")
    elif liked_post == False and real_friend == True:
        print ("I'm sorry to hear that. Being insulted, especially by someone who's friends with you is wrong. And not liking the post...perhaps you should chat to them.")
    elif liked_post == False and real_friend == False:
        print ("I'm sorry to hear that. Being insulted and disliked is not cool, but sadly that's normal with random people on the internet.")

elif done in what_was_done and what_was_done == done [1]:
    if liked_post == True and real_friend == True:
        print ("They ignored you? But they liked your post? AND THEY WERE YOUR FRIEND!? I don't know what to make of this.")
    elif liked_post == True and real_friend == False:
        print ("They ignored you but liked the post? It's strange that they liked it, but strangers can do weird things.")
    elif liked_post == False and real_friend == True:
        print ("A friend ignored you? WHAT!? They shouldn't be just ignoring you like that!")
    elif liked_post == False and real_friend == False:
        print ("Sorry to break it to you, but this is normal in influncing. If you need more help, talk to me.")

elif done in what_was_done and what_was_done == done [2]:
    if liked_post == True and real_friend == True:
        print ("That's sweet. No matter what they did, it's good that they apologised and liked it.")
    elif liked_post == True and real_friend == False:
        print ("Wait a second. WHAT??? Why was a stranger apologising? What did they do? Well, it must be for good reasons.")
    elif liked_post == False and real_friend == True:
        print ("Even if they didn't like your post, it's good that they apologised. I won't ask what for, but I'm sure it makes sense.")
    elif liked_post == False and real_friend == False:
        print ("What did a stranger do to you? If you need to talk about it, ask me. But apologising always helps.")

elif done in what_was_done and what_was_done == done [3]:
    if liked_post == True and real_friend == True:
        print ("That's what friends are for, aren't they? It's nice that you have such great people supporting you.")
    elif liked_post == True and real_friend == False:
        print ("It's always great to get praise from people outside your friends, and a like is even better!")
    elif liked_post == False and real_friend == True:
        print ("That's what friends are for, aren't they? Even though they didn't like, it's nice to see the support you have.")
    elif liked_post == False and real_friend == False:
        print ("It's always great to get praise from people outside your friends, even if they don't like it!")

print ("You good now?")