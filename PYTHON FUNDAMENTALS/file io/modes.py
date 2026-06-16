#modes:

# r --> reading [default]

# W --> writing, truncates file first ->overwrite

# X --> creates new & open for writing

# a --> writing, appends at end

# b --> binary mode

# t --> text mode [default]

# + --> opens disk file for update(r & w)

with open("sample3.txt" , "x") as f :
    f.write("some random text")