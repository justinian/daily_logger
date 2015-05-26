#!/bin/bash
 
BASENAME=worklog
LOGDIR="${HOME}/Dropbox/Work/Daily"
LOGNAME=`date +"%Y.%m.%d.md"`
 
TMPFILE=`mktemp /tmp/${BASENAME}.XXXXXX.md` || exit 1
LOGFILE="${LOGDIR}/${LOGNAME}"
 
# Insert header information
echo "$(date +"### _%l:%M %p_") $*" > ${TMPFILE}
echo >> ${TMPFILE}
 
# Open editor
if ${EDITOR} "${TMPFILE}"; then
	echo >> "${LOGFILE}"
	cat "${TMPFILE}" >> "${LOGFILE}"
fi

rm "${TMPFILE}"
