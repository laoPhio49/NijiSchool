# NijiSchool
> Name might change based on vote.

## What is this?
This is the repository for Visual Novel Project on 2021 which is started as one of the 3rd Debut Anniversary Projects for Kanae.\
This game is developed using Ren'Py engine.

## Directory (Folder)
> The Folder Structure of the game code
```
.
└── game
    ├── audio               # Dir for all the audios used in the game
        ├── background      # Dir for background audio
        └── effect          # Dir for effect audio
    ├── dialogues           # Dir for all dialogues and scenes
        ├── prologue.rpy    # The first interaction script from the Main script
        ├── sceneXX.rpy     # The script for XXth scene
        ├── menuXX.rpy      # The script for all choices for the XXth scene
        └── ending.rpy      # The script for the possible endings
    ├── gui                 # Dir for all the gui images
    ├── images              # Dir for all the non-gui images
        ├── background      # Dir for all background images
        └── characters      # Dir for all characters' images (possible with each character's folder)
    ├── properties          # Dir for scripts for the game properties
        ├── char.rpy        # Script to save character's headers (define statement with name color)
        ├── effect.rpy      # Script to save the effects if needed
        ├── image.rpy       # Script to save all the images' name in code
        └── variables.rpy   # Script to define all the variables
    ├── tl                  # Dir for languages translate files
        ├── japanese        # Dir to save all the translation for the scripted dialogues for the japanese language
        └── None            # Dir to save all the translation for the scripted dialogues for the default language (English)
    └── script.rpy          # The Main of the script
```

## Github Direction
***Please use Pull Request Mechanism to merge to main branch.***\
The most suggested way to use github is to make your own one dev branch, or to use multiple branches for multiple purposes.\
The branch name for consistency : `<devName>/<purpose>` \
The branch name can be in any alpha-numberical case.\
```
Example: 
- saifu/dev
- saifu/setTemplate
```

## Miscellaneous Informations
- How to delete save file = Hover to the save file and hit delete on keyboard