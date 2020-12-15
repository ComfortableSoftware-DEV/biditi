#!/usr/bin/python
# v01.01.0001


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# import globally
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

from datetime import datetime as DT
from os import path as PATH
import pickle as PD
import PySimpleGUI as SG

# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# setting constants
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

MAINDOWNCOLOR = "#880000"
MAINDOWNTEXTCOLOR = "#FF0000"
MAINUPCOLOR = "#008800"
MAINUPTEXTCOLOR = "#00FF00"
GRAY8 = "#888888"
GRAYC = "#CCCCCC"
PURP440022 = "#440022"
PURP660044 = "#660044"
YELLOW666600 = "#666600"
GREEN2 = "#448811"
BLACK = "#000000"
ORANGE = "#FF7F00"
YELLOW2 = "#444422"
TEAL1 = "#00FF7F"

ADJBTNDOWNCOLOR = MAINDOWNCOLOR
ADJBTNDOWNTEXTCOLOR = MAINDOWNTEXTCOLOR
ADJBTNUPCOLOR = MAINUPCOLOR
ADJBTNUPTEXTCOLOR = MAINUPTEXTCOLOR
ADJTIMEDOWNBKGNDCOLOR = MAINDOWNCOLOR
ADJTIMEFONTSZ = 9
ADJTIMETXTCOLOR = GRAYC
ADJTIMEUPBKGNDCOLOR = MAINUPCOLOR
BTNDOWNCOLOR = MAINDOWNCOLOR
BTNDOWNTEXTCOLOR = MAINDOWNTEXTCOLOR
BTNFONTSZ = 12
BTNQUITCOLOR = PURP440022
BTNQUITTEXTCOLOR = PURP660044
BTNTASKDOWNCOLOR = MAINDOWNCOLOR
BTNTASKDOWNTEXTCOLOR = MAINDOWNTEXTCOLOR
BTNTASKUPCOLOR = MAINUPCOLOR
BTNTASKUPTEXTCOLOR = MAINUPTEXTCOLOR
BTNUPCOLOR = MAINUPCOLOR
BTNUPTEXTCOLOR = MAINUPTEXTCOLOR
BTNZEROCOLOR = PURP440022
BTNZEROTEXTCOLOR = YELLOW666600
COUNTERFONTSZ = 20
FONT = "Source Code Pro"
LABELFONTSZ = 12
LASTFILENAME = "biditi.last"
MODE_NORMAL = "MODE_NORMAL"
MODE_RESTART = "MODE_RESTART"
MODE_START = "MODE_START"
MYFACTOR = 10
MYSCALE = 100
SETTIMERFONTSZ = 20
SPACECOLOR = GRAY8
SPACEFONTSZ = 10
SPINBKGNDCOLOR = TEAL1
SPINFONTSZ = 10
SPINSIZE = (10, 1)
SPINTEXTCOLOR = ORANGE
STOPMODE_BUTTON = "STOPMODE_BUTTON"
STOPMODE_CYCLE = "STOPMODE_CYCLE"
TASKCOUNTERCOLOR = GREEN2
TIMERDOWNBKGNDCOLOR = MAINDOWNCOLOR
TIMERDOWNTEXTCOLOR = MAINDOWNTEXTCOLOR
TIMERFONTSZ = 60
TIMEROFFBKGNDCOLOR = BLACK
TIMEROFFTXTCOLOR = YELLOW2
TIMERUPBKGNDCOLOR = MAINUPCOLOR
TIMERUPTEXTCOLOR = MAINUPTEXTCOLOR

AIR = "AIR"
DYNAVAP = "DYNAVAP"
FIREFLY = "FIREFLY"
Q = "Q"
QOMO = "QOMO"
VARIOUS = "VARIOUS"

TASKLIST = [
	AIR,
	DYNAVAP,
	FIREFLY,
	Q,
	QOMO,
	VARIOUS,
]

# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# up and down buttons in various sizes, and base 64 encoded for ease of use
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


UP16 = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAADB3pUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHjazZVdstsgDIXfWUWXgCSEYDmYn5nuoMvvAfvmtrdJE6d+KEyMBwQc9B0c1398H+4bCmXyLqilmGP0KCGHzAUvyX+WfrR7H/mwnh+Fjie5uwOMVtDK3mnhGJWj/yM+3losdGeA9MsEuW3Dv25s5ehnz78pGnrb4/M4x2+Mlsbo++lKiEhD3A+1b+E+lkHghizJmhZRDT/Fu62aUZMvvlLwzVe/oVYkmUn8oEDNUaFBnRraShUaA3c2tMyVZfUlMc5cxQtJmJUGm2RpkoSlcheR4IRvWmjtm9d+lRJ2boRQJixGmPLX6p4FvFLHqB45IsLp6cgVdDFPDjTTKPOJMAChcXDTleCPeivuF7ACgrrSnHDA4rd9iU3p01uyDCCIU7S7v8japMbLJQF7K8SQAIGPJEqRvDEbURBOAFSgnCXwBgKkyg0iOYhEsEnwEfbGHKMVy8p7P64K+KhEMbDJUgArBIV/LCR4qKhoUNWopkmzFhclhqgxRovzzhUTC6YWzSxZtpIkhaQpJksp5VQyZ8GV1Byz5ZRzLgV7luCKFswuiChl4022sOkWN9vSlrdSYZ8aqtZYraaaa2ncpIWmLTZrqeVWOnVYyfXQtcduPfXcy4DXhowwdMRhI408yo3aQfWPeoIaHdR4kZpxdqOGXrO50FqC5ndGJzMQ40AgbpMADM2TmU8UAk9yk5nPjFuhDJE62TTyxVEEwtCJddCN3Se5l7k55PoZN36FnJvoLiDHrssXbneotfklrIvYfgtnTr3g9mG8p8KpINm8v7zcDuhfr6M2P2o6BtxctcR9pHEdzerZpVfrzk54pMmtkQs0uSvyMwPcl8i3tblrmOGu/RH5piZ3RX4OHz2ceUqbu4bZ4aMrNLkr8nPHR+9rc9cwu+OjdzW5K/LzxEfntLlrmD3x0RlN7or8nPDRc23uiflf1uTe1fJVk3to+hP5edNHDxd6aP5Tmty/a/F/+YM8mZ8LfPT/LjTg7AxX/gQaxLaLAaEVugAAAYRpQ0NQSUNDIHByb2ZpbGUAAHicfZE9SMNAHMVfU6WiFQcLijgErE4WREUctQpFqBBqhVYdTC79EJo0JCkujoJrwcGPxaqDi7OuDq6CIPgB4uTopOgiJf4vKbSI8eC4H+/uPe7eAUKtxDSrbQzQdNtMJeJiJrsihl4RRhf6MISQzCxjVpKS8B1f9wjw9S7Gs/zP/Tm61ZzFgIBIPMMM0yZeJ57atA3O+8QRVpRV4nPiUZMuSPzIdcXjN84FlwWeGTHTqTniCLFYaGGlhVnR1IgniaOqplO+kPFY5bzFWStVWOOe/IXhnL68xHWag0hgAYuQIEJBBRsowUaMVp0UCynaj/v4B1y/RC6FXBtg5JhHGRpk1w/+B7+7tfIT415SOA60vzjOxzAQ2gXqVcf5Pnac+gkQfAau9Ka/XAOmP0mvNrXoEdCzDVxcNzVlD7jcAfqfDNmUXSlIU8jngfcz+qYs0HsLdK56vTX2cfoApKmr5A1wcAiMFCh7zefdHa29/Xum0d8PRltyldQcsX8AAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfkDAsXMR8BzCaGAAAAKHRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QIGJ5IEdhZWxpY0dyaW1ld9KrjgAAAElJREFUOMtjYMAH/kMhHsDEQCFgxGs7qkpGOroAl7+xuIIGLiAQ6uiuoLILCNmOxRVUdAGxtqO5gkouINV2JFdQwQXk2k6tWAAAfOMSEjTpcNIAAAAASUVORK5CYII='
DN16 = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAC13pUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHja1ZZtchshDIb/c4oeAUkIwXFYPmZ6gx6/L7vrtet6YqdOUgeNF4cF6UWPIHb918/hfqBRyskFtRRzjB4t5JC54Evy59b3fhsjH9bnqdH+JHfzBaMX9LINWtjfyj5+mh+PHo5uvCC9WiBHGL4MbGUfZ89/KOr5iHHezv4Zo6Ux+ra7EiLSELdNbSHcyQ0mLsiSrMsizPBRfLfVMiz54isF33z1C6xSJibxgwI1R4UGdWroK1VoDNzZ0DNXlnUsiXHmKl5IwjQabJKlSRKWyl1EghM+tNAaN6/xKiVEboSpTHBGWPKmuXsTHrExqkeOiLB72nMFXcyTA800ynxiGoDQ2LnpmuCTHc1dgBUQ1DXNCRssftlcLErn2pK1AATzFP1WX2RtUuO1SgJiK8SQAIGPJEqRvDEbURBOAFSgnCXwAgKkyg0iOYhEsEmoI8TGGqN1Litv4zgq4KMSxcAmSwGsEBT1YyGhhoqKBlWNapo0a3FRYogaY7Q4z1wxsWBq0cySZStJUkiaYrKUcDZL5iw4kppjtpxyzqUgZgmuaMHqghmlLLzIEhZd4mJLWvJSKsqnhqo1Vqup5loaN2mhaYvNWmq5lU4dpeR66Npjt5567mWg1oaMMHTEYSONPMpBbaf6l72DGu3UeCU159lBDaNm09HqguY9o5MZiHEgELdJAAXNk5lPFAJPcpOZz4xToQyROtk08sVRBMLQiXXQwe5M7mFuDrm+x40fIecmug8gx67LFbcb1Nq8CetKbDuFM6decPoAPhVOZWSXZRhyxfNv/0TvnnXwnxxJrXsuwHj4jluW99ycUvNFiq6VHOMvp+iGsk+uo3tKXlfRhTJ3jfFjFL1XyesqOhzdKPl/U/SEkldX9Mb18OjF555V8l0UvVfZBST3rJLvpuieshsF/FX/jj5LkeC3UsYPz98iX6IbCeIDbAAAAYRpQ0NQSUNDIHByb2ZpbGUAAHicfZE9SMNAHMVfU6WiFQcLijgErE4WREUctQpFqBBqhVYdTC79EJo0JCkujoJrwcGPxaqDi7OuDq6CIPgB4uTopOgiJf4vKbSI8eC4H+/uPe7eAUKtxDSrbQzQdNtMJeJiJrsihl4RRhf6MISQzCxjVpKS8B1f9wjw9S7Gs/zP/Tm61ZzFgIBIPMMM0yZeJ57atA3O+8QRVpRV4nPiUZMuSPzIdcXjN84FlwWeGTHTqTniCLFYaGGlhVnR1IgniaOqplO+kPFY5bzFWStVWOOe/IXhnL68xHWag0hgAYuQIEJBBRsowUaMVp0UCynaj/v4B1y/RC6FXBtg5JhHGRpk1w/+B7+7tfIT415SOA60vzjOxzAQ2gXqVcf5Pnac+gkQfAau9Ka/XAOmP0mvNrXoEdCzDVxcNzVlD7jcAfqfDNmUXSlIU8jngfcz+qYs0HsLdK56vTX2cfoApKmr5A1wcAiMFCh7zefdHa29/Xum0d8PRltyldQcsX8AAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfkDAsXMQ8cezbiAAAAKHRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QIGJ5IEdhZWxpY0dyaW1ld9KrjgAAAE5JREFUOMu10TsOgEAMA9EZ7n/n0GyB0LK/BNe29CQbECRykYwApwrBGsGJwratE+wofOxqBSsKX5t6wUhhp/+PoKfwo5sWDBMQs1fSght0IRISVNQe5AAAAABJRU5ErkJggg=='
UP32 = b'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'
DN32 = b'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'
UP96 = b'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'
DN96 = b'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'
DN64 = b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAKLHpUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHjarVlZduu4DvznKnoJJEEQ5HLA6Zy3g7f8LlCyk3jItX3bSkRFpjiggEJBcfP//1vuH3yoVu8SS8k1Z49PqqlGxUXxX595tse94NM+Xz7hPAf38IuIltDScVPS+S2d9y/987XFQA++CHzzAF2nid8nFj3vRx9/rChkv/z3T/n6XWuUteaxO00ZZsjHpo5H3WUYdGywEu3HMg7BL+Na9lFxFK++h+SH777h6KGGGMivkMJwQcMKMwy0PXSsMcUZBW2MPdK+V0hijZ08BUp2hBWFKg0qFKnHSUTJUbyuJex5656vh4KZR0DXGDBYwCO/Hu5PHV451uoeNgoBuw+nrbCuGA2HYGYkO6MbAAnrxI23gS/H9eO+AUtAkLeZCzaovh1DNA5fvkXbAQj9GO3hX0GGoRa3lyTMzVhMIEDgcyAOOXiJUUJIFAsAUqw8UooNCATmOLDImIgysCnwI8yNZyTsvpHjcR+hAnyYMgmwqaQAKyWG/0gq8CFl4sTMmYULV1aXKafMOWfJFnMqJElYsogUqaKFSipccpFSSi1aYyWEJNdcpZZaqyrm1OSUFU8reqi22Kilxi03aaXVph3u01Pnnrv00mvXEQeNNHjkIaOMOnSGCVdyM02eecoss05d8LVFKy1eeckqqy69onaiene8gVo4UYsbKesnV9RwV8QG2kME4xk2zIBYTAGIiyEAh46GmS8hpWjIGWa+RkQFRyySDZsRvLqQAWGaIfIKV+y+kHsZNwdb/wm3+ApyzqD7D5CLbtINbg9QG8aEfSN2RKHZ1BOibyad6CYrOKxcWy6sQ1ZueIYWfL9jwJYXuoY5+xSanUbUPqT3VpJWLCxi3Ulm4wo7ZkdFOyn2wWtmkJjixy++XPlXW/fuA9dWpWUqY6zCcBd2jcfAHlrE6m0rs2Blq7bWYKE8KeBMs6WIDcEbfNHBdaYMzEeZQfwcDaMteHZVquBsYV2zC0yN4cxMc5FgijBHz4RpZOTWZqtr4svcOvAdfqWI26uxWxMP2TJYKjcDCh5EdeUwK8+SM6U8srbAE2uMSXpafs4cFouuXkl0T+2izMTV9h1bN+SH338glb3VuncfKIjRq5XFk2JnjDzkwkyysLpKk/Nck8aoHeciiiCCz07rV8PKsha6kvSBQbo0BCbO2KIu6uoWGBkDSQMYES7dmWgRkmTsHWgFXjXCpPCy1HqJjSXxNi8sbrbZg7c+3GiX0dcevSMA2yA4LniCAA1Sfh0FYeSrUBJBlM0zLL5HhXspLCZZWDRIgDg4LO05DXOj2PysOjBOde20IQ35DK6zdb92qHDbVdryxyZa26GN9de1Lj4rsn0W6Shspy2wAehPkfu0EYJ7itFqzGH0CiRsy0cMAG7EAEwXD4tUWETErcMgYRukRTXHBDOBpaFaVuyCBcSMcZnM2O00gMKnfwDobKYTwVsA57qwFmAAFImGP1Yjq53ex/C+Yd7nzP3kcD8QcRkBXbVbHE0PN0y1U6tFhoVaTANRaZupIefNJ/DFNSAIivuQje7am4EAU7H0MQN3j+DYKHWpB0EkbGXzlBFEOQhiiIFpNjrR/OKgE88LnOAEI54OCMZcnBP8HvKzr95XKQta1CwBz4Zm1WgDRZ4pJMaPKBLP8Lz/8p6zznJxIcxpixMBicpJomAviAhkAWTMhGQbtIaJrNc5WaZNDX7TkKEQX6vTKsO4uV0o8YYR3U9KzLnBp3rkNJB1kHbLGplituQYuEgaGej1UY7VhtnOK4iI6wY+bZNtj1w7I0lB67oZBqoBKLVyOOkNh4UUoSsQSOA/+GJeO5eQnxBaw0BDaSCRL7z5G21m3ngMU/FBEVtcgO50qYHEVOKEEJkHaKDK4wLMdLZ/xs1Z9uOBHI1dYWrEjmUhgdK1tUFB5LK5GjlGj2C0mVcDx6qVJEEJPRmeDeHRA/JspQKc4V5tIEOBOSD5KyI/9mHr4ilQJrk8s7l7E6RAo4ET7oPI/RJFeQNpdvkFxkXYP4By96mIZ0xIRdAGGIN3AA0Iz3gwGvrSzPfh7y4XNwnrOd1ZvtIICT2SMWjLUQMUpYsMY46+mC46Q73qeAm1RrwI/hg1D3dVcGEruI8FnHsqyGww7AvrTFryGULPLe8eRNDM4xJBuLwGkPwaQO4SQWk8iqBUXwkga917EfU8oNx7EfU8oNx7EfW8dWcEJQ9BjDlQRnAPryUi8LIoijrUUjW4E8n5LIbuQyhPOPFdCDmk68N3Fsi3vqGRUBx91+buuTg3ZVK+S0D9TQC6N+qiXwWgOxTgRwKwqk9jIYg6GMAFxY2Bgs+yf0G5InOSbbXdaACTdGlgewLkKgJvWogTVI9CvdcttLoVGsNE2U5IC8q+nw4qcNBxcVDZDtp3wQE0S4ooq2G/AB3oekE1XGHFjkr1ZIsW07sCaTj+6wLrUBPuWYGV5l2BNUCwDwqso75ynxRYkQv4gchCCoZDkVTVvZDthY3TdCz89RRVZ9IOXBC2tFtLGoRbXUWzmFBKo5aF0ByzZ1gFdlBM1S/CTgHqyRTuA0F0w39HQe0eUeAnWtDdicEPtaC7E4MPtF3F1cwIDFh2oPqHbbTPH9aHzr4LKnQPsTbLIxNu0Yhsei8gaQ4IFbMKatIhiFZkOyCxy/Xf6bSSETlK2jQxPqKtZgKBYolTYu0wGp9bcchofytsgzbU/bsatwS2tj+Omecum1rpGTS8ALOMC0pYELwnzAds6DYdfifDhuqx5zJAytkssTz8UOEMw+p3S2w1ZqMY2KKXRodvVjcFdfKjHGztiRf65A0Y7DHy4nZfiS73oxKFMMrEGaQChSYLt0HD4+YNEJLoQp6ewABROUB0otDZsaIe7CtAz8EHtIEFwdyYTTUhZfORfxXzlmfrPmLt2RePWjZ4vqEDXrni434AZOUBB5Bx1mQIgdQ8vC5A1sA7RevY1coWIp5RFn8Vy+62Wv4qlrkqNg3SggazN6eIjcWl12bvAziHQdyQfChftiY6vxYfcWXJBqnObKsF5oG+hO3g6qjDt1RY91JBHC41r5otiqxO3fPZP0rgRnNHEdIotA744Cn0hrz7egmRj5cQMAR9fwsBUuLIHH/mq//wPeQloZ35zJ0J7Vs6M/nwRkI7GdF9nNBuXhe6b+ksJjRIV8g24LgBuX+lrd9ZaxbfIEZBX4h8OE2Ewpi9Qbfb+/OIhQCmjhhHwQHpDeVV4a+xtIVMt7rPZ1ZqXnpx5a/L9ad1/4uy/SZnuc9eYNznLPfaC4z7jNRS+zJvreRaJPv/TFEoDHAE+HlNsENlyFXwFMIXi1GceuNez8qHvfLs0IyFp1kAytQt5sGIzbxOOQDuqP7TEuKtxPM477j3E8/jvONeTzzth71bbT+s6A4zoipBifPNxftCOSNWfNe5i7wm1Jo5OBwdMId8cFW/JAjH5iBBX04AZwsDQaT/C/zvYdfjdlYrAAABhGlDQ1BJQ0MgcHJvZmlsZQAAeJx9kT1Iw0AcxV9TpaIVBwuKOASsThZERRy1CkWoEGqFVh1MLv0QmjQkKS6OgmvBwY/FqoOLs64OroIg+AHi5Oik6CIl/i8ptIjx4Lgf7+497t4BQq3ENKttDNB020wl4mImuyKGXhFGF/owhJDMLGNWkpLwHV/3CPD1Lsaz/M/9ObrVnMWAgEg8wwzTJl4nntq0Dc77xBFWlFXic+JRky5I/Mh1xeM3zgWXBZ4ZMdOpOeIIsVhoYaWFWdHUiCeJo6qmU76Q8VjlvMVZK1VY4578heGcvrzEdZqDSGABi5AgQkEFGyjBRoxWnRQLKdqP+/gHXL9ELoVcG2DkmEcZGmTXD/4Hv7u18hPjXlI4DrS/OM7HMBDaBepVx/k+dpz6CRB8Bq70pr9cA6Y/Sa82tegR0LMNXFw3NWUPuNwB+p8M2ZRdKUhTyOeB9zP6pizQewt0rnq9NfZx+gCkqavkDXBwCIwUKHvN590drb39e6bR3w9GW3KV1ByxfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+QMCxcuIQ33NbMAAAAodEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVAgYnkgR2FlbGljR3JpbWV30quOAAADHUlEQVR42uXZy0tUURzA8a+/wtTJZ5ZJQhHkA6OI3pmZjqv5E9q0K3ou0kWbatEiKJgKWkQtIogiRSR6UNGDqFCR8ZUZjZRZOhWYxZhmqTOtKs1xnMd93wOzmTnnd36/OZ+595w7Cb58hnO9pGDD1lvMoDTkcRSbtsZcqqU3iTO+Ar7brfi+Ivy+RC4DUFdBVRCCdnrVONkNIAB2U9BfyFDfPC5OedNOCmqd7P9Tt/y9ItpEwad8Rj7M43zID+2goK6Cqsk1y5T7osUVfF7Bj94kzobtZGUF9RUc/r9embY7sqiCgeX87EnCHVFnKyq4UR56xysh98gWUzC4jLE3yZyKapCVFNws5/hMdcqMJyWLKPi6lLHuZE7ENNgKCm5v52S4GiXsednkCvx5THhTZuZveQV3yjg9W30y61MTkyrwL2HitYNjigQzo4K7ZZyLpDaJpJPZFAwvJvDKwRFFg5pJwf1tXIi0Lom0o1kUjOQQ6Jo//dBjGwUPSrkUTU0STWejKxjNJvgyVaXVN4OCh6VcibYeiXaAURWMZhPsTKVak8mMqODxVmpiqUViGWQ0Bb8yCL5I5ZCmkxpJwZMS6mOtQ2IdaBQFY2nQkcZBXSY3goKnJdyKpwaJZ7DeCsYd0K7X6htBwfMt3Is3f4k3gF4Kxh3Qls4+Q9yG9FDQsJlHSuQuSgTRWkEgEdrS//3FbTsFTZt4plTeolQgrRQEEqElgz2GPI5qoaB5I41K5ixKBlNbQVCgJdMgV349FHg24FE6X1E6oFoKggKtmRwwxWNpNRS0rqddjVxFjaBqKPBkGfy3r6aCjnV0qZWnqBVYSQWeLJ1PfHoq6FyLV80cRc3gSihoXmCwPb+WCrrW0KN2fqL2BPEoaF5osiu/kgq8q+nXIjfRYpJYFDQuYi9WatEo6F7FR63yEq0mikZBU45J7/tKKHi7kgG3iwRLfgFuF3P6CxgK9wVcrWQHVm7hFLwr5otlVz8SBdcq2YkdWigF74v45nZpd1E2nILrTnZhpzZZQV8hftusfigFtU6L7PljUeDLZ9jtYq5eOfwGcH5/poxGOy4AAAAASUVORK5CYII='
UP64 = b'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'

CWD = PATH.abspath(".")
if CWD.find("_android") > -1:
	CONFIGDIRECTORY = ""
	UPIMAGE = UP64
	DOWNIMAGE = DN64
	SG.ChangeLookAndFeel("DarkPurple6")
elif CWD.find("_DEV") > -1:
	SG.ChangeLookAndFeel("DarkGreen5")
	CONFIGDIRECTORY = "/home/will/.config/biditi_DEV/"
	UPIMAGE = UP16
	DOWNIMAGE = DN16
else:
	CONFIGDIRECTORY = "/home/will/.config/biditi/"
	SG.ChangeLookAndFeel("DarkPurple6")
	UPIMAGE = UP16
	DOWNIMAGE = DN16