
define mc = Character("Me")

# Define the love level variable
default love = 0

# Define the total date counter variable
default date_counter = 0

# Define the character to be dated

define startup_girl = Character("Britneigh", color="#c8ffc8", image="startup_girl")
define cs_guy = Character("Brian", color="#c8ffc8", image="cs_guy")
define frat_bro = Character("Brett", color="#c8ffc8", image="frat_bro")
define police_officer = Character("Police", color="#c8ffc8", image="police_officer")
define anonymous_guy = Character("Killer", color="#c8ffc8", image="anonymous_guy")

image startup_girl = "startup_girl.png"

image cs_guy = "cs_guy.png"
image frat_bro = "frat_guy.png"
image hinge = 'hinge.jpeg'
image police_officer = 'police_officer.png'
image anonymous_guy = 'anonymous_guy.png'


image card = "card.jpeg"

# Define the starting label
label start:
    scene bg oval: 
        zoom 1.75

    # Display the introduction
    "It was a bright morning at Stanford University when I saw this on my phone..."

    # Display the date choice

    scene bg fizz:
        zoom 1.38
        truecenter

    "Eventually, after not hearing from my roomate, I realized that these Fizz and FoHo posts are about Jim!"

    scene bg dorm:
        zoom 3.0
    
    "Jim was my freshman year roommate and we’ve lived together every year since. I can’t believe he’s gone, I warned him to not go on dates with weirdos on this campus."

    scene bg oval: 
        zoom 1.75
    
    show hinge:
        zoom 1.3
        truecenter

    "There’s no way there was no evidence. The killer showed no remorse, their dating profile is probably still active. I have to find the murderer, guess it’s time to get on Tinge."


    
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

label middle:

    scene bg oval: 
        zoom 1.75
    
    show hinge:
        zoom 1.3
        truecenter
    
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
    


# Define the date label
label frat_bro_date:
    scene bg frat: 
        zoom 1.5

    # Increment the love level
    $ love += 1
    $ date_counter += 1
    show frat_bro:
        zoom 1.5

    # Display the date dialogue
    mc "Hey Brett! Damn I’ve never been in the house before. Thanks for letting me in!"
    frat_bro "Absolutely my guy. Anything for a good time ;)"
    mc "Uh… yeah absolutely? Anyways…"

    # Display the food choice
    menu:
        "Not to be a buzzkill, but my roommate Jim was the guy that died last weekend and I’ve been trying to find out anything related to the murder.":
            frat_bro "Daaamn that’s insane. Did they get transported or something? That would have been a sick story to tell ah ha ha. Anyways, do you wanna watch anything?"
            menu frat_guy_location:
                "Where were you on that night?":
                    frat_bro "Well I won’t lie, I was hanging out with him at lake lag that night. But I found out that he wasn’t FTB — FOR THE BOYS — that night, and I didn’t really care for him after that. So I left him there when I found out he doesn’t vibe with the boys. I don’t know what happened after that."
                    menu talk_about: 
                        "Did y’all talk about anything else?":
                            frat_bro "I guess we did talk about this thing that a few of my other friends, Britneigh and Brian, were building, AlibiAI. We were laughing about it because it was an idea that seemed so dumb, so I encouraged Brian to go through with building it as a prank, and I even managed to get him to pitch the idea to Britneigh. LOL! It was kind of strange though — Britneigh seemed a little wayyy too excited for the idea for some reason ahaha."
                            "{i}Brett and Britneigh were also Jim's romantic interests that you thought of as possible suspects.{/i}"
                            frat_bro "But anyways, I wanted to ask you…are you FTB? As in… FOR THE BOYS????"
                            menu:
                                "Absolutely not. I have reason to believe you might have murdered Jim.":
                                    frat_bro "Whoa whoa whoa! That’s a really strong accusation! I told you I left him there at lake lag, and I don’t know what happened to him after that if he was murdered then. How dare you accuse me! I think you should leave."
                                    jump middle
                                "Hell yeah, brother!":
                                    frat_bro "HELL YEAH BROTHER!! Alright man, listen…I can tell you’re a good guy. You’d make a good BROTHER. And I want to tell you the secret fraternity Latin phrase to seal the deal with your future acceptance into the fraternity. Here, it’s written on this piece of paper in this envelope. Take it with you, and open it once you are in private."
                                    #show the clue
                                    mc "Thanks!"
                        "Can you prove that you left him before he died and that you didn’t murder him?":
                            frat_bro "Nah I can’t prove it man, but you can choose to believe me! I’m a good guy, I swear. We’re the nice-guy frat, along with being the cs-bro frat."
                            menu:
                                "Did y’all talk about anything in particular?":
                                    jump talk_about
                                "Absolutely not. I have reason to believe you might have murdered Jim.":
                                    frat_bro "Whoa whoa whoa! That’s a really strong accusation! I told you I left him there at lake lag, and I don’t know what happened to him after that if he was murdered then. How dare you accuse me! I think you should leave."
                                    jump middle

                "Is that really your reaction to our friend’s death? That’s a little fucked up...":
                    frat_bro "Well, after I found out that he wasn’t FTB — FOR THE BOYS — I didn’t really care for him after that. I was hanging out with him at lake lag when I found out he doesn’t vibe with the boys, so I left him there. But it won’t be like that with you, right?"
                    menu:
                        "You just left him there? I don’t believe that…":
                            frat_bro "Whoa whoa whoa! Are you trying to accuse me of murdering Jim? That’s a really strong accusation! I told you I left him there at lake lag, and I don’t know what happened to him after that if he was murdered then. How dare you accuse me! I think you should leave."
                            jump middle
                        "Did y’all talk about anything in particular?":
                            jump talk_about
        "Damn, what frat is this house for? You guys seem like you’d have a lit time here.":
            frat_bro "Abso-fucking-lutely my guy! We throw down all the time and it’s always a great time here at Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa. It’s been a bit busy because of pledge or, sorry our new member process, but it’s been fun overall."
            menu:
                "What kind of things do you do for pledge?":
                    frat_bro "Ah sorry man, that’s a secret. Let’s just say it involves Lake Lag. That’s all I’ll say. But it’s a lit ass time brother — if you want to rush our frat, you can see for yourself!"
                    menu:
                        "Lake lag? Are you aware about what happened with Jim there?":
                            frat_bro "Um, if you’re referring to me taking him there, yeah. I was hanging out with him at lake lag one night. But I found out that he wasn’t FTB — FOR THE BOYS — that night, and I didn’t really care for him after that. So I left him there when I found out he doesn’t vibe with the boys. I don’t know what happened after that."
                            jump talk_about
                        "Not to be a buzzkill, but my roommate Jim was the guy that died last weekend and I’ve been trying to find out anything related to the murder.":
                            jump frat_guy_location
                "Yeah, I want to rush! I’d like to be a part of the frat too!":
                    frat_bro "Hmm…I don’t know yet. We at Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa are very selective in our process of choosing the new pledge class. I’ve got to get to know you better first, and I think you have to get to know me better too. Ask me some more questions."
                    menu besides_pledge:
                        "Have you hung out at Lake Lag recently, besides for pledge?":
                            frat_bro "Yeah actually, that’s a lit place for a date! I took a guy I was seeing, Jim, to that spot. But I found out that he wasn’t FTB — FOR THE BOYS — that night, and I didn’t really care for him after that. So I left him there when I found out he doesn’t vibe with the boys. I don’t know what happened after that."
                            menu:
                                "Did y’all talk about anything in particular?":
                                    jump talk_about
                                "Do you know who Jim is? Did you know he’s been murdered recently at Lake Lag?":
                                    frat_bro "Daaamn that’s insane. Did they get transported or something? That would have been a sick story to tell ah ha ha. Anyways, do you wanna watch anything?"
                                    jump frat_guy_location
                        "Be upfront and interrogate Brett directly about Jim’s murder.":
                            jump frat_guy_location
                "Dang, let me know when y’all are throwing down next!":
                    frat_bro "For sure man! It’s always a lit ass time when Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa throws down. You gotta be FTB to come through though — FOR THE BROTHERHOOD."
                    menu:
                        "Hell yeah brother, I am FTB! If it means being with more guys like you, that’d be awesome.":
                            frat_bro "Hmm…I don’t know yet. We at Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa are very selective in our process of choosing the new pledge class. I’ve got to get to know you better first, and I think you have to get to know me better too. Ask me some more questions."
                            menu:
                                "{i}Ask if he has been at Lake Lag recently, besides for pledge.{/i}":
                                    jump besides_pledge
                                "Do you know who Jim is? Did you know he’s been murdered recently at Lake Lag?":
                                    frat_bro "Daaamn that’s insane. Did they get transported or something? That would have been a sick story to tell ah ha ha. Anyways, do you wanna watch anything?"
                                    jump frat_guy_location
                        "I was kidding. To “throw down” with you is not why I’m actually here. I wanted to ask about Jim. He was murdered.":
                            mc "Not to be a buzzkill, but my roommate Jim was the guy that died last weekend and I’ve been trying to find out anything related to the murder."
                            jump frat_guy_location
        "Other than this house, where do you think the best place is to party at?":
            frat_bro "You came to the right guy to ask that question. No doubt it’s this one spot by Lake Lag. Hella good vibes and we always turn up there because only a few people know where it is. I took someone there a while ago and it was fun."
            menu:
                "Who did you take there?":
                    frat_bro "I took this other person I was seeing at the time, Jim. He wanted to get lit with us so I took him there, and we had a good time. Didn’t hear from him after that though. But I mean, if you’re for the BROTHERHOOD, and are possibly thinking about joining the frat too, let me know and I can take you there too, or anywhere else."
                    menu:
                        "Did y’all talk about anything in particular?":
                            jump talk_about
                        "You have no idea why you haven’t heard back from him?":
                            frat_bro "I mean, I heard something about a murder on Fizz, and I thought for a second that it might’ve been about Jim, but I wasn’t sure. I just figured he was just ghosting me."
                            menu:
                                "Actually, it was him. Not to be a buzzkill, but my roommate Jim was the guy that died last weekend and I’ve been trying to find out anything related to the murder.":
                                    jump frat_guy_location
                                "Yeah, I think he was just ghosting you.":
                                    frat_bro "Damn, fuck him then. I’ll take you to Lake Lag later too if you’d like?"
                                    mc "No thanks. I gotta go."
                                    jump middle
                        "You didn’t hear from him because you murdered him, didn’t you!":
                            frat_bro "Whoa whoa whoa! That’s a really strong accusation! I didn’t even know Jim was murdered or died! How dare you accuse me! I think you should leave."
                            jump middle
                "Dang, when are you taking me there?":
                    frat_bro "I’ll take you whenever you want man! It’s a lit ass spot. You gotta be FTB to go with me though — FOR THE BROTHERHOOD."
                    menu:
                        "I’m down! I am FTB — if it means being with more guys like you, that’d be awesome. Can I join the frat?":
                            frat_bro "Hmm…I don’t know yet. We at Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa are very selective in our process of choosing the new pledge class. I’ve got to get to know you better first, and I think you have to get to know me better too. Ask me some more questions."
                            menu:
                                "Have you hung out at Lake Lag recently, besides for pledge?":
                                    jump besides_pledge
                                "Do you know who Jim is? Did you know he’s been murdered recently at Lake Lag?":
                                    frat_bro "Daaamn that’s insane. Did they get transported or something? That would have been a sick story to tell ah ha ha. Anyways, do you wanna watch anything?"
                                    jump frat_guy_location
                        "I was kidding. To hang out with you is not why I’m actually here. I wanted to ask about Jim. He was murdered.":
                            jump frat_guy_location
                        
    # Display the ending
    frat_bro "Thanks for a great date! Let's do it again sometime."
    jump middle

label CS_guy_date:
    scene bg huang: 
        zoom 1.5

    # Increment the love level
    $ love += 1
    $ date_counter += 1
    show cs_guy:
        zoom 1.5

    # Display the date dialogue
    mc "Hey Brian! It’s great to meet you, excited to hang out with you!"
    cs_guy "Me too! I saw that your Hinge profile mentions that you’re a CS major! Talking about machine learning models really gets me going."

    # Display the food choice
    menu:
        "Look I know that we’re supposed to be on a date right now but I was hoping we could talk a bit more about my roommate Jim, who I know you went out on a date with.":
            cs_guy "Oh, I really liked Jim even though he wasn’t a CS major. Clearly, he wasn’t able to understand anything about my projects and any of my passions. Still, it was a shame to hear about the Lake Lag incident."
            menu: 
                "Where were you that night? Do you have any alibis or any evidence to back that up?":
                    cs_guy "I actually don’t but I was hanging out with my friend Brett before he said he had to go to Lake Lag for some Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa rush event."
                    cs_guy "After that, I was working by myself on one of my project’s – AlibiAI – code. That’s when the Jim murder happened, but I didn’t really take pictures of me coding or being in the room"
                    menu: 
                        "What rush event? Can you tell me more about Brett and Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa?":
                            cs_guy "Apparently the pledges were bringing potential dates to Lake Lag. That’s all I know. And Brett is a good friend of mine that I hang out with when I need to let loose after grinding on CS work and AlibiAI. But things have been weird lately, ever since he also started seeing Jim at the same time as me."
                            menu frat_guy_converge: 
                                "Oh that’s too bad. You’re probably a way better guy than Brett anyways, in my opinion, especially with what must be a cool project that you’re working on!":
                                    cs_guy "Oh, you’re too kind! But also you’re not wrong. Let me tell you more about AlibiAI. AlibiAI is an app that uses AI to help you create foolproof alibis using relevant details that you input."
                                    cs_guy "Brett was actually the one who really encouraged me to build it when I told him about it too. I can give you the access key to the beta demo if you want?"
                                    show card:
                                        xalign 0.5 yalign 0.4
                                    cs_guy "Oh shoot wrong card."
                                    cs_guy "Sorry I've got to head out really quick. Just remembered I have section. Bye!"
                                    jump middle
                                "Can I get Brett’s number?":
                                    cs_guy "Really? After what I just said about things being weird because of a mutual love interest? No, I won’t give you his number. In fact, I’m gonna have to ask you to leave."
                                    "Sorry for the trouble!"
                                    jump middle
                                "Can you tell me more about AlibiAI?":
                                    cs_guy "That’s a personal project that I’ve been working on ever since Andrew Ng told me that it would be a cool idea to look into. AlibiAI is an app that uses AI to help you create foolproof alibis using relevant details that you input."
                                    cs_guy "I personally thought it was a bit weird when he first told me about the idea, but I talked to my friend Brett about it, and he really strongly encouraged me to pursue it and implement it."
                                    menu more_alibi_ai: 
                                        "That sounds like a really cool project! It sounds like a very technically challenging engineering problem, so it’s so cool to see that you’re smart enough to tackle it.":
                                            cs_guy "Oh, you’re too kind! But also you’re not wrong. Let me tell you more about AlibiAI. AlibiAI is an app that uses AI to help you create foolproof alibis using relevant details that you input."
                                            cs_guy "Brett was actually the one who really encouraged me to build it when I told him about it too. I can give you the access key to the beta demo if you want?"
                                            show card:
                                                xalign 0.5 yalign 0.4
                                            cs_guy "Oh shoot wrong card."
                                            cs_guy "Sorry I've got to head out really quick. Just remembered I have section. Bye!"
                                            jump middle
                                        "Why did Brett encourage you so much to build AlibiAI?":
                                            cs_guy "Honestly, I’m not really sure why. But it did seem like it might be because he really wanted to use it for himself. But that’s all I’ll say. Anyways, I gotta get going. Gotta keep working on my project. See you later! "
                                            jump middle
                "What did you guys talk about? How did your date go with Jim?":
                    cs_guy "I tried explaining my projects to Jim, like for example my project AlibiAI, but he really didn’t understand what I was talking about. That’s when I knew that things between us weren’t going to work out."
                    cs_guy "Also, he was clearly more into my friend Brett and mentioned his name multiple times during our date. He even told me that they were supposed to meet up later somewhere. Since then, things between Brett and I have been a little weird, but I guess that’s not that important."
                    jump frat_guy_converge
        "Yes, I’d love to chat about your projects and what kind of research you’re doing! It’s so cool to connect with someone who is interested in the same things as me!":
            cs_guy "Oh yeah I would love to tell you all about the amazing things that I’ve been working on. It’s really setting me up for success for my Stanford CS PhD applications. I’m currently working in 2 labs! I’m working in Andrew Ng’s lab – which is super prestigious to get into – and I’m working on a personal project called AlibiAI."
            menu: 
                "Wow that's so cool! Can you tell me more about AlibiAI?":
                    cs_guy "That’s a personal project that I’ve been working on ever since Andrew Ng told me that it would be a cool idea to look into. AlibiAI is an app that uses AI to help you create foolproof alibis using relevant details that you input."
                    cs_guy "I personally thought it was a bit weird when he first told me about the idea, but I talked to my friend Brett about it, and he really strongly encouraged me to pursue it and implement it."
                    jump more_alibi_ai
                "I’d love to hear more about what you do outside of work though!":
                    cs_guy "Hmm let’s see…outside of work, sometimes I really need to let loose and I go hang out with some of my friends in Kappa Alpha Beta Delta Gamma Pi Sigma Mu Kappa."
                    cs_guy " I’m really close to Brett actually who is in the frat, and he was the one who strongly encouraged me to pursue implementing the tech for AlibiAI, the project I mentioned earlier. But things got a bit weird between us when I heard he was also seeing Jim."
                    jump frat_guy_converge

label start_up_date:
    scene bg coupa: 
        zoom 1.4

    # Increment the love level
    $ love += 1
    $ date_counter += 1
    show startup_girl:
        zoom 2

    # Display the date dialogue
    mc "Hey there! So, you're all about startups and entrepreneurship, huh? Changing the world one app at a time?"
    startup_girl "Absolutely! I'm like the Elon Musk of dorm room innovations. The next big thing is just a pitch deck away!"
    menu: 
        "Let’s get down to business. I know I called you here for a date, but I’m here to investigate the details of the murder of my roommate Jim, who I know you were seeing. Where were you on the night when Jim was murdered at Lake Lag?":
            label down_to_business:
                startup_girl " Ah, the night of that incident. I was sad to hear about that. Well, here's the deal, I was actually rocking the startup scene at an ultra-exclusive conference. Top secret stuff! "
                menu:
                    "Is there any way you can prove you were there? Any witnesses or photos?":
                        startup_girl "Oh, I wish! Unfortunately, this event was like a covert mission—invite-only, no social media allowed. It was so secretive, they had a password just to use the bathroom. What I can share though is what my new startup is currently working on, which is really exciting!"
                        menu: 
                            "Sigh…okay, what’s your startup idea?":
                                jump next_big_thing
                            "No, I don’t really care. What I really want to know is proof that you really were at this “conference” on that night.":
                                startup_girl " I swear, it’ll only take a second to pitch it to you! Okay, picture this —"
                                jump next_big_thing
                    "What was the conference for?": 
                        startup_girl "Oh, I wish I could tell you! Unfortunately, this event was like a covert mission—invite-only, no social media allowed. It was so secretive, they had a password just to use the bathroom. What I can share though is what my new startup is currently working on, which is really exciting!"         
                        menu: 
                            "Sigh…okay, what’s your startup idea?":
                                jump next_big_thing
                            "No, I don’t really care. What I really want to know is proof that you really were at this “conference” on that night.":
                                startup_girl " I swear, it’ll only take a second to pitch it to you! Okay, picture this —"
                                jump next_big_thing
                    "What kind of startup are you working on that you brought to the table there?":
                        jump next_big_thing

        "So what’s your next big thing?":
            show startup_girl flirty:
                zoom 1.5
            label next_big_thing:
                startup_girl "'AlibiAI' – the ultimate solution for concealing unsavory activities. It's a revolutionary app that helps you create foolproof alibis, no questions asked."
                startup_girl "AlibiAI is all about empowering individuals to control their narratives. It's not just for criminals, but for anyone who wants to maintain privacy, protect their reputation, or maybe even hide a harmless secret or two."

                menu :
                    "This sounds very suspicious…":
                        startup_girl "Yes I know about the recent murder…but this is completely unrelated to that, I swear. I’m only working on this because my colleague <CS nerdy guy> suggested the idea to me and wanted my help on the business side of things."
                        "{i}You remember that 'CS nerdy guy' was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                        menu: 
                            "CS nerdy guy? Can you tell me more about him?":
                                startup_girl "I honestly don't really know anything about the guy. I swear. Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"
                                jump middle
                            "CS nerdy guy? Are you aware that he was seeing Jim, the person who was murdered at Lake Lag recently?":
                                startup_girl "I honestly don't really know anything about the guy. I swear. Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"
                                jump middle

                    "How would this even work?":
                        startup_girl "Simple. Users would input relevant details about their desired alibi—time, location, circumstances—and AlibiAI's advanced algorithms would generate a meticulously crafted narrative, backed by seemingly authentic evidence."
                        startup_girl "We'd offer different package tiers, from basic cover-ups to deluxe setups that include tailored social media posts and forged documents. Unsure how the technology works - I’m on the business side of things, but you can email my colleague <CS nerdy guy> who came to me with the idea and wanted my help on the business side of things while he codes it."
                        "{i}You remember that 'CS nerdy guy' was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                        menu: 
                            "CS nerdy guy? Can you tell me more about him?":
                                startup_girl "I honestly don't really know anything about the guy. I swear."
                                startup_girl "Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"                                
                                jump middle
                            "CS nerdy guy? Are you aware that he was seeing Jim, the person who was murdered at Lake Lag recently?":
                                startup_girl "I honestly don't really know anything about the guy. I swear."
                                startup_girl "Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"                               
                                jump middle
                            "This sounds like a really cool idea! It’s honestly so impressive how you’re spearheading the business side of things!":
                                show card:
                                    xalign 0.5 yalign 0.4
                                startup_girl "Thanks so much! It’s cool to see that it seems like an exciting project to you too! Here, I gotta get going, but let me give you my business card so we can chat more later. Would love to grab a meal sometime!"
                                jump middle

                    "Is this your own original idea?":
                        startup_girl "I mean…depends on how you define “original”. It is my idea now too, since I’m working on the business side of things as the COO, but I will admit that my colleague <CS nerdy guy> did suggest the idea to me originally because he wanted my help."
                        "{i}You remember that 'CS nerdy guy' was also one of Jim's romantic interests that you thought of as a possible suspect.{/i}"
                        menu: 
                            "CS nerdy guy? Can you tell me more about him?":
                                startup_girl "I honestly don't really know anything about the guy. I swear."
                                startup_girl "Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"                                
                                jump middle
                            "CS nerdy guy? Are you aware that he was seeing Jim, the person who was murdered at Lake Lag recently?":
                                startup_girl "I honestly don't really know anything about the guy. I swear."
                                startup_girl "Anyways, something has come up unexpectedly so it looks like I'll have to leave. This was fun! Maybe we'll 'grab a meal' sometime. See ya!"
                                jump middle
                            "This sounds like a really cool idea! It’s honestly so impressive how you’re spearheading the business side of things!":
                                show card:
                                    xalign 0.5 yalign 0.4
                                startup_girl "Thanks so much! It’s cool to see that it seems like an exciting project to you too! Here, I gotta get going, but let me give you my business card so we can chat more later. Would love to grab a meal sometime!"
                                jump middle
        "Wow, you look like you’d be really good at rock climbing. Want to go with me some time?":
            startup_girl "Rock climbing! You know, I have a bit of a reputation in climbing circles. They call me the Spider. As much as I would love to though, I unfortunately won’t be able to. I’ve had my hands really full recently, so I really don’t have much free time these days. You know, other than for quick casual dates like this."
            menu:
                "What’s got you so busy?":
                    jump next_big_thing
                "I was making fun of you. I don’t even like rock climbing. What I really want to know is that you were doing on the night that my roommate Jim was murdered!":
                    jump down_to_business
        
    # Display the ending
    startup_girl "Thanks for a great date! Let's do it again sometime."
    jump middle

label police_segment:
    if date_counter < 3:
        "{i}Sorry you haven't been on all of the dates!{/i}"
        jump middle
    scene bg police: 
        zoom 1
    show police_officer:
        zoom 2
    
    police_officer "This is Stanford Police open up."
    mc "Woah, hi there. How can I help you?"
    police_officer "We’re just here to ask a few questions regarding the recent death of your roommate."
    police_officer "While we have no particular suspects, we need to start by asking if you knew anything that could help with the investigation of the murder. Is there anyone that you are aware of that your roommate interacted with prior to their death?"
    menu:
        mc "Yes! I know who did it! It was"
        "Brett":
            police_officer "Hm… interesting… Alright, we will go arrest him right away"
            scene bg black:
                zoom 10
            show frat_bro:
                zoom 1.5
            police_officer "THIS IS STANFORD POLICE! OPEN UP!"
            police_officer "YOU’RE UNDER ARREST FOR THE MURDER OF JIM!"
            frat_bro "Woah woah woah! Chill man! I didn’t do anything alright. What are you guys even talking about?!"
            police_officer "We know you’re lying! Get on the floor and put your hands behind your back!"
            frat_bro "NO! Wait, I really don’t know what’s happening! Can we all just chill the fuck out?! My boys are gonna be furious if they find out this has happened!"
            police_officer "Where you’re going no one will be FTB and you’ll be kept away from the boys for a long long time!"
            frat_bro "NO! NOT MY BOYS! I NEED MY BOYS! NOOOOOOO!!!!!!"
            jump correct_killer_identified
        "Brian":
            police_officer "Hm… interesting… Alright, we will go arrest him right away"
            scene bg black:
                zoom 10
            show cs_guy:
                zoom 1.5
            police_officer "THIS IS STANFORD POLICE! OPEN UP!"
            police_officer "YOU’RE UNDER ARREST FOR THE MURDER OF JIM!"
            cs_guy "What?! I don’t even know who that is?! What are you talking about?"
            police_officer "Of course you know! You murdered him!"
            cs_guy "How do I have time to think about murdering someone, much less having the time to actually do it, when I’m literally grinding 229, 140, and 110 at the same time?"
            police_officer "We don’t care what those numbers mean nor do we like to think about numbers! Get on the ground!"
            cs_guy "I swear you have the wrong person! No! I was just about to push my latest commit too and then submit the psets!!!! Just let me submit them first!!!!!!!!"
            jump wrong_murderer
        "Britneigh":
            police_officer "Hm… interesting… Alright, we will go arrest him right away"
            scene bg black:
                zoom 10
            show startup_girl:
                zoom 1.5
            police_officer "THIS IS STANFORD POLICE! OPEN UP!"
            police_officer "YOU’RE UNDER ARREST FOR THE MURDER OF JIM!"
            startup_girl "What?! I don’t even know who that is?! What are you talking about?"
            police_officer "Of course you know! You murdered him!"
            startup_girl "I’ve literally been meeting with 20 VCs a day!? How could I possibly enough care enough about anyone to not flake with them, much less carry out a murder?"
            police_officer "That’s exactly the type of cold heartless personality that would kill someone and hide it perfectly! Get on the ground!"
            startup_girl "I swear you have the wrong person! No! I was literally just about to grab coffee with Pearquoia Ventures and raise for my pre-pre Series F funding round! Please let me just circle back with them really quickly!"
            jump wrong_murderer
            
            




label correct_killer_identified:
    scene bg oval: 
        zoom 1.75
    "You caught the correct killer! Congrats!"
    return

label wrong_murderer:
    scene bg dorm: 
        zoom 3
    mc "Wow thank god, we finally caught the murderer. I’m glad that’s over with. "
    scene bg murder:
        zoom 4
    show anonymous_guy:
        zoom 2.5
    anonymous_guy "Sorry to do this to you, but I just can’t let you go free, especially when you know too much! I'm going to have to kill you!"
    "Oops! You identified the wrong murderer. Play the game again!"
    return