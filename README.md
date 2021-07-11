# ChitterOPLBasic

ChitterOPLBasic is a Non-Linear Dialogue Engine that uses code blocks instead of plain text for passages.

## Why OPLBasic
For a long time I've dreamed have having a non-linear dialogue engine that instead of using plain text, would evaluate a code string. Unfortuntely because the risk of eval in JS, Python and others, you really can't do that. So I thought if I could find/make an interpreted language that didn't have access to the os, maybe this could be a reality. Enter "My Own Programming Language" (OPL) by davidcallanan. (On Youtube check out CodePulse).

The concept is simple. Using Twine, create your story. Instead of using english to write dialog, use OPLBasic. The ChitterOPLBasic engine will evaluate each code block to get the dialogue. Since your story is written in a programming language you can declare variables, test boolean conditions, do loops, and and even declare fuctions. Now you have dynamic text!

## Other Cool Things about ChitterOPLBasic
1. Completely seperate from the presentation layer. Each passage creates an "Emote" string to give commands to the presentation layer. ChitterOPLBasic sees this as just a string, so you can use keywords, hashtags, a list of numeric values. Even something as simple as a .jpg name.

2. Opens Twine Files. You make your story in Twine then archives your story. Now ChitterOPLBasic opens your .html and parses the story into a nodes table and an edges table.

3. Right now, ChitterOPLBasic is implemented in Python so you wouldn't be able to include that in a Unity game written in C#. However I in the Python directory of this repo, there is a tcpchitteroplserver.py file that will serve the dialogue of your game to a Unity client. Check out the Python client called tcpchitteroplclient.py
