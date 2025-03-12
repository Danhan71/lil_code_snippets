Make git automatically clear nb outputs before commit

Add this to .gitconfig in home dir
```
[filter "strip-notebook-output"]
    clean = "jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR"
```

Add this to a .gitattributes file in repo
```
*.ipynb filter=strip-notebook-output
```

[Source](https://stackoverflow.com/a/58004619)
