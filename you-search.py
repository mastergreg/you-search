#!/usr/bin/python2
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#* File Name : you-search.py
#* Purpose : search youtube page for video
#* Creation Date : 16-02-2012
#* Last Modified : Sun 07 Oct 2012 06:03:21 PM EEST
#* Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

import mechanize
import cookielib
from sys import argv

def main():
    if len(argv) == 1:
        print "Usage: %s <search terms>"%argv[0]
        exit(1)
    URL="http://youtube.com"

    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.set_handle_robots(False)
    br.open(URL)

    br.select_form( nr = 1 ) 
    br["search_query"] = " ".join(argv[1:])
    br.submit()
    links = br.links( url_regex="/watch\?v=" )
    for (i,link) in enumerate(links):
        print "http://www.youtube.com"+link.url
        break

if __name__=="__main__":
    main()

