---
image:
    svg: 1280, 720, 1c1d22
title:
    text: 10, 10, EEE, 20px
description:
    text: 77, 190, EEE, 10px
aitable:
    html: 10, 200, 700, 500
    text: 20, 200, EEE, 20px, bold
    style: AITable.css
neuroprojects: 
    html: TBD
    text: TBD
    style: TBD
programming:
    html: 10, 78, 170, 70
    source: programming.html
    style: programming.css
---


Metadata type is either:
-   svg: W, H, color
-   text: X, Y, color, font-size (optional: font-weight)
-   html: X, Y, W, H
-   source: file-source (should be impled as override)
-   style: file-source

section names will be converted to lowercase


programing has no editable properties from here


!!! title ""
    Hello and welcome to the #programing channel!!!1!
    bc u are asking here, here are some things to note!


!!! description ""
    The Programming chat, despite it's name is the general tech channel.
    The channel description sums it up best; But another word phrase is:
    If your called a nerd or need the help of nerds. You are in the correct place.


!!! aitable "Recommended Models to build stuff:"
    | Parts:      | "Just Works"                                                                   | "Custom"                                                                                                                 |
    |-------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
    | - Voice     | Whisper for vocal transcribing other people's voices                           | For Vocal input, you can grab an LLM with audio input (source)                                                           |
    |             | ??? for TTS, Applio for RVC, search for RVC voices on a site like silly tavern | No way that I'm aware of to train such.                                                                                  |
    |             |                                                                                | For Vocal output, some LLMs do such but still need an RVC step. Applio is what is recommended for such.                  |
    | - LLM       | **TODO!** Ask around for rec based on VRAM, maybe 6GB, 12GB, 24GB              | **TODO!** Same as left, but some finetuning advice.                                                                      |
    |             | CPU (step 1 is getting a GPU)                                                  | Unless you rent out a H100 cluster, TBs of raw data AND can outskill entire teams of AI research. Then finetune a model. |
    | - Vision    | **TODO!** Ask on this one                                                      | **TODO!** Ask on this side as well                                                                                       |
    |             |                                                                                | Some object detection is possible to train sepratly, Better off grabbing an existing object detection model.             |
    |             |                                                                                | having your LLM include vision is also an option.                                                                        |
    | - Memory    | **TODO!** Best we got is some sort of RAG.                                     | Intergrate some flavor of RAG into your LLM model. However you do so.                                                    |
    |             | Maybe memgpt or similar, I got no idea on this one.                            | Long term, some database for memories.                                                                                   |
    | - API       | **TODO!** You really, really think this just exists? xdx                       | Not an AI question; check if a general project exists or hit the docs                                                    |
    | - All of it | NOmegalul (replace with image of N+neuromegealul)                              | All of the above at least, but that is just getting the persona.                                                         |
    |             |                                                                                | No one can help you beyond here, so don't bother asking.                                                                 |
    |             |                                                                                | Even if they could, there is no reason at all for them to help you.                                                      |
    |             |                                                                                | Why would they help **you**?                                                                                             |


!!! neuroprojects "I want X part of Neuro/Evil:"
    | Parts:  | Recreation                                                                                                                     |
    |---------|--------------------------------------------------------------------------------------------------------------------------------|
    | = Voice | Hello SuperBox :neurowave:                                                                                                     |
    | - API   | [Neuro SDK](https://github.com/VedalAI/neuro-game-sdk) is a offical project to allow for modding games for Neuro/Evil to play. |
