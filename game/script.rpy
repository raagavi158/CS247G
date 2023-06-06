define mc = Character("Me")

# Define the love level variable
default love = 0

# Define the total date counter variable
default date_counter = 0
default puzzle_solved = 0
default clue1 = 0
default clue2 = 0
default clue3 = 0
default clue4 = 0
default password = ""

# Define the character to be dated

define startup_girl = Character("Britneigh", color="#c8ffc8", image="startup_girl")
define cs_guy = Character("Brian", color="#c8ffc8", image="cs_guy")
define frat_bro = Character("Brett", color="#c8ffc8", image="frat_bro")
define police_officer = Character("Police", color="#c8ffc8", image="police_officer")
define anonymous_guy = Character("Killer", color="#c8ffc8", image="anonymous_guy")

image startup_girl = "startup_girl.svg"
image foho = "foho.png"
image fizz = "fizz.png"
image cs_guy = "cs_guy.png"
image frat_bro = "frat_bro.svg"
image hinge = 'hinge_profile.jpg'
image hinge1 = 'hinge_profile_1.jpg'
image hinge2 = 'hinge_profile_2.jpg'
image police_officer = 'police_officer.png'
image anonymous_guy = 'Asset 7.svg'

image cl1 = "Asset 12.png"
image cl2 = "Asset 13.png"
image cl3 = "Asset 11.png"
image cl4 = "Asset 10.png"


image card = "card.jpeg"

# Define the starting label
label start:

    scene bg oval: 
        zoom 1.75
        truecenter

    # Display the introduction
    "It was a bright morning at Stanford University when I saw this on my phone..."

    # Display the date choice

    show fizz:
        xalign 0.05 yalign 0.2
        zoom 0.8
    show foho: 
        xalign 0.85 yalign 0.2
        zoom 0.65

    "Eventually, after not hearing from my roomate, I realized that these Fizz and FoHo posts are about Jim!"

    scene bg dorm:
        zoom 1.7
    
    "Jim was my freshman year roommate and we’ve lived together every year since. I can’t believe he’s gone, I warned him to not go on dates with weirdos on this campus."
    "There’s no way there was no evidence. The killer showed no remorse, their dating profile is probably still active. I have to find the murderer, guess it’s time to get on Tinge."
    jump middle

label middle:
    if clue1 >= 1 and clue2 >= 1 and clue3 >= 1 and puzzle_solved==0:
        jump puzzle

    scene bg oval: 
        zoom 1.75
    
    show hinge:
        zoom 1.3
        xalign 0.3 yalign 0.2
    show hinge1:
        zoom 1.3
        xalign 0.5 yalign 0.2
    show hinge2:
        zoom 1.3
        xalign 0.7 yalign 0.2
    
    "Repeat a date or click a new one!"

    menu:
        "Who are you swiping on?"
        "Stanford Start-up Girl (Britneigh)":
            jump start_up_date
        "Nerdy CS Guy (Brian)":
            jump CS_guy_date
        "Frat Bro (Brett)":
            jump frat_bro_date
        "Call the police":
            jump police_segment
    
label puzzle:
    scene bg black: 
        zoom 10
    show cl1:
        zoom 1.5
        xalign 0.05 yalign 0.2
    show cl2:
        zoom 1.5
        xalign 0.85 yalign 0.2
    show cl3:
        zoom 1.5
        xalign 0.45 yalign 0.85
    mc "Alright, now I know these clues must all be related somehow. But what do all of these clues mean?"
    $ password = renpy.input("What is the secret message?", length=35)
    $ password = password.lower()
    while password != "ask_brett/what_he_found" and password != "ask brett what he found at lake lag":
        $ password = renpy.input("That's not right. Guess again?", length=35)
        $ password = password.lower()
    $ puzzle_solved = 1
    if puzzle_solved and clue4 == 0:
        "{i}Hmm it might be time to revisit Brett"
        jump frat_bro_date
    else:
        jump middle

# Define the date label
label frat_bro_date:
    scene bg frat: 
        zoom 0.75

    # Increment the love level
    $ love += 1
    $ date_counter += 1
    show frat_bro:
        zoom 1
        truecenter
    if puzzle_solved == 1: 
        jump brett_menu
    # Display the date dialogue
    mc "Hey Brett! Damn I’ve never been in the house before. Thanks for letting me in!"
    show frat_bro weird
    frat_bro "Absolutely my guy. Anything for a good time ;)"
    mc "Uh… yeah absolutely? Anyways…"

    # Display the food choice
    menu brett_menu:
        "{i}Be upfront and interrogate Brett directly about Jim’s murder.{/i}":
            mc "My roommate Jim was the guy that died last weekend and I’ve been trying to find out anything related to the murder."
            show frat_bro sad
            frat_bro "Daaamn that’s insane. Did they get transported or something? That would have been a sick story to tell ah ha ha. Anyways, do you wanna watch anything?"
            menu frat_guy_location:
                "{i}Ask him where he was that night{/i}}":
                    mc "Where were you on that night?"
                    show frat_bro
                    frat_bro "Well I won’t lie, I was hanging out with him at lake lag that night."
                    frat_bro "But I found out that he wasn’t FTB — FOR THE BOYS — that night, and I didn’t really care for him after that. So I left him there when I found out he doesn’t vibe with the boys. I don’t know what happened after that."
                    menu talk_about: 
                        "{i}Ask about what they talked about.{/i}":
                            label talk_about_subpart:
                                mc "Did y’all talk about anything else?"
                                frat_bro "I guess we did talk about this thing that a few of my other friends, Britneigh and Brian, were building, AlibiAI." 
                                frat_bro "We were laughing about it because it was an idea that seemed so dumb, so I encouraged Brian to go through with building it as a prank, and I even managed to get him to pitch the idea to Britneigh."
                                frat_bro "LOL! It was kind of strange though — Britneigh seemed a little wayyy too excited for the idea for some reason ahaha."
                                "{i}Brett and Britneigh were also Jim's romantic interests that you thought of as possible suspects.{/i}"
                                frat_bro "But anyways, I wanted to ask you…are you FTB? As in… FOR THE BOYS????"
                                menu:
                                    "{i}Say no and express your suspicion towards him.{/i}":
                                        label suspicion_frat:
                                            mc "Absolutely not. I have reason to believe you might have murdered Jim."
                                            show frat_bro angry
                                            frat_bro "Whoa whoa whoa! That’s a really strong accusation! I told you I left him there at lake lag, and I don’t know what happened to him after that if he was murdered then. How dare you accuse me! I think you should leave."
                                            jump middle
                                    "{i}Enthusiastically say yes.{/i}":
                                        mc "Hell yeah, brother!"
                                        show frat_bro weird
                                        frat_bro "HELL YEAH BROTHER!! Alright man, listen…I can tell you’re a good guy. You’d make a good BROTHER. And I want to tell you the secret fraternity Latin phrase to seal the deal with your future acceptance into the fraternity."
                                        frat_bro "Here, it’s written on this piece of paper in this envelope. Take it with you, and open it once you are in private."
                                        show cl3: 
                                            zoom 1.5
                                            truecenter
                                        $ clue3 += 1
                                        mc "Thanks!"
                        "{i}Ask him to prove that Brett left Jim there before he died.{/i}":
                            mc "Can you prove that you left him before he died and that you didn’t murder him?"
                            frat_bro "Nah I can’t prove it man, but you can choose to believe me! I’m a good guy, I swear. We’re the nice-guy frat, along with being the cs-bro frat."
                            menu:
                                "{i}Ask about what they talked about.{/i}":
                                    jump talk_about_subpart
                                "{i}Say that you don’t believe hRim and express your suspicion towards him.{/i}":
                                    jump suspicion_frat
                "{i}Express your disapproval of his nonchalant reaction.{/i}":
                    mc "Is that really your reaction to our friend’s death? That’s a little fucked up..."
                    frat_bro "Well, after I found out that he wasn’t FTB — FOR THE BOYS — I didn’t really care for him after that. I was hanging out with him at lake lag when I found out he doesn’t vibe with the boys, so I left him there. But it won’t be like that with you, right?"
                    menu:
                        "{i}Express your suspicion towards him supposedly “leaving him there”.{/i}":
                            mc "You just left him there? I don’t believe that…"
                            show frat_bro angry
                            frat_bro "Whoa whoa whoa! Are you trying to accuse me of murdering Jim? That’s a really strong accusation!"
                            frat_bro "I told you I left him there at lake lag, and I don’t know what happened to him after that if he was murdered then. How dare you accuse me! I think you should leave."
                            jump middle
                        "{i}Ask about what they talked about.{/i}":
                            jump talk_about_subpart
        "{i} Ask about the frat house {/i}":
            mc "Damn, what frat is this house for? You guys seem like you’d have a lit time here."
            show frat_bro
            frat_bro "Abso-fucking-lutely my guy! We throw down all the time and it’s always a great time here at Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa."
            frat_bro "It’s been a bit busy because of pledge or, sorry our new member process, but it’s been fun overall."
            menu:
                "{i}Ask what they do for pledge.{/i}":
                    mc "What kind of things do you do for pledge?"
                    frat_bro "Ah sorry man, that’s a secret. Let’s just say it involves Lake Lag. That’s all I’ll say. But it’s a lit ass time brother — if you want to rush our frat, you can see for yourself!"
                    menu:
                        "{i}Ask if he is aware about what happened with Jim at Lake Lag.{/i}":
                            mc "Lake lag? Are you aware about what happened with Jim there?"
                            show frat_bro sad
                            frat_bro "Um, if you’re referring to me taking him there, yeah. I was hanging out with him at lake lag one night."
                            frat_bro "But I found out that he wasn’t FTB — FOR THE BOYS — that night, and I didn’t really care for him after that. So I left him there when I found out he doesn’t vibe with the boys. I don’t know what happened after that."
                            jump talk_about
                        "{i}Enthusiastically express your desire to rush and join the frat.{/i}":
                            show frat_bro
                            mc "Yeah, I want to rush! I’d like to be a part of the frat too!"
                            frat_bro "Hmm…I don’t know yet. We at Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa are very selective in our process of choosing the new pledge class."
                            frat_bro "I’ve got to get to know you better first, and I think you have to get to know me better too. Ask me some more questions."
                            menu:
                                "{i}Ask if he has been at Lake Lag recently, besides for pledge.{/i}":
                                    label besides_pledge:
                                        mc "Have you hung out at Lake Lag recently, besides for pledge?"
                                        frat_bro "Yeah actually, that’s a lit place for a date! I took a guy I was seeing, Jim, to that spot."
                                        frat_bro "But I found out that he wasn’t FTB — FOR THE BOYS — that night, and I didn’t really care for him after that."
                                        frat_bro "So I left him there when I found out he doesn’t vibe with the boys. I don’t know what happened after that."
                                        menu:
                                            "{i}Ask about what they talked about.{/i}":
                                                jump talk_about_subpart
                                            "{i}Ask him if he knows Jim and that he’s been murdered recently.{/i}":
                                                show frat_bro sad
                                                mc "Do you know who Jim is? Did you know he’s been murdered recently at Lake Lag?"
                                                frat_bro "Daaamn that’s insane. Did they get transported or something? That would have been a sick story to tell ah ha ha. Anyways, do you wanna watch anything?"
                                                jump frat_guy_location
                                "{i}Ask him if he knows Jim and that he’s been murdered recently.{/i}":
                                    show frat_bro sad
                                    mc "Do you know who Jim is? Did you know he’s been murdered recently at Lake Lag?"
                                    frat_bro "Daaamn that’s insane. Did they get transported or something? That would have been a sick story to tell ah ha ha. Anyways, do you wanna watch anything?"
                                    jump frat_guy_location

                "{i}Enthusiastically ask when Brett and his frat are throwing down next.{/i}":
                    mc "Dang, let me know when y’all are throwing down next!"
                    show frat_bro
                    frat_bro "For sure man! It’s always a lit ass time when Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa throws down. You gotta be FTB to come through though — FOR THE BROTHERHOOD."
                    menu:
                        "{i}Enthusiastically express your desire to rush and join the frat.{/i}":
                            mc "Hell yeah brother, I am FTB! If it means being with more guys like you, that’d be awesome."
                            show frat_bro weird
                            frat_bro "Hmm…I don’t know yet. We at Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa are very selective in our process of choosing the new pledge class."
                            frat_bro "I’ve got to get to know you better first, and I think you have to get to know me better too. Ask me some more questions."
                            menu lag_and_murder:
                                "{i}Ask if he has been at Lake Lag recently, besides for pledge.{/i}":
                                    jump besides_pledge
                                "{i}Ask him if he knows Jim and that he’s been murdered recently.{/i}":
                                    mc "Do you know who Jim is? Did you know he’s been murdered recently at Lake Lag?"
                                    frat_bro "Daaamn that’s insane. Did they get transported or something? That would have been a sick story to tell ah ha ha. Anyways, do you wanna watch anything?"
                                    jump frat_guy_location
                        "{i}Tell him that you are kidding and that you are here to ask him upfront about Jim’s murder.{/i}":
                            mc "I was kidding. To “throw down” with you is not why I’m actually here. I wanted to ask about Jim. He was murdered."
                            mc "I wanted to ask about Jim. He was murdered."
                            show frat_bro sad
                            frat_bro "Daaamn that’s insane. Did they get transported or something? That would have been a sick story to tell ah ha ha. Anyways, do you wanna watch anything?"
                            jump frat_guy_location
        "{i}Ask Brett where he thinks the best place to party at is other than this house.{/i}":
            mc "Other than this house, where do you think the best place is to party at?"
            show frat_bro
            frat_bro "You came to the right guy to ask that question. No doubt it’s this one spot by Lake Lag."
            frat_bro "Hella good vibes and we always turn up there because only a few people know where it is. I took someone there a while ago and it was fun."
            menu:
                "{i}Ask him who he took to Lake Lag.{/i}":
                    mc "Who did you take there?"
                    frat_bro "I took this other person I was seeing at the time, Jim. He wanted to get lit with us so I took him there, and we had a good time."
                    frat_bro "Didn’t hear from him after that though. But I mean, if you’re for the BROTHERHOOD, and are possibly thinking about joining the frat too, let me know and I can take you there too, or anywhere else."
                    menu:
                        "{i}Ask about what they talked about.{/i}":
                            jump talk_about_subpart
                        "{i}Ask him if he might know why he hasn’t heard back from Jim.{/i}":
                            mc "You have no idea why you haven’t heard back from him?"
                            frat_bro "I mean, I heard something about a murder on Fizz, and I thought for a second that it might’ve been about Jim, but I wasn’t sure. I just figured he was just ghosting me."
                            menu:
                                "{i}Tell Brett that it was indeed Jim and that that is why you are here.{/i}":
                                    mc "Actually, it was him. My roommate Jim was the guy that died last weekend and I’ve been trying to find out anything related to the murder."
                                    show frat_bro sad
                                    frat_bro "Daaamn that’s insane. Did they get transported or something? That would have been a sick story to tell ah ha ha. Anyways, do you wanna watch anything?"
                                    jump frat_guy_location
                                "{i}Affirm his belief that Jim was just ghosting him.{/i}":
                                    mc "Yeah, I think he was just ghosting you."
                                    show frat_bro weird
                                    frat_bro "Damn, fuck him then. I’ll take you to Lake Lag later too if you’d like?"
                                    mc "No thanks. I gotta go."
                                    jump middle
                        "{i}Accuse him straight up for murdering Jim.{/i}":
                            mc "You didn’t hear from him because you murdered him, didn’t you!"
                            show frat_bro angry
                            frat_bro "Whoa whoa whoa! That’s a really strong accusation! I didn’t even know Jim was murdered or died! How dare you accuse me! I think you should leave."
                            jump middle
                "{i}Ask him when he plans on taking you to Lake Lag,{/i}":
                    mc "Dang, when are you taking me there?"
                    frat_bro "I’ll take you whenever you want man! It’s a lit ass spot. You gotta be FTB to go with me though — FOR THE BROTHERHOOD."
                    menu:
                        "{i}Express that you are down and that you are FTB.{/i}":
                            mc "I’m down! I am FTB — if it means being with more guys like you, that’d be awesome. Can I join the frat?"
                            frat_bro "Hmm…I don’t know yet. We at Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa are very selective in our process of choosing the new pledge class."
                            frat_bro "I’ve got to get to know you better first, and I think you have to get to know me better too. Ask me some more questions."
                            menu:
                                "{i}Ask if he has been at Lake Lag recently, besides for pledge.{/i}":
                                    jump besides_pledge
                                "{i}Ask him if he knows Jim and that he’s been murdered recently.{/i}":
                                    mc "Do you know who Jim is? Did you know he’s been murdered recently at Lake Lag?"
                                    show frat_bro sad
                                    frat_bro "Daaamn that’s insane. Did they get transported or something? That would have been a sick story to tell ah ha ha. Anyways, do you wanna watch anything?"
                                    jump frat_guy_location
                        "{i}Say that you were kidding and that you’re really here to ask him about Jim’s murder.{/i}":
                            mc "I was kidding. To hang out with you is not why I’m actually here. I wanted to ask about Jim. He was murdered."
                            jump frat_guy_location
        "{i} \[Retrieve more info to ask Brett this question\] {/i}" if puzzle_solved==0:
            jump brett_menu
        "{i}\[Unlocked\]: Ask Brett for a hoodie {/i}" if  puzzle_solved==1:
            mc "Hey, it's really cold out here, could I borrow a hoodie?"
            show frat_bro weird
            frat_bro "Yeah bro, it’s funny you mention that, I found this sweet hoodie at Lake Lag right after the date with Jim."
            frat_bro "It’s got some red stains on it, but it’ll probably come out when you wash it"
            show cl4:
                zoom 2
                truecenter
            $ clue4 += 1
            mc "Thanks so much! I'll return it next week. Bye!"
            frat_bro "Keep it, I just found it lying near Lag and finder keeper or whatever yaknow"
            jump middle
                        
    # Display the ending
    frat_bro "Thanks for a great date! Let's do it again sometime."
    jump middle


label CS_guy_date:
    scene bg huang: 
        zoom 1
        truecenter

    # Increment the love level
    $ love += 1
    show cs_guy:
        zoom 1
        truecenter
    $ date_counter += 1

    # Display the date dialogue
    mc "Hey Brian! It’s great to meet you, excited to hang out with you!"
    cs_guy "Me too! I saw that your Hinge profile mentions that you’re a CS major! Talking about machine learning models really gets me going."

    # Display the food choice
    menu:
        "{i}Be upfront and interrogate Brian directly about Jim’s murder.{/i}":
            mc "Look I know that we’re supposed to be on a date right now but I was hoping we could talk a bit more about my roommate Jim, who I know you went out on a date with"
            show cs_guy sad
            cs_guy "Oh, I really liked Jim even though he wasn’t a CS major. Clearly, he wasn’t able to understand anything about my projects and any of my passions. Still, it was a shame to hear about the Lake Lag incident."
            menu: 
                "{i}Ask Brian where he was that night, and if he has any alibis to back it up.{/i}":
                    mc "Where were you that night? Do you have any alibis or any evidence to back that up?"
                    cs_guy "I actually don’t but I was hanging out with my friend Brett before he said he had to go to Lake Lag for some Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa rush event."
                    show cs_guy
                    cs_guy "After that, I was working by myself on one of my project’s – AlibiAI – code. That’s when the Jim murder happened, but I didn’t really take pictures of me coding or being in the room"
                    "{i} You remember that Brett was also one of Jim's romantic interests that you thought of as a possible suspect. {/i}"
                    menu: 
                        "{i}Interrogate further about the frat’s rush event and Brett.{/i}":
                            show cs_guy
                            mc "What rush event? Can you tell me more about Brett?"
                            show cs_guy shy
                            cs_guy "Apparently the pledges were bringing potential dates to Lake Lag. That’s all I know. And Brett is a good friend of mine that I hang out with when I need to let loose after grinding on CS PSets and AlibiAI."
                            cs_guy "He gets it you know, what it’s like being a CS major, with the frat he’s in being the CS-bro frat. But things have been weird lately, ever since he also started seeing Jim at the same time as me."
                            menu frat_guy_converge: 
                                "{i}Express your sympathy for things having gotten weird for Brian and his friend.{/i}":
                                    mc "Aw, I’m sorry to hear that things have been weird with you and Brett."
                                    show cs_guy
                                    cs_guy "Oh, it’s no worries. Thanks for expressing your concern, but I’ve realized that romance and love only get in the way of my intellectual pursuits. Unless my partner were to also be as good at CS as I am."
                                    cs_guy "Anyways, do you want to hear more about my current intellectual pursuits?"
                                    menu: 
                                        "Yes":
                                            mc "Sure"
                                            jump ask_more_alibi_ai
                                        "No":
                                            mc "No, I'm good"
                                            show cs_guy angry
                                            cs_guy "Oh alright. Well then, if you don’t care about my intellectual pursuits either, then I’m gonna have to ask you to leave."
                                            mc "Sorry for the trouble!"
                                            jump middle
                                "{i} Ask for Brett’s phone number.{/i}":
                                    mc "Can I get Brett’s number?"
                                    show cs_guy angry
                                    cs_guy "Really? After what I just said about things being weird because of a mutual love interest? No, I won’t give you his number. In fact, I’m gonna have to ask you to leave."
                                    mc "Sorry for the trouble!"
                                    jump middle
                                "{i} Ask to hear more about AlibiAI. {/i}":
                                    jump ask_more_alibi_ai
                        "{i} Ask to hear more about AlibiAI. {/i}":
                            label ask_more_alibi_ai:
                                mc "Can you tell me more about AlibiAI?"
                                show cs_guy
                                cs_guy "That’s a personal project that I’ve been working on ever since Andrew Ng told me that it would be a cool idea to look into."
                                cs_guy "AlibiAI is an app that uses AI to help you create foolproof alibis using relevant details that you input."
                                cs_guy "I personally thought it was a bit weird when he first told me about the idea, but I talked to my friend Brett about it, and he really strongly encouraged me to pursue it and implement it."
                                cs_guy "I even have funding for it in the works now — I pitched my idea to some hotshot ex-CEO named Britneigh, who is now handling all the business stuff. I don’t know too much about those details though."
                                "{i}You remember that Brett was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                                menu more_alibi_ai: 
                                    "{i} Compliment his AlibiAI project and his engineering skills for being able to build it.{/i}":
                                        mc "That sounds like a really cool project! It sounds like a very technically challenging engineering problem, so it’s so cool to see that you’re smart enough to tackle it."
                                        cs_guy "Oh, you’re too kind! But also you’re not wrong. Doesn’t AlibiAI sound like a pretty awesome project? It’s awesome to see that great can recognize great."
                                        cs_guy "Here, I can give you the access key to the beta demo if you want to check it out?"
                                        show cl1:
                                            zoom 1.7
                                            xalign 0.5 yalign 0.4
                                        $ clue1 += 1
                                        show cs_guy shy
                                        cs_guy "Sorry I've got to head out really quick. Just remembered I have section. Bye!"
                                        jump middle
                                    "{i} Ask about why Brett might have encouraged him so much to build AlibiAI.{/i}":
                                        mc "Why did Brett encourage you so much to build AlibiAI?"
                                        show cs_guy angry
                                        cs_guy "Honestly, I’m not really sure why. But it did seem like it might be because he really wanted to use it for himself." 
                                        cs_guy "But that’s all I’ll say. Anyways, I gotta get going. Gotta keep working on my project. See you later! "
                                        jump middle
                                    "{i} Ask to hear more about Britneigh and the business side of things.{/i}":
                                        mc "Can you tell me any more about Britneigh and the business side of things?"
                                        show cs_guy angry
                                        cs_guy "Oh god, you care more about the business side of things than the sick tech??"
                                        cs_guy "Ugh. To answer your question, there’s not much I can tell you because she hasn’t been communicating very well about it.  But you can go ask her yourself if you want."
                                        cs_guy "Anyways, I think this date is over."
                                        jump middle
                "{i}Ask about how the date with Jim went.{/i}":
                    mc "What did you guys talk about? How did your date go with Jim?"
                    show cs_guy angry
                    cs_guy "I tried explaining my projects to Jim, like for example my project AlibiAI, but he really didn’t understand what I was talking about. That’s when I knew that things between us weren’t going to work out."
                    cs_guy "Also, he was clearly more into my friend Brett and mentioned his name multiple times during our date. He even told me that they were supposed to meet up later somewhere." 
                    cs_guy "Since then, things between Brett and I have been a little weird, but I guess that’s not that important."
                    jump frat_guy_converge
                
        "{i}Ask him enthusiastically about his project, research, and work.{/i}":
            mc "Yes, I’d love to chat about your projects and what kind of research you’re doing! It’s so cool to connect with someone who is interested in the same things as me!"
            show cs_guy
            cs_guy "I’d love to tell you all about the amazing things that I’ve been working on! It’s really setting me up for success for my Stanford CS PhD applications."
            cs_guy "I’m currently working in 2 labs, the main one being Andrew Ng’s lab which is super prestigious to get into."
            cs_guy "I’m also working on a personal project called AlibiAI while being in 25 units this quarter — I’m taking CS 224n, CS 231n, CS 224w, CS 229, and CS 230. This quarter has been one of the lighter quarters this year though, which is nice."

            menu: 
                "{i}Ask how he is able to juggle all of those commitments.{/i}":
                    mc "Dang, that’s so many classes! How do you juggle all of that?"
                    show cs_guy sad
                    cs_guy "This? You think this is a lot? Oh boy, you should’ve seen me last quarter… I think I was in like 40 units! This is nothing compared to that."
                    cs_guy "This quarter has been more about focusing on my personal projects, mainly AlibiAI, and hanging out with my friend Brett who is in Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa, the CS-bro frat."
                    cs_guy "He was actually the one who encouraged me to pursue implementing the tech for the personal project I mentioned."
                    "{i}You remember that Brett was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                    menu frat_converge_2: 
                        "{i} Ask about why Brett might have encouraged him so much to build AlibiAI.{/i}":
                            mc "Why did Brett encourage you so much to build AlibiAI?"
                            show cs_guy shy
                            cs_guy "Honestly, I’m not really sure why. But it did seem like it might be because he really wanted to use it for himself. But that’s all I’ll say. Anyways, I gotta get going. Gotta keep working on my project. See you later! "
                            jump middle
                        "{i} Ask for Brett’s phone number.{/i}":
                            mc "Can I get Brett’s number?"
                            show cs_guy angry
                            cs_guy "Really? After what I just said about things being weird because of a mutual love interest? No, I won’t give you his number. In fact, I’m gonna have to ask you to leave."
                            mc "Sorry for the trouble!"
                            jump middle
                        "{i} Ask to hear more about AlibiAI. {/i}":
                            jump ask_more_alibi_ai

                "{i}Ask about what he does outside of work.{/i}":
                    mc "I’d love to hear more about what you do outside of work though!"
                    show cs_guy
                    cs_guy "Hmm let’s see…outside of work, sometimes I really need to let loose and I go hang out at LAIR. I just love being around CS, you know?"
                    cs_guy "But I guess other than that, and other than trying to find dates at Huang basement, I’ll hang out with my friend Brett who is in Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa, the CS-bro frat."
                    cs_guy "He was actually the one who encouraged me to pursue implementing the tech for AlibiAI, the project I mentioned earlier, when I told him about it."
                    "{i}You remember that Brett was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                    jump frat_converge_2

label start_up_date:
    scene bg coupa: 
        zoom 1
        truecenter
    $ date_counter += 1

    # Increment the love level
    $ love += 1
    show startup_girl:
        zoom 1
        truecenter

    # Display the date dialogue
    mc "Hey there! So, you're all about startups and entrepreneurship, huh? Changing the world one app at a time?"
    startup_girl "Absolutely! I'm like the Elon Musk of dorm room innovations. The next big thing is just a pitch deck away!"
    menu: 
        "{i}Be upfront and interrogate Britneigh directly about Jim’s murder.{/i}":
            mc "Let’s get down to business. I know I called you here for a date, but I’m here to investigate the details of the murder of my roommate Jim, who I know you were seeing."
            mc "Where were you on the night when Jim was murdered at Lake Lag?"
            label down_to_business:
                show startup_girl sad
                startup_girl " Ah, the night of that incident. I was sad to hear about that. Well, here's the deal, I was actually rocking the startup scene at an ultra-exclusive conference. Top secret stuff! "
                menu:
                    "{i}Ask Britneigh if she has any proof that she was really at that conference.{/i}":
                        mc "Is there any way you can prove you were there? Any witnesses or photos?"
                        show startup_girl
                        startup_girl "Oh, I wish! Unfortunately, this event was like a covert mission—invite-only, no social media allowed. It was so secretive, they had a password just to use the bathroom."
                        startup_girl "What I can share though is what my new startup is currently working on, which is really exciting!"
                        menu: 
                            "{i}Give in and let her share her startup idea to you.{/i}":
                                mc "Sigh…okay, what’s your startup idea?"
                                jump next_big_thing
                            "{i}Keep grilling her about her alibi.{/i}":
                                mc "No, I don’t really care. What I really want to know is proof that you really were at this “conference” on that night."
                                startup_girl "I swear, it’ll only take a second to pitch it to you! Okay, picture this —"
                                jump next_big_thing
                    "{i}Ask what the conference was for.{/i}":
                        mc "What was the conference for?"
                        show startup_girl
                        startup_girl "Oh, I wish I could tell you! Unfortunately, this event was like a covert mission—invite-only, no social media allowed."
                        startup_girl "It was so secretive, they had a password just to use the bathroom. What I can share though is what my new startup is currently working on, which is really exciting!"         
                        menu: 
                            "{i}Give in and let her share her startup idea to you.{/i}":
                                mc "Sigh…okay, what’s your startup idea?"
                                jump next_big_thing
                            "{i}Keep grilling her about her alibi.{/i}":
                                mc "No, I don’t really care. What I really want to know is proof that you really were at this “conference” on that night."
                                startup_girl "I swear, it’ll only take a second to pitch it to you! Okay, picture this —"
                                jump next_big_thing
                    "{i}Ask about what startup she’s currently working on that she presented there.{i}":
                        mc "What kind of startup are you working on that you brought to the table there?"
                        jump next_big_thing
        "{i}Ask Britneigh what she is currently working on.{/i}":
            mc "So what’s your next big thing?"
            label next_big_thing:
                show startup_girl flirty
                startup_girl "'AlibiAI' – the ultimate solution for concealing unsavory activities. It's a revolutionary app that helps you create foolproof alibis, no questions asked."
                startup_girl "AlibiAI is all about empowering individuals to control their narratives."
                startup_girl "It's not just for criminals, but for anyone who wants to maintain privacy, protect their reputation, or maybe even hide a harmless secret or two."

                menu :
                    "{i}Express that this project seems suspicious.{/i}":
                        mc "This sounds very suspicious…"
                        show startup_girl sad
                        startup_girl "Yes I know about the recent murder…but this is completely unrelated to that, I swear. I’m only working on this because Brian suggested the idea to me and wanted my help on the business side of things."
                        "{i}You remember that Brian was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                        menu more_brian: 
                            "{i}Ask to hear more about Brian.{/i}":
                                mc "Brian? Can you tell me more about him?"
                                startup_girl "I honestly don’t know much about him, and that’s mostly because I’ve been trying to keep him in the dark on a lot of the business side of things."
                                startup_girl "I guess he is the one who pitched the idea to me, but I'm more of a visionary, ya know?"
                                startup_girl "So things like who I’ve been getting funding from, Stanford BASES, I don’t really tell him about. But, I don’t really know anything about the guy. We barely talk."
                                menu: 
                                    "{i}Criticize her for taking credit for Brian’s idea.{/i}":
                                        mc "You shouldn’t take credit for that…especially if it wasn’t your idea originally. That’s a little messed up."
                                        show startup_girl angry
                                        startup_girl "Hey, who are you to tell me what I should and shouldn’t do?"
                                        startup_girl "I’m an entrepreneur of several startups alongside this one, and I’m very successful so I know what I’m doing. You know what, I should leave. I have to get going anyway."
                                        jump middle
                                    "{i}Affirm her desire to take credit and give her positive validation.{/i}":
                                        mc "I guess I get why you’d want to take the credit. It is a really cool idea, after all. It’s honestly so impressive how you’re spearheading the business side of things."
                                        show startup_girl flirty
                                        startup_girl "Thanks so much! It’s cool to see that it seems like an exciting project to you too!"
                                        startup_girl "Here, I gotta get going, but let me give you my business card so we can chat more later. Would love to grab a meal sometime!"
                                        show cl2:
                                            zoom 1.5
                                            xalign 0.5 yalign 0.4
                                        $ clue2 += 1
                                        mc "Bye!"
                                        jump middle

                            "{i}Ask her if she is aware that Brian was seeing Jim as well, and remind her that Jim was murdered.{/i}":
                                mc "Brian? Are you aware that he was seeing Jim, the person who was murdered at Lake Lag recently?"
                                show startup_girl sad
                                startup_girl "Whoa, I had no idea! I didn’t know Jim was seeing other people. But I swear, I didn’t know that about Brian — "
                                startup_girl "I’ve honestly been trying to keep him in the dark on a lot of the business side of things, and as a result, we don’t really communicate that much."
                                startup_girl "He is the one who pitched the idea to me, but I kinda want the credit for myself, ya know? So things like who I’ve been getting funding from, Stanford BASES, I don’t really tell him about. We barely talk."
                                menu:
                                    "{i}Criticize her for taking credit for Brian’s idea.{/i}":
                                        mc "You shouldn’t take credit for that…especially if it wasn’t your idea originally. That’s a little messed up."
                                        show startup_girl angry
                                        startup_girl "Hey, who are you to tell me what I should and shouldn’t do? I’m an entrepreneur of several startups alongside this one, and I’m very successful so I know what I’m doing."
                                        startup_girl "You know what, I should leave. I have to get going anyway."
                                        jump middle
                                    "{i}Affirm her desire to take credit and give her positive validation.{/i}":
                                        mc "I guess I get why you’d want to take the credit. It is a really cool idea, after all. It’s honestly so impressive how you’re spearheading the business side of things."
                                        startup_girl "Thanks so much! It’s cool to see that it seems like an exciting project to you too! Here, I gotta get going, but let me give you my business card so we can chat more later. Would love to grab a meal sometime!"
                                        show cl2:
                                            zoom 1.5
                                            xalign 0.5 yalign 0.4
                                        $ clue2 += 1
                                        mc "Bye!"
                                        jump middle
                    "{i}Ask her how this idea would work.{/i}":
                        mc "How would this even work?"
                        show startup_girl
                        startup_girl "Simple. Users would input relevant details about their desired alibi—time, location, circumstances—and AlibiAI's advanced algorithms would generate a meticulously crafted narrative, backed by seemingly authentic evidence."
                        startup_girl "We'd offer different package tiers, from basic cover-ups to deluxe setups that include tailored social media posts and forged documents. Unsure how the technology works - "
                        startup_girl "I’m on the business side of things, but you can email my colleague Brian who came to me with the idea and wanted my help on the business side of things while he codes it."
                        "{i}You remember that Brian was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                        jump more_brian
                    "{i}Ask her if this is her own original idea.{/i}":
                        mc"Is this your own original idea?"
                        startup_girl "I mean…depends on how you define “original”. It is my idea now too, since I’m working on the business side as the COO, but I will admit that Brian did suggest the idea to me originally because he wanted my help."
                        "{i}You remember that Brian was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                        jump more_brian
        "{i}Butter her up and ask her if she wants to go rock climbing with you.{/i}":
            mc "Wow, you look like you’d be really good at rock climbing. Want to go with me some time?"
            show startup_girl flirty
            startup_girl "Rock climbing! You know, I have a bit of a reputation in climbing circles. They call me the Spider."
            startup_girl "As much as I would love to though, I unfortunately won’t be able to. I’ve had my hands really full recently, so I really don’t have much free time these days. You know, other than for quick casual dates like this."
            menu:
                "{i}Ask her about why she’s so busy.{/i}":
                    mc "What’s got you so busy?"
                    jump next_big_thing
                "{i}Flip on her and start grilling her about the murder of Jim.{/i}":
                    mc "I was making fun of you. I don’t even like rock climbing. What I really want to know is that you were doing on the night that my roommate Jim was murdered!"
                    jump down_to_business
        



    # Display the ending
    startup_girl "Thanks for a great date! Let's do it again sometime."
    jump middle

label police_segment:
    if date_counter < 3:
        "{i}Sorry either you haven't been on all of the dates or haven't picked up all the clues from the dates!{/i}"
        jump middle
    scene bg police: 
        zoom 1
    show police_officer:
        zoom 1
        truecenter
    
    police_officer "This is Stanford Police open up."
    mc "Woah, hi there. How can I help you?"
    police_officer "We’re just here to ask a few questions regarding the recent death of your roommate."
    police_officer "While we have no particular suspects, we need to start by asking if you knew anything that could help with the investigation of the murder."
    police_officer "Is there anyone that you are aware of that your roommate interacted with prior to their death?"
    menu:
        mc "Yes! I know who did it! It was"
        "{i}Report Brett{/i}":
            mc "It was Brett!"
            police_officer  "Hm… interesting… Alright, we're going to bring him in immediately for questioning."
            mc "Don't you need a warrant? Or evidence?"
            police_officer  "Nah f*** these kids!"
            scene bg black:
                zoom 10
            show frat_bro:
                zoom 1.5
                truecenter
            police_officer "THIS IS STANFORD POLICE! OPEN UP!"
            police_officer "WE'RE BRINGING YOU INTO CUSTODY FOR JIM'S MUDER"
            show frat_bro angry
            frat_bro "Woah woah woah! Chill man! I didn’t do anything alright. What are you guys even talking about?!"
            police_officer "We know you’re lying! Get on the floor and put your hands behind your back!"
            show frat_bro sad
            frat_bro "NO! Wait, I really don’t know what’s happening! Can we all just chill the fuck out?! My boys are gonna be furious if they find out this has happened!"
            police_officer "Where you’re going no one will be FTB and you’ll be kept away from the boys for a long long time!"
            frat_bro "NO! NOT MY BOYS! I NEED MY BOYS! NOOOOOOO!!!!!!"
            jump wrong_murderer
        "{i}Report Brian{/i}":
            mc "It was Brian!"
            police_officer "Hm… interesting… Alright, we're going to bring him in immediately for questioning."
            mc "Don't you need a warrant? Or evidence?"
            police_officer  "Nah f*** these kids!"
            scene bg black:
                zoom 10
            show cs_guy:
                zoom 1.5
                truecenter
            police_officer "THIS IS STANFORD POLICE! OPEN UP!"
            police_officer "WE'RE BRINGING YOU INTO CUSTODY FOR JIM'S MUDER"
            show cs_guy angry
            cs_guy "What?! I don’t even know who that is?! What are you talking about?"
            police_officer "Of course you know! You murdered him!"
            cs_guy "How do I have time to think about murdering someone, much less having the time to actually do it, when I’m literally grinding 229, 140, and 110 at the same time?"
            police_officer "We don’t care what those numbers mean nor do we like to think about numbers! Get on the ground!"
            show cs_guy sad
            cs_guy "I swear you have the wrong person! No! I was just about to push my latest commit too and then submit the psets!!!! Just let me submit them first!!!!!!!!"
            jump wrong_murderer
        "{i}Report Britneigh{/i}":
            mc "It was Britneigh!"
            police_officer  "Hm… interesting… Alright, we're going to bring her in immediately for questioning."
            mc "Don't you need a warrant? Or evidence?"
            police_officer  "Nah f*** these kids!"
            scene bg black:
                zoom 10
            show startup_girl:
                zoom 1.5
                truecenter
            police_officer "THIS IS STANFORD POLICE! OPEN UP!"
            police_officer "WE'RE BRINGING YOU INTO CUSTODY FOR JIM'S MUDER"
            show startup_girl angry
            startup_girl "What?! I don’t even know who that is?! What are you talking about?"
            police_officer "Of course you know! You murdered him!"
            startup_girl "I’ve literally been meeting with 20 VCs a day!? How could I possibly enough care enough about anyone to not flake with them, much less carry out a murder?"
            police_officer "That’s exactly the type of cold heartless personality that would kill someone and hide it perfectly! Get on the ground!"
            show startup_girl sad
            startup_girl "I swear you have the wrong person!"
            startup_girl "No! I was literally just about to grab coffee with Pearquoia Ventures and raise for my pre-pre Series F funding round! Please let me just circle back with them really quickly!"
            jump correct_killer_identified


label correct_killer_identified:
    scene bg oval: 
        zoom 1.75
    "You caught the correct killer! Congrats!"
    return

label wrong_murderer:
    scene bg dorm: 
        zoom 1.7
    mc "Wow thank god, we finally caught the murderer. I’m glad that’s over with. "
    scene bg murder:
        zoom 4
    show anonymous_guy:
        zoom 1.2
        truecenter
    anonymous_guy "Sorry to do this to you, but I just can’t let you go free, especially when you know too much!"
    anonymous_guy "I'm going to have to kill you before they realize they have the wrong person!"
    "Oops! You identified the wrong murderer. Play the game again!"
    return