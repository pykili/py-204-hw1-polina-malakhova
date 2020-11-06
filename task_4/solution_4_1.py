for i in "a"*10:

    user_in=input()
    bad_string=""
    if user_in!=bad_string and user_in[0]!="#":

        num_of_tab = 0
        form = ""

        for letter in user_in:
            if num_of_tab == 1:
                form = form + letter

            if letter=="\t":
                num_of_tab += 1

        num_of_tab=0
        lemma = ""

        for letter in user_in:
            if num_of_tab == 2:
                lemma=lemma + letter

            if letter=="\t":
                num_of_tab += 1
	
        if form!=lemma:
            print(form,lemma)
