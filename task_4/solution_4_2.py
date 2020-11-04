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

        number_of_letter=0
        wow_condition=""

        for i in lemma:
                if lemma[number_of_letter]==form[number_of_letter]:
                    number_of_letter+=1

                if number_of_letter==len(lemma)-1:
                    wow_condition="True"
        
        if wow_condition!="True":
            print(form,lemma)
