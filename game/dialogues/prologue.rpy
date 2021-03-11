label prologue:
    "Inner Thought 1"
    play music testMusic
    scene bgTest at truecenter
    with fade
    pause 2.0
    show imgKanae at left
    with dissolve
    show imgKuzuha at right
    with dissolve
    kanae "Dialogue 1"
    kuzuha "Dialogue 2"
    "Time for some choices"

label menu1:
    "There are 2 choices"
    menu:
        "Choice 1":
            jump choice1
        "Choice 2":
            jump choice2

label choice1:
    "You choose 1"
    jump endTest

label choice2:
    "You choose 2"
    jump endTest

label endTest:
    "Test End"
    return
