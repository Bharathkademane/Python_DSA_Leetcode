class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1=strs[0]
        s=''
        for i in range(1,len(strs)):
            s2=strs[i]
            
            m=0
            b=min(len(s1),len(s2))
          
            
            while(m<b):
                
                if s1[m]==s2[m]:
                    s+=s1[m]
                  
                else:
                    break 
                m+=1    
            s1=s
            s=''
        return s1
        
