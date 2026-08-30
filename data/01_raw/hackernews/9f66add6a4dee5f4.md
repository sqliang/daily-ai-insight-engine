---
title: When str.lower() is a security vulnerability in Python
source: https://sethmlarson.dev/when-str-lower-is-a-security-vulnerability
author:
- '[[rbanffy]]'
published: '2026-08-25'
created: '2026-08-26'
manifest_dates:
- '2026-08-26'
description: 'Article URL: https://sethmlarson.dev/when-str-lower-is-a-security-vulnerability
  Comments URL: https://news.ycombinator.com/item?id=49440410 Points: 120 # Comments:
  49'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 9f66add6a4dee5f4
---

Some internet standards only support ASCII characters, but the world uses much more than the Latin alphabet. Thus, a mapping from Unicode to ASCII for use in domain names is required.

NamePrep was part of that solution, defined in RFC 3491 as a profile of StringPrep, and is crucially a component of Internationalizing Domain Names in Applications (IDNA), also known as “IDNA 2003”. The StringPrep algorithm is defined in RFC 3454. IDNA 2003 has been obsoleted by IDNA 2008 defined in RFC 5890, 5891, 5892, and 5893.

Python supports IDNA 2003 through the `idna`

codec (`str.encode('idna')`

) and
IDNA 2008 is supported by the `idna`

package on the Python package Index.
Python's implementation of StringPrep is implemented in the `stringprep`

module
in the standard library. In general, you should be using the `idna`

package (IDNA 2008)
and not `.encode("idna")`

(IDNA 2003), but sometimes you
do need the older behavior.

StringPrep defines the “case folding” step (case folding is approximately “how to lowercase/uppercase a codepoint”) in Section 3.2, enabling case-insensitive
comparisons of strings, by mapping all characters through mapping tables B.2 and B.3.
B.2 is effectively `str.lower()`

, lowercasing all characters according to
Unicode rules and B.3 contains the exceptions. The Python code implementing
this (and assuming B.3 table is captured correctly) is the following code below:

```
def map_table_b3(code):
r = b3_exceptions.get(ord(code))
if r is not None: return r
return code.lower()
```


And that might seem fine... and the title probably gave it away already.
The `str.lower()`

call in this function is a vulnerability!

Why? Because `str`

uses whatever Unicode data that the particular Python
interpreter is shipped with, you can figure out what Unicode version your
Python interpreter uses by accessing `unicodedata.unidata_version`

:

```
>>> import unicodedata
>>> unicodedata.unidata_version
'17.0.0'
```


There's also a database of Unicode 3.2.0 data available on every version
of Python (`unicodedata.ucd_3_2_0`

) specifically for the StringPrep and IDNA algorithms:

```
$ grep -I "ucd_3_2_0" -R Lib/
Lib/stringprep.py:from unicodedata import ucd_3_2_0 as unicodedata
Lib/encodings/idna.py:from unicodedata import ucd_3_2_0 as unicodedata
```


This is important! StringPrep depends on this specific version of Unicode
to operate consistently, the B.2 and B.3 tables in RFC 3454 are essentially
Unicode 3.2.0 case-folding rules encoded into
a table. So we need to use Unicode 3.2.0 case-folding rules, not newer
Unicode case-folding rules. This is why calling `str.lower()`

represents
a difference in the implementation and the specification,
and therefore a vulnerability:

```
# RFC 3454 compliant value ('Ꭰ' is U+13A0)
>>> "ᎠᎠ".encode("idna")
'xn--58da'
# Value if using Unicode 17.0.0 case-folding
>>> "ᎠᎠ".encode("idna")
'xn--kz9aa'
```


The fix was to create new exceptions so that `str.lower()`

would behave
as if it was using Unicode 3.2.0 for only particular function. So, we
go through each Unicode codepoint and record when the behavior of
`str.lower()`

is different when comparing the Unicode version shipped with Python and Unicode 3.2.0.
And that's all, now IDNA 2003 is consistent with the specification.

Thanks to Bitshift for reporting the vulnerability, Stan Ulbrych for co-developing the remediation, and Marc-Andre Lemburg and Petr Viktorin for reviewing the remediation. See CVE-2026-17084 for more details.

md5-372ecb8017279e9daff2de5f9c3b41f6


Wow, you made it to the end!


- Share your thoughts with me on Mastodon, email, or Bluesky.
- Browse this blog’s archive of 193 entries.
- Check out this list of cool stuff I found on the internet.
- Follow this blog on RSS or the email newsletter.
- Go outside (best option)