#!/usr/bin/python2
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : you-search.py
#
#* Purpose :
#
#* Creation Date : 16-02-2012
#
#* Last Modified : Sat 03 Mar 2012 11:03:54 PM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import mechanize
import cookielib
from re import search
from sys import argv





def main():
    if len(argv) == 1:
        print "Usage: %s search terms"%argv[0]
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
    page = br.submit()
    data = page.read()
    result = search('watch\?[=A-Za-z0-9]*?"', data)
    print "http://www.youtube.com/"+result.group(0)[:len(result.group(0))-1]

if __name__=="__main__":
    main()

