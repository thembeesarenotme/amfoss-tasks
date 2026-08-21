class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.strip()
        words=w.split()
        ls=[]
        for i in range(len(words)-1,-1, -1):
            ls.append(words[i])
        st=str(ls) 
        st1=st.strip('[]')
        st2=st1.replace("'","")
        st3=st2.replace(",","")
        return st3
        

