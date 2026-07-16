---
title: SQLite should have (Rust-style) editions
source: https://mort.coffee/home/sqlite-editions/
author:
- '[[gnyeki]]'
published: '2026-07-15'
created: '2026-07-16'
manifest_dates:
- '2026-07-16'
description: 'Article URL: https://mort.coffee/home/sqlite-editions/ Comments URL:
  https://news.ycombinator.com/item?id=48928135 Points: 266 # Comments: 106'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: c9f6eb2af9ad4ae5
---

Date: 2026-07-15

Git: https://gitlab.com/mort96/blog/blob/published/content/00000-home/00017-sqlite-editions.md

SQLite is an amazing database engine. I use it as a database for plenty of embedded projects, and I don't think it's an exaggeration to call it the industry standard for local data storage. Some server software even uses it; for example, lobste.rs is now running on SQLite.

Unlike traditional RDBMSes (Relational DataBase Management Systems), SQLite is not a separate process; it's an RDBMS as a library, meaning your software remains self contained. Unlike traditional file formats, you don't need to write custom serializers and parsers. In some ways, it's the best of both worlds.

There's just one huge problem though. Its defaults are all wrong.

## Bad default #1: Foreign key constraints are ignored by default

You read that right. Foreign key constraints are arguably the primary tool we have to ensure that a database remains consistent and don't have dangling references.

As a quick primer, this is how an SQL foreign key constraint looks:

```
CREATE TABLE users (
id INTEGER PRIMARY KEY,
display_name TEXT
);
CREATE TABLE posts (
id INTEGER PRIMARY KEY,
user_id INTEGER NOT NULL,
content TEXT NOT NULL,
FOREIGN KEY(user_id) REFERENCES users(id)
);
```


The typical behavior for all other RDBMSes would be that the `user_id`

column
of a post must *always* reference the ID of a valid user.
You can't create a new post without providing a valid user ID,
you can't delete a user without also deleting its posts,
lest you get a foreign key constraint violation error.

The only RDBMS I'm aware of which doesn't enforce this by default is SQLite.

This is made even worse by SQLite's tendency to re-use `ROWID`

.
You see, in this example, those `INTEGER PRIMARY KEY`

rows become aliases
for the table's `ROWID`

, which is a unique integer ID assigned to every row
of a table in SQLite.
The algorithm for assigning `ROWID`

is a bit complicated
(more details in the SQLite documentation),
but it results in ID re-use in some cases.
This means that a dangling reference easily results in a reference to
the *wrong row*, which is even worse than a dangling reference because
everything will seem fine.
You don't even get an error during lookup.

Just look at this hypothetical sequence of operations in our toy database schema:

```
-- Bob creates a user account
INSERT INTO users (display_name) VALUES ('Bob');
SELECT * FROM users;
-- id | display_name
-- 1 | Bob
-- Bob posts an introduction post
INSERT INTO posts (user_id, content) VALUES (1, 'Hello, I am Bob');
SELECT u.display_name, p.content FROM users as u, posts as p WHERE u.id = p.user_id;
-- display_name | content
-- Bob | Hello, I am Bob
-- Bob deletes his account,
-- but we forgot to delete the posts.
-- SQLite doesn't produce an error because it ignores our foreign key.
DELETE FROM users WHERE id = 1;
-- Alice creates an account.
-- Alice gets the same ID that Bob had due to the ROWID algorithm.
INSERT INTO users (display_name) VALUES ('Alice');
SELECT * FROM users;
-- id | display_name
-- 1 | Alice
-- Alice has now inherited Bob's old post!
SELECT u.display_name, p.content FROM users as u, posts as p WHERE u.id = p.user_id;
-- display_name | content
-- Alice | Hello, I am Bob
```


The fix is to enable `foreign_keys`

with a pragma:

```
PRAGMA foreign_keys = ON;
```


If we had done this in the beginning,
the buggy `DELETE`

would have produced an error:

```
DELETE FROM users WHERE id = 1;
-- Runtime error: FOREIGN KEY constraint failed (19)
```


## Bad default #2: Columns can store the wrong data type

SQLite has a simple type system: a value can be `NULL`

, an `INTEGER`

,
a `REAL`

(aka a double precision float), `TEXT`

, or a `BLOB`

(aka binary data).
Consequently, a column can be defined to hold values of any of those types.

However, a column defined as an `INTEGER`

column isn't restricted to only integers;
instead, SQLite considers it to "use INTEGER affinity".
What this means is essentially:

- If you try to insert a
`TEXT`

value, and it is a valid string representation of an integer, it is converted to an integer and stored as such. - If you try to insert a
`TEXT`

value, and it is a valid string representation of a real number, it is converted to a real (aka double precision float) and stored as such. - Otherwise, the value is stored as-is.

Other affinities have different but simpler rules:

- Columns with
`BLOB`

affinity store values as-is. - Columns with
`TEXT`

affinity store`BLOB`

,`TEXT`

and`NULL`

values as-is, but convert numeric values to`TEXT`

. - Columns with
`REAL`

affinity work like columns with`INTEGER`

affinity except that integer values are converted to`REAL`

.

Here's how this looks in practice:

```
CREATE TABLE music (
id INTEGER PRIMARY KEY,
name TEXT,
duration_sec INTEGER
);
INSERT INTO music (name, duration_sec) VALUES ('Lost In Hollywood', 321);
INSERT INTO music (name, duration_sec) VALUES ('Comfortably Numb', 382);
INSERT INTO music (name, duration_sec) VALUES ('The Way of All Flesh', 'Way too long, I mean come on');
SELECT * FROM music;
-- id | name | duration_sec
-- 1 | Lost In Hollywood | 321
-- 2 | Comfortably Numb | 382
-- 3 | The Way of All Flesh | Way too long, I mean come on
```


I don't think I need to explain why it's a bad idea for a *database*
to be so careless about *data validation*.
It would be one thing if SQLite was an explicitly dynamically typed
document database, but it's not.
SQLite asks me through its syntax rules, "What type do you want to go into this column".

I once had to clean up a project where some code had accidentally been writing the
strings `'1'`

and `'0'`

to a column which was intended to store booleans (`1`

and `0`

).
That was not a fun debugging story.

Luckily, SQLite has the concept of strict tables, which makes SQLite produce a type error when the wrong type is inserted into a column:

```
CREATE TABLE music (
id INTEGER PRIMARY KEY,
name TEXT,
duration_sec INTEGER
) strict;
INSERT INTO music (name, duration_sec) VALUES ('The Way of All Flesh', 'Way too long, I mean come on');
-- Runtime error: cannot store TEXT value in INTEGER column music.duration_sec (19)
```


Unfortunately, there is no pragma to globally make all tables strict.
So you have to remember to add the `strict`

tag to every table manually.

There's a couple of arguments against strict tables which I want to cover here.

The authors of SQLite have written
about their preference for "flexible typing".
Personally, I find this a really strange piece of writing.
It doesn't provide any examples for why it could ever be useful to insert
a `BLOB`

into an `INTEGER`

column.
All it does is illustrate why it's sometimes useful to have a column
which can store values of any type.
Strict tables have a solution for that; it's called the `ANY`

data type.
You can still create columns which accept any value,
you just have to be explicit about it.

A much better argument
is provided by user 'zie' on lobste.rs.
You see, strict tables in SQLite don't just *enforce* types.
They also change the rules for how type specifiers are parsed.

Non-strict SQLite tables use the following rules to determine the type of a column (from SQLite's documentation):


- If the declared type contains the string "INT" then it is assigned INTEGER affinity.
- If the declared type of the column contains any of the strings "CHAR", "CLOB", or "TEXT" then that column has TEXT affinity. Notice that the type VARCHAR contains the string "CHAR" and is thus assigned TEXT affinity.
- If the declared type for a column contains the string "BLOB" or if no type is specified then the column has affinity BLOB.
- If the declared type for a column contains any of the strings "REAL", "FLOA", or "DOUB" then the column has REAL affinity.
- Otherwise, the affinity is NUMERIC.

A consequence of this rule, combined with SQLite's loose typing,
is that you can give your columns type names such as `DATETIME`

or `KEY_VALUE_SET`

or `COLOR`

,
and have a database connector/wrapper which automatically knows to
serialize and deserialize columns with custom types.
And if nothing else, those custom type names serve as useful documentation.

I have to acknowledge that just changing the default from non-strict tables to strict tables, with no further changes, would give up on this somewhat nifty quirk. However, I think we would be much better served by custom type aliases.

If we could write something like:

```
CREATE TYPE KEY_VALUE_SET = TEXT;
```


and then use `KEY_VALUE_SET`

as a type name in a strict table,
I think everyone would be happy.
I would probably start using such a feature liberally to document
the expected pattern of data in my columns.
In a real world schema,
you inevitably end up with `TEXT`

columns which have to be parsed
by application code.

As an aside to this aside, it would be neat if we could associate CHECK constraints with a custom type.


Update:'masklinn' on lobste.rs points out that the SQL 99 standard already specifies type aliases, called CREATE DOMAIN. This already supports constraints as well. So really, SQLite just needs to add support for the standard`CREATE DOMAIN`

statement.

## Bad default #3: SQLITE_BUSY errors with concurrent writers

SQLite allows multiple concurrent readers, but only one writer at a time.
By default, if you have two processes trying to acquire a write lock
at the same time, one of them will immediately receive an `SQLITE_BUSY`

error.

This is not the behavior I expect. I expect SQLite to wait for the lock to get unlocked, up to some timeout. It's doing disk IO after all, so I already structure my code with the assumption that a write could potentially be slow.

The default behavior has lead me to writing real-world bugs, where systems would sometimes just crash. I've manually written retry loops to fix it.

The fix is to set `busy_timeout`

with a pragma:

```
PRAGMA busy_timeout = 5000;
```


This makes SQLite try to acquire the lock for up to 5 seconds before erroring
with a `SQLITE_BUSY`

error.

I didn't learn about this setting until recently. It seems like such an obvious default that I'm astonished that it's not.


Update:I should add a note here about why support for concurrent writers is desirable.During normal operation, you're usually best served by structuring your software such that all writes are done by a single process, ideally a single thread. Concurrent writers will never be

fast. But there are non-typical situations. Maybe you need to manually clean up a database interactively using the`sqlite3`

tool interactively on the command line. Maybe you have scripts for uncommon administrative tasks which you haven't had the need to write a front-end for. These are perfectly legitimate and, I believe, fairly common use cases. I think it's bad that with SQLite's defaults, this kind use has a chance to just crash the software by making it throw an unexpected`SQLITE_BUSY`

error.

## Bad default 4: Performance

There's a lot to say about performance tuning in SQLite. When correctly configured, it can be a truly fast RDBMS, with the ability to fill roles we typically reserve for the big servers like PostgreSQL or MySQL.

But by default, its performance isn't great. Smarter people than me have written much more on this, and I recommend Sylvain Kerkour's Optimizing SQLite for servers if you're interested in this topic.

But the most significant bad default is that SQLite's Write-Ahead Log (WAL) is disabled by default. It can be enabled with:

```
PRAGMA journal_mode = WAL;
```


The WAL provides a dramatic write speed-up in most circumstances. Additionally, it lets us drastically reduce the amount of disk syncs without risking data corruption by changing another setting:

```
PRAGMA synchronous = NORMAL;
```


See the SQLite documentation on what exactly synchronous does.

## The solution: editions?

The oft-cited reason for why these defaults remain, well, default,
is of course backwards compatibility.
Changing defaults *now* would likely break lots of old software
and make people afraid to upgrade SQLite in the future in case it breaks everything again,
just like how I'm afraid to upgrade Python because every "upgrade"
breaks a bunch of software I use.
It's a laudbile and rare goal to try to not break your dependents.

However, I think the solution is simple: add one "super pragma" which changes all the bad defaults. I propose that the following:

```
PRAGMA edition = 2026;
```


should be an alias for at least the following set of pragmas:

```
PRAGMA foreign_keys = ON;
PRAGMA busy_timeout = 5000;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
```


And also make `strict`

mode the default for tables.

This should be a nice middle ground which avoids breaking backwards compatibility, but lets the database engine move forwards and not be bogged down by its own history.

The `edition`

idea is stolen straight from
Rust editions.
The advantage of a year-based edition rather than something like
JavaScript's `"use strict";`

is that as the years go by, the sensible defaults may change.
Maybe something like Hctree's WAL2
makes its way into the main branch, say, in the year 2034,
so maybe `PRAGMA edition = 2034`

will some day set `PRAGMA journal_mode = WAL2`

.

Anyway, that's all. I think SQLite should have an edition system with updated sets of defaults. Are there any things I've missed which makes this a bad idea? Or more pragmas which should be added to my imaginary "2026 edition"?