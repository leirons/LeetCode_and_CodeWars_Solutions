def anagrams(word, words):
   res = []
   for i in words:
      if str(sorted(word)) == str(sorted(i)):
         res.append(i)
   return res
