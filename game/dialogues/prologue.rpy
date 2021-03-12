label prologue:
    jump test

label test:
    "This is the start of font test"
    "Try out the {font=font/font_1_honokamarugo_1.1.ttf} honoka marugo {/font} in a sentence."
    "{font=font/font_1_honokamarugo_1.1.ttf}Kanae is a baby. Babu babu{/font}"

    "Try out the {font=font/KosugiMaru-Regular.ttf} Kosugi Maru Regular {/font} in a sentence."
    "{font=font/KosugiMaru-Regular.ttf}Kanae is a baby. Babu babu{/font}"
    "Try out the {font=font/KTEGAKI.ttf} {size=+10} KTEGAKI {/size} {/font} in a sentence."
    "{font=font/KTEGAKI.ttf} {size=+10}Kanae is a baby. Babu babu{/size}{/font}"

    "Try out the {font=font/rounded-mgenplus-1m-medium.ttf} rounded-mgenplus-1m-medium {/font} in a sentence."
    "{font=font/rounded-mgenplus-1m-medium.ttf}Kanae is a baby. Babu babu{/font}"

    "Inner Thought 1 [testList[2]]\nstart-[testListStr[1]]\nstart"
    play music testMusic
    scene bgTest at truecenter
    with fade
    pause 2.0
    show imgKanae at left
    with dissolve
    show imgKuzuha at right
    with dissolve
    $ testList[2] = 10
    kanae "Dialogue 1 [testList[2]]"
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
