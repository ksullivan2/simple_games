Finishing the game seems to crash it:
```
File "./StrategoGame.py", line 188, in player_conflict
     self.piece_death(loser)
   File "./StrategoGame.py", line 193, in piece_death
     piece.dead = True
 AttributeError: 'NoneType' object has no attribute 'dead'
 ```
