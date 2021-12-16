def csvmerge(nftfail, rarityfail, uusfail) :
    import pandas as pd
    df1 = pd.read_csv(nftfail)
    df2 = pd.read_csv(rarityfail)
    merged_inner = pd.merge(left= df1, right= df2, left_on="nimi",right_on="nimi")
    merged_inner.to_csv(uusfail, index= False)
csvmerge("oogabooga.csv","data2.csv","kolmas3.csv")
