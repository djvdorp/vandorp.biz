Title: How to auto-generate Doctrine db migrations
Date: 2012-03-19 11:03
Author: Daniel
Tags: development, symfony
Slug: how-to-auto-generate-doctrine-db-migrations

Because I always seem to forget this (for Symfony 1.4 btw).  
(this assumes you have a running system with an existing database)

first, edit schema.yml

then run this from the command line:  
symfony doctrine:generate-migrations-diff

then run symfony doctrine:build --all-classes

 

a migration will be generated in /lib/migration/doctrine
