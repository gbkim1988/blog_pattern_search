﻿#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      YES24
#
# Created:     19-04-2017
# Copyright:   (c) YES24 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# case test 1

from io import StringIO as strIo

ori = """
A	 	 	 	 	 	anchor
ABBR	 	 	 	 	 	abbreviated form (e.g., WWW, HTTP, etc.)
ACRONYM
ADDRESS	 	 	 	 	 	information on author
APPLET	 	 	 	D	L	Java applet
AREA	 	F	E	 	 	client-side image map area
B	 	 	 	 	 	bold text style
BASE	 	F	E	 	 	document base URI
BASEFONT	 	F	E	D	L	base font size
BDO	 	 	 	 	 	I18N BiDi over-ride
BIG	 	 	 	 	 	large text style
BLOCKQUOTE	 	 	 	 	 	long quotation
BODY	O	O	 	 	 	document body
BR	 	F	E	 	 	forced line break
BUTTON	 	 	 	 	 	push button
CAPTION	 	 	 	 	 	table caption
CENTER	 	 	 	D	L	shorthand for DIV align=center
CITE	 	 	 	 	 	citation
CODE	 	 	 	 	 	computer code fragment
COL	 	F	E	 	 	table column
COLGROUP	 	O	 	 	 	table column group
DD	 	O	 	 	 	definition description
DEL	 	 	 	 	 	deleted text
DFN	 	 	 	 	 	instance definition
DIR	 	 	 	D	L	directory list
DIV	 	 	 	 	 	generic language/style container
DL	 	 	 	 	 	definition list
DT	 	O	 	 	 	definition term
EM	 	 	 	 	 	emphasis
FIELDSET	 	 	 	 	 	form control group
FONT	 	 	 	D	L	local change to font
FORM	 	 	 	 	 	interactive form
FRAME	 	F	E	 	F	subwindow
FRAMESET	 	 	 	 	F	window subdivision
H1	 	 	 	 	 	heading
H2	 	 	 	 	 	heading
H3	 	 	 	 	 	heading
H4	 	 	 	 	 	heading
H5	 	 	 	 	 	heading
H6	 	 	 	 	 	heading
HEAD	O	O	 	 	 	document head
HR	 	F	E	 	 	horizontal rule
HTML	O	O	 	 	 	document root element
I	 	 	 	 	 	italic text style
IFRAME	 	 	 	 	L	inline subwindow
IMG	 	F	E	 	 	Embedded image
INPUT	 	F	E	 	 	form control
INS	 	 	 	 	 	inserted text
ISINDEX	 	F	E	D	L	single line prompt
KBD	 	 	 	 	 	text to be entered by the user
LABEL	 	 	 	 	 	form field label text
LEGEND	 	 	 	 	 	fieldset legend
LI	 	O	 	 	 	list item
LINK	 	F	E	 	 	a media-independent link
MAP	 	 	 	 	 	client-side image map
MENU	 	 	 	D	L	menu list
META	 	F	E	 	 	generic metainformation
NOFRAMES	 	 	 	 	F	alternate content container for non frame-based rendering
NOSCRIPT	 	 	 	 	 	alternate content container for non script-based rendering
OBJECT	 	 	 	 	 	generic embedded object
OL	 	 	 	 	 	ordered list
OPTGROUP	 	 	 	 	 	option group
OPTION	 	O	 	 	 	selectable choice
P	 	O	 	 	 	paragraph
PARAM	 	F	E	 	 	named property value
PRE	 	 	 	 	 	preformatted text
Q	 	 	 	 	 	short inline quotation
S	 	 	 	D	L	strike-through text style
SAMP	 	 	 	 	 	sample program output, scripts, etc.
SCRIPT	 	 	 	 	 	script statements
SELECT	 	 	 	 	 	option selector
SMALL	 	 	 	 	 	small text style
SPAN	 	 	 	 	 	generic language/style container
STRIKE	 	 	 	D	L	strike-through text
STRONG	 	 	 	 	 	strong emphasis
STYLE	 	 	 	 	 	style info
SUB	 	 	 	 	 	subscript
SUP	 	 	 	 	 	superscript
TABLE
TBODY	O	O	 	 	 	table body
TD	 	O	 	 	 	table data cell
TEXTAREA	 	 	 	 	 	multi-line text field
TFOOT	 	O	 	 	 	table footer
TH	 	O	 	 	 	table header cell
THEAD	 	O	 	 	 	table header
TITLE	 	 	 	 	 	document title
TR	 	O	 	 	 	table row
TT	 	 	 	 	 	teletype or monospaced text style
U	 	 	 	D	L	underlined text style
UL	 	 	 	 	 	unordered list
VAR	 	 	 	 	 	instance of a variable or program argument
"""

attr="""
Name	Related Elements	Type	Default	Depr.	DTD	Comment
abbr	TD, TH	%Text;	#IMPLIED	 	 	abbreviation for header cell
accept-charset	FORM	%Charsets;	#IMPLIED	 	 	list of supported charsets
accept	FORM, INPUT	%ContentTypes;	#IMPLIED	 	 	list of MIME types for file upload
accesskey	A, AREA, BUTTON, INPUT, LABEL, LEGEND, TEXTAREA	%Character;	#IMPLIED	 	 	accessibility key character
action	FORM	%URI;	#REQUIRED	 	 	server-side form handler
align	CAPTION	%CAlign;	#IMPLIED	D	L	relative to table
align	APPLET, IFRAME, IMG, INPUT, OBJECT	%IAlign;	#IMPLIED	D	L	vertical or horizontal alignment
align	LEGEND	%LAlign;	#IMPLIED	D	L	relative to fieldset
align	TABLE	%TAlign;	#IMPLIED	D	L	table position relative to window
align	HR	(left | center | right)	#IMPLIED	D	L
align	DIV, H1, H2, H3, H4, H5, H6, P	(left | center | right | justify)	#IMPLIED	D	L	align, text alignment
align	COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR	(left | center | right | justify | char)	#IMPLIED
alink	BODY	%Color;	#IMPLIED	D	L	color of selected links
alt	APPLET	%Text;	#IMPLIED	D	L	short description
alt	AREA, IMG	%Text;	#REQUIRED	 	 	short description
alt	INPUT	CDATA	#IMPLIED	 	 	short description
archive	APPLET	CDATA	#IMPLIED	D	L	comma-separated archive list
archive	OBJECT	CDATA	#IMPLIED	 	 	space-separated list of URIs
axis	TD, TH	CDATA	#IMPLIED	 	 	comma-separated list of related headers
background	BODY	%URI;	#IMPLIED	D	L	texture tile for document background
bgcolor	TABLE	%Color;	#IMPLIED	D	L	background color for cells
bgcolor	TR	%Color;	#IMPLIED	D	L	background color for row
bgcolor	TD, TH	%Color;	#IMPLIED	D	L	cell background color
bgcolor	BODY	%Color;	#IMPLIED	D	L	document background color
border	TABLE	%Pixels;	#IMPLIED	 	 	controls frame width around table
border	IMG, OBJECT	%Pixels;	#IMPLIED	D	L	link border width
cellpadding	TABLE	%Length;	#IMPLIED	 	 	spacing within cells
cellspacing	TABLE	%Length;	#IMPLIED	 	 	spacing between cells
char	COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR	%Character;	#IMPLIED	 	 	alignment char, e.g. char=':'
charoff	COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR	%Length;	#IMPLIED	 	 	offset for alignment char
charset	A, LINK, SCRIPT	%Charset;	#IMPLIED	 	 	char encoding of linked resource
checked	INPUT	(checked)	#IMPLIED	 	 	for radio buttons and check boxes
cite	BLOCKQUOTE, Q	%URI;	#IMPLIED	 	 	URI for source document or msg
cite	DEL, INS	%URI;	#IMPLIED	 	 	info on reason for change
class	All elements but BASE, BASEFONT, HEAD, HTML, META, PARAM, SCRIPT, STYLE, TITLE	CDATA	#IMPLIED	 	 	space-separated list of classes
classid	OBJECT	%URI;	#IMPLIED	 	 	identifies an implementation
clear	BR	(left | all | right | none)	none	D	L	control of text flow
code	APPLET	CDATA	#IMPLIED	D	L	applet class file
codebase	OBJECT	%URI;	#IMPLIED	 	 	base URI for classid, data, archive
codebase	APPLET	%URI;	#IMPLIED	D	L	optional base URI for applet
codetype	OBJECT	%ContentType;	#IMPLIED	 	 	content type for code
color	BASEFONT, FONT	%Color;	#IMPLIED	D	L	text color
cols	FRAMESET	%MultiLengths;	#IMPLIED	 	F	list of lengths, default: 100% (1 col)
cols	TEXTAREA	NUMBER	#REQUIRED
colspan	TD, TH	NUMBER	1	 	 	number of cols spanned by cell
compact	DIR, DL, MENU, OL, UL	(compact)	#IMPLIED	D	L	reduced interitem spacing
content	META	CDATA	#REQUIRED	 	 	associated information
coords	AREA	%Coords;	#IMPLIED	 	 	comma-separated list of lengths
coords	A	%Coords;	#IMPLIED	 	 	for use with client-side image maps
data	OBJECT	%URI;	#IMPLIED	 	 	reference to object's data
datetime	DEL, INS	%Datetime;	#IMPLIED	 	 	date and time of change
declare	OBJECT	(declare)	#IMPLIED	 	 	declare but don't instantiate flag
defer	SCRIPT	(defer)	#IMPLIED	 	 	UA may defer execution of script
dir	All elements but APPLET, BASE, BASEFONT, BDO, BR, FRAME, FRAMESET, IFRAME, PARAM, SCRIPT	(ltr | rtl)	#IMPLIED	 	 	direction for weak/neutral text
dir	BDO	(ltr | rtl)	#REQUIRED	 	 	directionality
disabled	BUTTON, INPUT, OPTGROUP, OPTION, SELECT, TEXTAREA	(disabled)	#IMPLIED	 	 	unavailable in this context
enctype	FORM	%ContentType;	"application/x-www- form-urlencoded"
face	BASEFONT, FONT	CDATA	#IMPLIED	D	L	comma-separated list of font names
for	LABEL	IDREF	#IMPLIED	 	 	matches field ID value
frame	TABLE	%TFrame;	#IMPLIED	 	 	which parts of frame to render
frameborder	FRAME, IFRAME	(1 | 0)	1	 	F	request frame borders?
headers	TD, TH	IDREFS	#IMPLIED	 	 	list of id's for header cells
height	IFRAME	%Length;	#IMPLIED	 	L	frame height
height	TD, TH	%Length;	#IMPLIED	D	L	height for cell
height	IMG, OBJECT	%Length;	#IMPLIED	 	 	override height
height	APPLET	%Length;	#REQUIRED	D	L	initial height
href	A, AREA, LINK	%URI;	#IMPLIED	 	 	URI for linked resource
href	BASE	%URI;	#IMPLIED	 	 	URI that acts as base URI
hreflang	A, LINK	%LanguageCode;	#IMPLIED	 	 	language code
hspace	APPLET, IMG, OBJECT	%Pixels;	#IMPLIED	D	L	horizontal gutter
http-equiv	META	NAME	#IMPLIED	 	 	HTTP response header name
id	All elements but BASE, HEAD, HTML, META, SCRIPT, STYLE, TITLE	ID	#IMPLIED	 	 	document-wide unique id
ismap	IMG, INPUT	(ismap)	#IMPLIED	 	 	use server-side image map
label	OPTION	%Text;	#IMPLIED	 	 	for use in hierarchical menus
label	OPTGROUP	%Text;	#REQUIRED	 	 	for use in hierarchical menus
lang	All elements but APPLET, BASE, BASEFONT, BR, FRAME, FRAMESET, IFRAME, PARAM, SCRIPT	%LanguageCode;	#IMPLIED	 	 	language code
language	SCRIPT	CDATA	#IMPLIED	D	L	predefined script language name
link	BODY	%Color;	#IMPLIED	D	L	color of links
longdesc	IMG	%URI;	#IMPLIED	 	 	link to long description (complements alt)
longdesc	FRAME, IFRAME	%URI;	#IMPLIED	 	F	link to long description (complements title)
marginheight	FRAME, IFRAME	%Pixels;	#IMPLIED	 	F	margin height in pixels
marginwidth	FRAME, IFRAME	%Pixels;	#IMPLIED	 	F	margin widths in pixels
maxlength	INPUT	NUMBER	#IMPLIED	 	 	max chars for text fields
media	STYLE	%MediaDesc;	#IMPLIED	 	 	designed for use with these media
media	LINK	%MediaDesc;	#IMPLIED	 	 	for rendering on these media
method	FORM	(GET | POST)	GET	 	 	HTTP method used to submit the form
multiple	SELECT	(multiple)	#IMPLIED	 	 	default is single selection
name	BUTTON, TEXTAREA	CDATA	#IMPLIED
name	APPLET	CDATA	#IMPLIED	D	L	allows applets to find each other
name	SELECT	CDATA	#IMPLIED	 	 	field name
name	FORM	CDATA	#IMPLIED	 	 	name of form for scripting
name	FRAME, IFRAME	CDATA	#IMPLIED	 	F	name of frame for targetting
name	IMG	CDATA	#IMPLIED	 	 	name of image for scripting
name	A	CDATA	#IMPLIED	 	 	named link end
name	INPUT, OBJECT	CDATA	#IMPLIED	 	 	submit as part of form
name	MAP	CDATA	#REQUIRED	 	 	for reference by usemap
name	PARAM	CDATA	#REQUIRED	 	 	property name
name	META	NAME	#IMPLIED	 	 	metainformation name
nohref	AREA	(nohref)	#IMPLIED	 	 	this region has no action
noresize	FRAME	(noresize)	#IMPLIED	 	F	allow users to resize frames?
noshade	HR	(noshade)	#IMPLIED	D	L
nowrap	TD, TH	(nowrap)	#IMPLIED	D	L	suppress word wrap
object	APPLET	CDATA	#IMPLIED	D	L	serialized applet file
onblur	A, AREA, BUTTON, INPUT, LABEL, SELECT, TEXTAREA	%Script;	#IMPLIED	 	 	the element lost the focus
onchange	INPUT, SELECT, TEXTAREA	%Script;	#IMPLIED	 	 	the element value was changed
onclick	All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE	%Script;	#IMPLIED	 	 	a pointer button was clicked
ondblclick	All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE	%Script;	#IMPLIED	 	 	a pointer button was double clicked
onfocus	A, AREA, BUTTON, INPUT, LABEL, SELECT, TEXTAREA	%Script;	#IMPLIED	 	 	the element got the focus
onkeydown	All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE	%Script;	#IMPLIED	 	 	a key was pressed down
onkeypress	All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE	%Script;	#IMPLIED	 	 	a key was pressed and released
onkeyup	All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE	%Script;	#IMPLIED	 	 	a key was released
onload	FRAMESET	%Script;	#IMPLIED	 	F	all the frames have been loaded
onload	BODY	%Script;	#IMPLIED	 	 	the document has been loaded
onmousedown	All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE	%Script;	#IMPLIED	 	 	a pointer button was pressed down
onmousemove	All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE	%Script;	#IMPLIED	 	 	a pointer was moved within
onmouseout	All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE	%Script;	#IMPLIED	 	 	a pointer was moved away
onmouseover	All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE	%Script;	#IMPLIED	 	 	a pointer was moved onto
onmouseup	All elements but APPLET, BASE, BASEFONT, BDO, BR, FONT, FRAME, FRAMESET, HEAD, HTML, IFRAME, ISINDEX, META, PARAM, SCRIPT, STYLE, TITLE	%Script;	#IMPLIED	 	 	a pointer button was released
onreset	FORM	%Script;	#IMPLIED	 	 	the form was reset
onselect	INPUT, TEXTAREA	%Script;	#IMPLIED	 	 	some text was selected
onsubmit	FORM	%Script;	#IMPLIED	 	 	the form was submitted
onunload	FRAMESET	%Script;	#IMPLIED	 	F	all the frames have been removed
onunload	BODY	%Script;	#IMPLIED	 	 	the document has been removed
profile	HEAD	%URI;	#IMPLIED	 	 	named dictionary of meta info
prompt	ISINDEX	%Text;	#IMPLIED	D	L	prompt message
readonly	TEXTAREA	(readonly)	#IMPLIED
readonly	INPUT	(readonly)	#IMPLIED	 	 	for text and passwd
rel	A, LINK	%LinkTypes;	#IMPLIED	 	 	forward link types
rev	A, LINK	%LinkTypes;	#IMPLIED	 	 	reverse link types
rows	FRAMESET	%MultiLengths;	#IMPLIED	 	F	list of lengths, default: 100% (1 row)
rows	TEXTAREA	NUMBER	#REQUIRED
rowspan	TD, TH	NUMBER	1	 	 	number of rows spanned by cell
rules	TABLE	%TRules;	#IMPLIED	 	 	rulings between rows and cols
scheme	META	CDATA	#IMPLIED	 	 	select form of content
scope	TD, TH	%Scope;	#IMPLIED	 	 	scope covered by header cells
scrolling	FRAME, IFRAME	(yes | no | auto)	auto	 	F	scrollbar or none
selected	OPTION	(selected)	#IMPLIED
shape	AREA	%Shape;	rect	 	 	controls interpretation of coords
shape	A	%Shape;	rect	 	 	for use with client-side image maps
size	HR	%Pixels;	#IMPLIED	D	L
size	FONT	CDATA	#IMPLIED	D	L	[+|-]nn e.g. size="+1", size="4"
size	INPUT	CDATA	#IMPLIED	 	 	specific to each type of field
size	BASEFONT	CDATA	#REQUIRED	D	L	base font size for FONT elements
size	SELECT	NUMBER	#IMPLIED	 	 	rows visible
span	COL	NUMBER	1	 	 	COL attributes affect N columns
span	COLGROUP	NUMBER	1	 	 	default number of columns in group
src	SCRIPT	%URI;	#IMPLIED	 	 	URI for an external script
src	INPUT	%URI;	#IMPLIED	 	 	for fields with images
src	FRAME, IFRAME	%URI;	#IMPLIED	 	F	source of frame content
src	IMG	%URI;	#REQUIRED	 	 	URI of image to embed
standby	OBJECT	%Text;	#IMPLIED	 	 	message to show while loading
start	OL	NUMBER	#IMPLIED	D	L	starting sequence number
style	All elements but BASE, BASEFONT, HEAD, HTML, META, PARAM, SCRIPT, STYLE, TITLE	%StyleSheet;	#IMPLIED	 	 	associated style info
summary	TABLE	%Text;	#IMPLIED	 	 	purpose/structure for speech output
tabindex	A, AREA, BUTTON, INPUT, OBJECT, SELECT, TEXTAREA	NUMBER	#IMPLIED	 	 	position in tabbing order
target	A, AREA, BASE, FORM, LINK	%FrameTarget;	#IMPLIED	 	L	render in this frame
text	BODY	%Color;	#IMPLIED	D	L	document text color
title	All elements but BASE, BASEFONT, HEAD, HTML, META, PARAM, SCRIPT, TITLE	%Text;	#IMPLIED	 	 	advisory title
type	A, LINK	%ContentType;	#IMPLIED	 	 	advisory content type
type	OBJECT	%ContentType;	#IMPLIED	 	 	content type for data
type	PARAM	%ContentType;	#IMPLIED	 	 	content type for value when valuetype=ref
type	SCRIPT	%ContentType;	#REQUIRED	 	 	content type of script language
type	STYLE	%ContentType;	#REQUIRED	 	 	content type of style language
type	INPUT	%InputType;	TEXT	 	 	what kind of widget is needed
type	LI	%LIStyle;	#IMPLIED	D	L	list item style
type	OL	%OLStyle;	#IMPLIED	D	L	numbering style
type	UL	%ULStyle;	#IMPLIED	D	L	bullet style
type	BUTTON	(button | submit | reset)	submit	 	 	for use as form button
usemap	IMG, INPUT, OBJECT	%URI;	#IMPLIED	 	 	use client-side image map
valign	COL, COLGROUP, TBODY, TD, TFOOT, TH, THEAD, TR	(top | middle | bottom | baseline)	#IMPLIED	 	 	vertical alignment in cells
value	INPUT	CDATA	#IMPLIED	 	 	Specify for radio buttons and checkboxes
value	OPTION	CDATA	#IMPLIED	 	 	defaults to element content
value	PARAM	CDATA	#IMPLIED	 	 	property value
value	BUTTON	CDATA	#IMPLIED	 	 	sent to server when submitted
value	LI	NUMBER	#IMPLIED	D	L	reset sequence number
valuetype	PARAM	(DATA | REF | OBJECT)	DATA	 	 	How to interpret value
version	HTML	CDATA	%HTML.Version;	D	L	Constant
vlink	BODY	%Color;	#IMPLIED	D	L	color of visited links
vspace	APPLET, IMG, OBJECT	%Pixels;	#IMPLIED	D	L	vertical gutter
width	HR	%Length;	#IMPLIED	D	L
width	IFRAME	%Length;	#IMPLIED	 	L	frame width
width	IMG, OBJECT	%Length;	#IMPLIED	 	 	override width
width	TABLE	%Length;	#IMPLIED	 	 	table width
width	TD, TH	%Length;	#IMPLIED	D	L	width for cell
width	APPLET	%Length;	#REQUIRED	D	L	initial width
width	COL	%MultiLength;	#IMPLIED	 	 	column width specification
width	COLGROUP	%MultiLength;	#IMPLIED	 	 	default width for enclosed COLs
width	PRE	NUMBER	#IMPLIED	D	L
"""

def remote_duplicates(lst):
    """ parameter must be list type """
    # 중복된 것을 제거하는 방법은?
    # 다른 리스트에 복사하면서 중복된 내용을 제거한다.
    ret = list()
    for x in lst:
        if ret.count(x) == 0:
            ret.append(x)
    return ret

print([l.split('\t')[0].strip() for l in attr.splitlines()])

print(remote_duplicates([l.split('\t')[0].strip() for l in attr.splitlines()]))

with open('attr.list', 'w') as x:
    for l in remote_duplicates([l.split('\t')[0].strip() for l in attr.splitlines()]):
        if l is not "":
            x.write(l + "\n")




