# Databricks notebook source
print("Parent Notebook Starting")
dbutils.notebook.run("testnewnotebook", 60, {"foo": "bar"})
