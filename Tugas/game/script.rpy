
image chika_frown:
   "Aiko_WinterUni_Frown.png"
   yalign -0.3

image chika_smile:
    "Aiko_WinterUni_Smile.png"
    yalign -0.3

image chika_shout:
    "Aiko_WinterUni_Shout.png"
    yalign -0.3

image sou_frown:
   "Sora_WinterUni_Frown.png"
   yalign -0.3

image sou_smile:
    "Sora_WinterUni_Smile.png"
    yalign -0.3

image sou_open:
    "Sora_WinterUni_Open.png"
    yalign -0.3

image yui_frown:
   "Miho_WinterUni_Frown.png"
   xalign 0.5
   yalign -0.3
   zoom 0.28

image yui_smile:
    "Miho_WinterUni_Smile.png"
    xalign 0.5
    yalign -0.3
    zoom 0.28

image yui_open:
    "Miho_WinterUni_Open.png"
    xalign 0.5
    yalign -0.3
    zoom 0.28

image classroom = "kelas.jpg"
image mybedroom = "kamar_mc.png"
image outclass = "luar_kelas.jpg"
image outdoor = "luar_sekolah.jpg"
image school_field = "halaman_sekolah.jpg"
image canteen = "canteen.jpg"

define c = Character(None, kind=nvl,
        window_left_padding = 80,
        window_right_padding = 80, what_prefix="Chika: \"",
                     what_suffix="\"")

define s = Character(None, kind=nvl,
        window_left_padding = 80,
        window_right_padding = 80, what_prefix="Sou: \"",
                     what_suffix="\"")

define y = Character(None, kind=nvl,
        window_left_padding = 80,
        window_right_padding = 80, what_prefix="Yui: \"",
                     what_suffix="\"")

define me = Character(None, kind=nvl,
        window_left_padding = 80,
        window_right_padding = 80, what_prefix="Me: \"",
                     what_suffix="\"")

define tc = Character(None, kind=nvl,
        window_left_padding = 80,
        window_right_padding = 80, what_prefix="Teacher: \"",
                     what_suffix="\"")

define ev = Character(None, kind=nvl,
        window_left_padding = 80,
        window_right_padding = 80, what_prefix="Everyone: \"",
                     what_suffix="\"")

define narrator = Character(None, kind=nvl,
        window_left_padding = 80,
        window_right_padding = 80 )

define menu = nvl_menu
label start:


    scene black with Fade(0, 3.0, 1)
    play music "audio/mainbgm.mp3"
    scene mybedroom with dissolve:
        zoom 1.5

    "My name is Ron, a student from Koukou Highschool."

    "Today is Monday, and today is a school day."

    "I woke up at 6:25, and arrived at school 30 minutes later."

    nvl clear

    scene classroom with dissolve

    "After entering the class, a familiar voice called me."

    "\"Morning, Ron!\""

    "I gazed to the source of the voice and replied to the greeting as I walked to my seat."

    show sou_smile with dissolve

    me "Mornin'."

    "He's Sou, my friend since god-knows-when."

    s "Hey Ron, done your homework yet?"

    me "Yeah, it wasn't that hard after I tried it."

    s "Nice."

    "Then, someone came near our desks."

    nvl clear
    hide sou_smile with dissolve

    show chika_smile with dissolve:
        xalign 1

    show sou_frown with dissolve

    c "Morning Ron. Thanks for the book you lent me before. Here's the book."

    me "Ah, OK. Thanks Chika."

    hide chika_smile with dissolve

    "After she gave me the book, she then went back to her seat."

    hide sou_frown
    show sou_smile

    s "Yo.. what book did you lent her?"

    me "Maths, she asked me two days before."

    s "I see."

    play sound "audio/bell.mp3"

    "After a short delay, the bell started to ring."

    nvl clear
    hide sou_smile with dissolve

    "The teacher for the first lesson today has come."

    me "Wait a minute..."

    "After I saw the teacher, I realized that the teacher is a new substitute teacher."

    "After knowing that fact, I decided to..."

    menu:
        "Sleep":
            "I was still feeling sleepy, then I quickly fell asleep."

        "Stay awake":
            jump ed1


    nvl clear

    scene classroom with Fade(0.5, 0.2, 0)
    scene black

    "Clearly, as I fell asleep, I felt this day was going to be like other days."

    "But today is different."

    "Because of the noise, I woke up."

    nvl clear

    me "Hnngh..."

    tc "Amasuji Ron!"

    "Still feeling the dizziness after waking up, I didn't realize I was being called"

    tc "I repeat, Amasuji Ron!"

    nvl clear
    scene classroom with dissolve

    "I finally fully awake after a moment."

    me "Ah yes, present sir!"

    tc "What were you doing?"

    "I didn't answer."

    tc "It's my first time here teaching and I already got a student like this..."

    tc "Amasuji, now please step out from this class as a punishment!"

    me "Shoot.."

    "I got up and walked out from the class."

    nvl clear
    scene outclass with dissolve

    me "What the hell with that teacher?"

    "I kicked the air near the floor, venting my anger a bit."

    "Then I calmed down and sighed."

    me "Huft... I can't believe it started like this."

    me "Dang it that teacher, now what should I do?"

    "Shortly after, another friend of mine approached me."

    nvl clear

    show yui_smile with dissolve

    y "Hey, why are you outside Ron?"

    me "Punishment, I got punished by the new teacher."

    show yui_open

    y "Haha, what the hell was that?"

    me "Eh, shut up Yui."

    hide yui_open

    show yui_smile

    y "Seriously, how come you got punished?"

    me "I fell asleep."

    y "Classic Ron, you were always lucky. Who was that new teacher by the way?"

    me "Dunno, I don't know his name."

    nvl clear

    me "By the way, what're you doing outside?"

    y "You wanna know?"

    me "Of course, why would I ask then?"

    y "OK then, follow me."

    me "Huh.. alright."

    "I went and followed Yui."

    nvl clear
    hide yui_smile
    scene outdoor with dissolve

    "After 5 minutes walking, we arrived near the gate."

    show yui_smile with dissolve

    me "What are we doing here?"

    y "Come, hide behind this tree."

    me "Why?"

    stop music fadeout 1.0

    show yui_frown

    y "Just come here quick."

    "I hid behind the tree near Yui."

    y "Look to the gate."

    "After hearing what Yui said, I looked to the gate."

    nvl clear

    me "Who's that?"

    y "You probably don't know, he's a goddamn school shooter."

    play music "audio/reveal.mp3"

    me "What the fuck?"

    y "No kidding, in his bag is a gun, he's going to act up in this school."

    me "Hold up, how do you know this?"

    y "It's not important, what's important now is how we stop him."

    me "Stop him? What.. how?"

    y "I already have a plan in mind, and now because you're here, this should be easier."

    me "Why don't we just run away?"

    y "You want your friends to be shot?"

    me "Of course no..."

    y "Then, follow my plan. Come."

    "I felt my heartbeat increasing, knowing the fact there's a school shooter entering this school."

    "I then followed Yui, trusting her plan."

    hide yui_frown
    nvl clear

    scene school_field with dissolve

    "The suspected shooter entered the school field, we followed him from behind maintaining a safe range to not be detected by him."

    "Suddenly, the shooter stopped walking."

    y "Quick! Hide!"

    "Both of us quickly hid."

    "I took a peek to see what the shooter is doing."

    "He was looking behind for a while, and he then reached out to his backpack."

    "He grabbed something resembling a gun, and continue walking inside."

    me "The fuck, was that a gun?"

    show yui_frown with dissolve

    y "I think, lets follow him again."

    hide yui_frown with dissolve

    "We then followed him again while maintaining a safe range like before."

    "After a while, the shooter then entered the canteen."

    nvl clear

    scene canteen with dissolve

    "The canteen is mysteriously quite, even though it's still morning, there should be a canteen employee here."

    me "Yui, how do the shooter know the canteen's empty?"

    show yui_frown with dissolve

    y "I don't know... this shooter must be someone from this school, or someone with immense luck."

    me "Damn."

    hide yui_frown with dissolve

    "We continued to follow him for a while."

    "And then, he finally arrived in front of my class."

    nvl clear

    scene outclass with dissolve

    me "Yui! This is my fucking class! He's going to shoot everyone inside!"

    "Yui stayed silent, and she kept watching the shooter's movement."

    "Seeing Yui keeping her mouth shut, I shut up my mouth."

    "The shooter opened his backpack and put his \"gun\" back."

    me "Yui! He put the gun back inside his backpack!"

    show yui_frown with dissolve

    y "Wait for him to enter the class, then rush him."

    me "What the hell? Why?!"

    y "It's the only way, trust me."

    me "What if I failed? I would be dead!."

    y "You won't! Just trust me!."

    hide yui_frown with dissolve

    nvl clear

    me "Shit... this is getting ridiculous."

    "Like Yui had planned, the shooter then entered the class slowly."

    "My body is getting hotter, and I feel a bit dizzy."

    y "Ron, now's the chance!"

    "After I heard what Yui said, I then decided to..."

    menu:
        "RUSH THE SHOOTER":
            jump ed3

        "Stay here":
            jump ed21

    return

label ed1:

    "Despite my sleepiness, I decided to take out my books and listened to the teacher's introduction."

    stop music fadeout 1.0
    "Just another day of school, nothing special."

    scene classroom with Fade(0.5, 0.2, 0)
    scene black

    return

label ed21:
    "I stayed still."

    y "Ron! It's now or never! Rush him!"

    "Yui told me to go, and now I am going to..."

    menu:
        "RUSH THE SHOOTER":
            jump ed3

        "Stay here, again":
            jump ed2

    return

label ed2:
    nvl clear

    me "Ugh..."

    "My heartbeat increases again, and this time I felt more dizzy than before."

    "Whether it's bad luck or not, my body felt really heavy and my head really light."

    "I sweat so much."

    "Then I fainted."

    y "Huh? Ron?!"

    "The last thing I saw is the ceiling and Yui's worried face."

    "The shooter will find me, fast or slow, and I'm going to die not being able to save my friends."

    stop music fadeout 1.0

    "What a sad end for me."

    scene outclass with Fade(0.5, 0.2, 0)
    scene black

    return

label ed3:
    nvl clear

    "I collected all the courage I needed, then took a deep breath."

    me "OK... I'm going."

    y "Good luck, Ron."

    "I walked step-by-step, slowly, and not making any loud sounds."

    "Because of my adrenaline, I opened the door and rushed in quickly."

    nvl clear

    scene classroom with dissolve
    stop music fadeout 1.0

    "But what I'm seeing is not what I expected."

    me "Huh?"

    play sound "audio/hbd_sfx.mp3"
    show sou_open with dissolve

    show chika_shout with dissolve:
        xalign 1.0

    ev "Happy birthday, Ron!"

    me "HUH??!!!"

    "Then, Yui also entered the classroom."

    show yui_open with dissolve:
        xalign 0

    y "Happy birthday Ron!"

    nvl clear

    hide yui_open
    hide sou_open
    hide chika_shout

    show sou_smile with dissolve:
        xalign 0
    show chika_smile with dissolve:
        xalign 1.0
    show yui_smile with dissolve

    "I got really confused and can't think straight after what all happened."

    stop sound

    play music "audio/relaxed.mp3"

    y "Hey Ron! It was all just a prank, we're all going to celebrate your birthday."

    s "Yeah, it was Chika who created this plan, a genius isn't she?"

    me "A goddamn genius."

    c "Hahaha, by the way, we all gave you a present, check your desk."

    "I then walked to my desk, just to see my desk is full of presents."

    me "Thanks, guys. Even though this is a bit crazy, I appreciate you all."

    ev "No problem!"

    tc "Alright now, party's over! Let's continue to the lesson."

    tc "Don't fall asleep again, Ron!"

    me "Yes sir."

    hide sou_smile with dissolve
    hide chika_smile with dissolve
    hide yui_smile with dissolve

    nvl clear

    "Everyone went to their desk, and so am I."

    "I put away all the presents to the floor, and prepared my lesson book."

    "I kept thinking, what a crazy day is today."

    me "At least, the shooter's ain't real."

    "I took a deep breath, then followed the lesson."

    stop music fadeout 1.0

    scene classroom with Fade(0.5, 0.2, 0)
    scene black

    return
