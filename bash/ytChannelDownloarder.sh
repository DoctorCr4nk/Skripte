#!/bin/bash
## Author:       Alexander Mueller
## Email:        amueller@doctorcrank.de
## Version:      1.1
## Date:         2022-10-27
## Comment:
## Description:  for loop to download youtube channels

channels_mr2="https://www.youtube.com/channel/UCP9OdCtr2q13Gnj-F3uGOcw
https://www.youtube.com/c/ErikSeastead1
https://www.youtube.com/user/heeltoemotorsport
https://www.youtube.com/channel/UCGFuHwWoJZw3em6pHVghHcw
https://www.youtube.com/c/PlaneTMRS
https://www.youtube.com/c/StavTech"

channels_mr2_others="https://www.youtube.com/c/GearsandGasoline
https://www.youtube.com/c/SpyderLEE
https://www.youtube.com/c/StarkReality
https://www.youtube.com/channel/UCqumOv9F_sjdyQr_judN-pQ"

channels_important="https://www.youtube.com/user/AsterEntertainment
https://www.youtube.com/channel/UC1W9Lh96xoDvGvpL81jqeCQ
https://www.youtube.com/channel/UCMbTsFkvIu2w1PqeVhXaZ2g
https://www.youtube.com/c/LucyEllis
https://www.youtube.com/c/WesleyKagan"

channels_entertainment="https://www.youtube.com/c/chrisfix
https://www.youtube.com/c/ClarityCoders
https://www.youtube.com/c/colinfurze
https://www.youtube.com/c/JaymeEdwardsMedia
https://www.youtube.com/c/kondensatorschaden
https://www.youtube.com/c/Matthiaswandel
https://www.youtube.com/channel/UCarhVHQDU63divhaYPScVnQ
https://www.youtube.com/channel/UCAL3JXZSzSm8AlZyD3nQdBA
https://www.youtube.com/c/RcLifeOn
https://www.youtube.com/c/rctestflight
https://www.youtube.com/c/TechIngredients
https://www.youtube.com/c/TheBackyardScientist
https://www.youtube.com/channel/UCMZkAT1Vf7CPSNcTzZkK_qQ
https://www.youtube.com/user/frezibln"

for channel in ${channels_mr2_others} "https://www.youtube.com/channel/UC5zKNgrnghGLAdUwT9SD7Dg"
do
    echo "${channel}" | tee --append "/mnt/share/Videos/Youtube/log"
    yt-dlp --output '/mnt/share/Videos/Youtube/%(channel)s/%(release_date)s_%(title)s' --no-overwrites --write-description --write-info-json "${channel}" | tee --append "/mnt/share/Videos/Youtube/log"
done

#for video in "https://www.youtube.com/watch?v=gNi_6U5Pm_o" "https://www.youtube.com/watch?v=R9gXtvSyTzA" ; do youtube-dl -x --audio-format mp3 "${video}" & done
