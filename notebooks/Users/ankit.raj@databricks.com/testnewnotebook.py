# Databricks notebook source
print("Second notebook started")
dbutils.widgets.text("foo", "fooDefault", "fooEmptyLabel")
print(dbutils.widgets.get("foo"))
