#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed="Mutt"):
        self.name=name
        self.breed=breed

scooby=Dog("Scooby","Bulldog")
print(scooby.name)
print(scooby.breed)