#!/usr/bin/env python
 
import os
import os.path
import re
import sys
import time

FROM_EMAIL = 'You <you@example.com>'
TO_EMAIL = 'Your Evernote Notebook Email <your.evernote.notebook@m.evernote.com>'
 
IN_DIR = sys.argv[1]
OUT_DIR = sys.argv[2]
 
daily_re = re.compile(r'([0-9]{4})\.([0-9]{2})\.([0-9]{2})\.md$')

def email_log(filename, month):
	import smtplib
	from cStringIO import StringIO
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	from markdown import markdownFromFile

	md = StringIO()
	markdownFromFile(input=filename, output=md)

	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Daily logs: %s @Default #dailylog" % (month,)
	msg['From'] = FROM_EMAIL
	msg['To'] = TO_EMAIL

	part = MIMEText(md.getvalue(), 'html')
	msg.attach(part)

	s = smtplib.SMTP('localhost')
	s.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
	s.quit()

 
MONTHS = {}
for entry in sorted(os.listdir(IN_DIR)):
	match = daily_re.match(entry)
	if match is None:
		continue
 
	year = match.group(1)
	month = match.group(2)
	day = match.group(3)
	if (year, month) not in MONTHS:
		MONTHS[(year, month)] = []
	MONTHS[(year, month)].append(entry)
 
 
for year, month in MONTHS:
	outfile_path = os.path.join(OUT_DIR, "%s.%s.md" % (year, month))
	outfile = file(outfile_path, "a")
	monthname = ""
 
	for entry in MONTHS[(year, month)]:
		fullpath = os.path.join(IN_DIR, entry)
		when = time.strptime(entry, "%Y.%m.%d.md")
		if not monthname:
			monthname = time.strftime("%b %Y", when)
		print >> outfile, "##", time.strftime("%a, %d %b %Y", when)
		outfile.write(file(fullpath).read())
		print >> outfile, ""
		os.unlink(fullpath)

	email_log(outfile_path, monthname)
