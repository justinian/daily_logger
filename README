# Daily log utility

I use this system to keep daily activity logs. It's simple, it lets me use Vim,
and it mostly stays out of my way while still making nice searchable notes.

## Installation

I use this in conjunction with Dropbox. So on my home linux box, I install
everything, and just use the log writing tool on all my other machines.

### On the central machine:

Requirements:
 * Python
 * pip
 * local smtp

```
git clone https://github.com/justinian/daily_logger.git
cd daily_logger
pip install -r requirements.txt
```

Edit `rollup.py` to include your email address and the email address for your
[Evernote notebook](https://evernote.com/contact/support/kb/#!/article/23480523).

Then edit your crontab (or other favorite automation tool) to run `rollup.py
<daily_dir> <monthly_dir>` at the start of each month.

### On all machines

Copy `log.sh` to somewhere in your path (I prefer `/usr/local/bin/log`) and be
sure to make it executable with `chmod a+x /usr/local/bin/log`.

## Usage

Just call `log [optional title for the timestamp]` and it will bring up your
editor to write your notes, and append it to the day's file. Once a month, the
rollup script will email the formatted markdown note to your Evernote notebook.
