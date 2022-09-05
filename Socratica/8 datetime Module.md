# Datetime Module Python Help Result
>>> import datetime
>>> help(datetime.date)
Help on class date in module datetime:

class date(builtins.object)
 |  date(year, month, day) --> date object
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __format__(...)
 |      Formats self with strftime.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __radd__(self, value, /)
 |      Return value+self.
 |
 |  __reduce__(...)
 |      __reduce__() -> (cls, state)
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  ctime(...)
 |      Return ctime() style string.
 |
 |  isocalendar(...)
 |      Return a named tuple containing ISO year, week number, and weekday.
 |
 |  isoformat(...)
 |      Return string in ISO 8601 format, YYYY-MM-DD.
 |
 |  isoweekday(...)
 |      Return the day of the week represented by the date.
 |      Monday == 1 ... Sunday == 7
 |
 |  replace(...)
 |      Return date with new specified fields.
 |
 |  strftime(...)
 |      format -> strftime() style string.
 |
 |  timetuple(...)
 |      Return time tuple, compatible with time.localtime().
 |
 |  toordinal(...)
 |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
 |
 |  weekday(...)
 |      Return the day of the week represented by the date.
 |      Monday == 0 ... Sunday == 6
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  fromisocalendar(...) from builtins.type
 |      int, int, int -> Construct a date from the ISO year, week number and weekday.
 |
 |      This is the inverse of the date.isocalendar() function
 |
 |  fromisoformat(...) from builtins.type
 |      str -> Construct a date from the output of date.isoformat()
 |
 |  fromordinal(...) from builtins.type
 |      int -> date corresponding to a proleptic Gregorian ordinal.
 |
 |  fromtimestamp(timestamp, /) from builtins.type
 |      Create a date from a POSIX timestamp.
 |
 |      The timestamp is a number, e.g. created via time.time(), that is interpreted
 |      as local time.
 |
 |  today(...) from builtins.type
 |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  day
 |
 |  month
 |
 |  year
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  max = datetime.date(9999, 12, 31)
 |
 |  min = datetime.date(1, 1, 1)
 |
 |  resolution = datetime.timedelta(days=1)

# Datetime Format modifiers

| Directive |	Description |	Example |
|-----------|---------------|-----------|
|%a         |	Weekday, short version  | 	Wed  |	
|%A         |	Weekday, full version  |	Wednesday 	
|%w         |	Weekday as a number 0-6, 0 is Sunday | 	3  |	
|%d        |	Day of month 01-31  |	31 	
|%b        |	Month name, short version  |	Dec 	
|%B        |	Month name, full version  |	December 	
|%m        |	Month as a number 01-12  |	12 	
|%y        |	Year, short version, without century  |	18 	
|%Y        |	Year, full version  |	2018 	
|%H        |	Hour 00-23  |	17 	
|%I        |	Hour 00-12  |	05 	
|%p        |	AM/PM  |	PM 	
|%M        |	Minute 00-59  |	41 	
|%S        |	Second 00-59  |	08 	
|%f        |	Microsecond 000000-999999  |	548513 	
|%z        |	UTC offset  |	+0100  |	
|%Z        |	Timezone  |	CST  |	
|%j        |	Day number of year 001-366  |	365  |	
|%U        |	Week number of year, Sunday as the first day of week, 00-53  |	52 	
|%W  |	Week number of year, Monday as the first day of week, 00-53  |	52 	
|%c  |	Local version of date and time  |	Mon Dec 31 17:41:00 2018 	
|%x  |	Local version of date  |	12/31/18 	 |
|%X  |	Local version of time  |	17:41:00 	 |
|%%  |	A % character  |	% 	 |
|%G  |	ISO 8601 year  |	2018  |	
|%u  |	ISO 8601 weekday (1-7)  |	1 	
|%V  |	ISO 8601 weeknumber (01-53)  |	01 |