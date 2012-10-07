#!/bin/sh
youtube_url=$(you-search.py $*)
#echo $youtube_url
#!/bin/sh
#
# Public domain
# Author: roman [] tsisyk.com
#
# Usage: ./me url [youtube-dl parameters]
#

COOKIE_FILE=/var/tmp/youtube-dl-cookies.txt
mplayer -vo null -cookies -cookies-file ${COOKIE_FILE} $(youtube-dl -g --cookies ${COOKIE_FILE} ${youtube_url})
