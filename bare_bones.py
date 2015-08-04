ans1 = raw_input("\nAre you planning on coming into work today?\n> ").lower()
if ans1 == "yes":
    print "Alright, see you there"
if ans1 == "no":
    ans2 = raw_input("Do you have work to do?\n> ").lower()
    if ans2 == "yes":
        ans3 = raw_input("Are you out of town?\n> ").lower()
        if ans3 == "yes":
            print "Foldit follows you wherever you go.  Get to work."
        if ans3 == "no":
            ans4 = raw_input("Are you sick?\n> ").lower()
            if ans4 == "yes":
                ans5 = raw_input("Are you dead?\n> ").lower()
                if ans5 == "yes":
                    print "Then how would you be typing this?  Nice try, see you at work."
                if ans5 == "no":
                    print "This is why we have PPE.  Get to work."
            if ans4 == "no":
                ans6 = raw_input("are you busy?\n> ").lower()
                if ans6 == "yes":
                    print "That's right, you are busy.  Busy coming into work.  See you at work"
                if ans6 == "no":
                    print "Then there's no excuse not to come into work"
    if ans2 == "no":
        ans7 = raw_input("Can you find work to do?\n> ").lower()
        if ans7 == "yes":
            ans10 = raw_input("Are you out of town?\n> ").lower()
            if ans10 == "yes":
                print "Foldit follows you wherever you go.  Get to work."
            if ans10 == "no":
                ans11 = raw_input("Are you sick?\n> ").lower()
                if ans11 == "yes":
                    ans12 = raw_input("Are you dead?\n> ").lower()
                    if ans12 == "yes":
                        print "Then how would you be typing this?  Nice try, see you at work."
                    if ans12 == "no":
                        print "This is why we have PPE.  Get to work."
                if ans11 == "no":
                    ans13 = raw_input("are you busy?\n> ").lower()
                    if ans13 == "yes":
                        print "That's right, you are busy.  Busy coming into work.  See you at work"
                    if ans13 == "no":
                        print "Then there's no excuse not to come into work"
        if ans7 == "no":
            print "Is Alex there?\n> no"
            ans8 = raw_input("Is Ryan there?\n> ").lower()
            if ans8 == "yes":
                print "Ryan will find something for you to do.  Get to work."
            if ans8 == "no":
                ans9 =  raw_input("Is the lab closed?\n> ").lower()
                if ans9 == "yes":
                    print "Foldit isn't closed.  Get to work."
                if ans9 == "no":

                    ans14 = raw_input("Are you out of town?\n> ").lower()
                    if ans14 == "yes":
                        print "Foldit follows you wherever you go.  Get to work."
                    if ans14 == "no":
                        ans15 = raw_input("Are you sick?\n> ").lower()
                        if ans15 == "yes":
                            ans16 = raw_input("Are you dead?\n> ").lower()
                            if ans16 == "yes":
                                print "Then how would you be typing this?  Nice try, see you at work."
                            if ans16 == "no":
                                print "This is why we have PPE.  Get to work."
                        if ans15 == "no":
                            ans17 = raw_input("are you busy?\n> ").lower()
                            if ans17 == "yes":
                                print "That's right, you are busy.  Busy coming into work.  See you at work"
                            if ans17 == "no":
                                print "Then there's no excuse not to come into work"
print "\n"
