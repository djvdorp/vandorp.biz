Title: Recent database tricks learned
Date: 2013-12-20 18:16
Author: Daniel
Tags: development, internet
Slug: recent-database-tricks-learned

Lately I've been busy working with databases for my spare time projects.
I imported a huge dump of data into the db via CSV import, but forgot to
add an Unique Id Column (Primary Key). Not willing to do the whole
import job again, I searched for a solution online to add an Id column
to an existing table without any hassle, and found one:

```sql
ALTER TABLE \`tablename\` ADD COLUMN \`id\` INT AUTO\_INCREMENT UNIQUE FIRST;
```

Another trick was the CSV import itself. Pretty much all data can be
inserted into MySQL by using an CSV export, in my case, from an ESRI
Shapefile.

The 0th row of the CSV file can even contain column names, which will
then be added to the newly created MySQL table in the database if you
like so!

Yet another helpful thing I found out is that while MySQL doesn't
support Materialized Views, there is an solution available for a kind of
Materialized View which will also give huge performance gains compared
to a regular view (as the data is static in the mat.view). The creation
of the 'Materialized View for MySQL' here will take some time, just like
updating, but querying it is blazingly fast:

```sql
DROP TABLE IF EXISTS `myDatabase`.`myMaterializedView`;  
CREATE TABLE `myDatabase`.`myMaterializedView` SELECT * from `myDatabase`.`myRegularView`;
```

When I managed to join the 2 tables needed in a view, and then in a
Materialized View, I found out that the Materialized View contained all
information I needed for my project. So, to speed up the performance, I
decided to port it to a NoSQL-database (MongoDb in my case). MySQL makes
this pretty easy when you have a table you want to export (and our
Materialized View is pretty much a table!), so we can choose to export
the data to CSV (or even JSON, which I need to try myself yet!):

> If your database is simple and you only have individual tables that
> you want to import (meaning: there are no JOINs between the tables)
> you can very simply export your data form MySQL to a CSV file and then
> import that CSV file with [mongoimport](http://docs.mongodb.org/manual/reference/program/mongoimport/) to MongoDB.

If we do however have relations, I have found [an excellent blogpost
here](http://tamas.io/converting-your-data-from-mysql-to-mongodb/) on how to proceed.

I have worked with MongoDb in the past, so I know most of it and it's
terms already. However, new users might be confused. That's why I'm also
linking [an SQL to MongoDB Mapping Chart here](http://docs.mongodb.org/manual/reference/sql-comparison/) for your convenience.

Happy devving!